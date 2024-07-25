#most of the basic features of MIS are implemented, but not all of them are properly show in the graphs, id be happy if someone made better graphs!

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import ipywidgets as widgets
from IPython.display import display, HTML

class ImprovedMorphingInfinitySpiral:
    def __init__(self, alpha=0.5+0.5j, beta=1+0j, num_points=1000, max_radius=5, max_time=100, time_step=0.1):
        self.alpha = alpha
        self.beta = beta
        self.num_points = num_points
        self.max_radius = max_radius
        self.max_time = max_time
        self.time_step = time_step
        self.t = 0
        self.fig = self.setup_figure()
        self.setup_widgets()

    def mis(self, z, t):
        z = np.where(np.abs(z) < 1e-10, 1e-10, z)
        log_z = np.log(z)
        power = np.power(z, self.alpha, where=np.abs(z) > 0)
        exp_term = np.exp(1j * t * np.power(log_z, self.beta, where=np.abs(log_z) > 0))
        return np.where(np.isfinite(power) & np.isfinite(exp_term), power * exp_term, 0)

    def create_spiral_points(self, t):
        # Create a grid in the complex plane
        x = np.linspace(-self.max_radius, self.max_radius, 200)
        y = np.linspace(-self.max_radius, self.max_radius, 200)
        X, Y = np.meshgrid(x, y)
        Z = X + 1j*Y

        # Apply the MIS function
        W = self.mis(Z, t)

        # Create a mask for points where |W| is within a certain range
        mask = (np.abs(W) > 0.1) & (np.abs(W) < 10)

        # Return the masked points and the full W array
        return W[mask], W

    def setup_figure(self):
        fig = make_subplots(rows=2, cols=2, 
                            specs=[[{'type': 'xy'}, {'type': 'xy'}],
                                   [{'type': 'xy'}, {'type': 'polar'}]],
                            subplot_titles=('MIS in Complex Plane', 'Magnitude Heat Map', 
                                            'Phase Heat Map', 'Polar Plot'))
        
        spiral_points, W = self.create_spiral_points(0)
        
        # MIS in Complex Plane
        fig.add_trace(go.Scatter(x=spiral_points.real, y=spiral_points.imag,
                                 mode='markers', marker=dict(size=5, color=np.angle(spiral_points),
                                                             colorscale='HSV', showscale=True,
                                                             colorbar=dict(title='Phase')),
                                 name='MIS'), row=1, col=1)
        
        # Magnitude Heat Map
        fig.add_trace(go.Heatmap(z=np.abs(W), colorscale='Viridis', name='Magnitude'), row=1, col=2)
        
        # Phase Heat Map
        fig.add_trace(go.Heatmap(z=np.angle(W), colorscale='HSV', name='Phase'), row=2, col=1)
        
        # Polar Plot
        r = np.linspace(0, self.max_radius, 100)
        theta = np.linspace(0, 2*np.pi, 100)
        R, Theta = np.meshgrid(r, theta)
        Z = R * np.exp(1j * Theta)
        W_polar = self.mis(Z, 0)
        fig.add_trace(go.Scatterpolar(r=np.abs(W_polar.flatten()), theta=np.angle(W_polar.flatten()),
                                      mode='markers', marker=dict(color=np.abs(W_polar.flatten()),
                                                                  colorscale='Viridis'),
                                      name='Polar MIS'), row=2, col=2)
        
        fig.update_layout(title='Improved Morphing Infinity Spiral',
                          height=800, width=1000,
                          showlegend=False)
        
        return go.FigureWidget(fig)

    def update_plot(self, t):
        spiral_points, W = self.create_spiral_points(t)
        W_polar = self.mis(np.linspace(0, self.max_radius, 1000) * np.exp(1j * np.linspace(0, 2*np.pi, 1000)), t)
        
        with self.fig.batch_update():
            # Update MIS in Complex Plane
            self.fig.data[0].x = spiral_points.real
            self.fig.data[0].y = spiral_points.imag
            self.fig.data[0].marker.color = np.angle(spiral_points)
            
            # Update Magnitude Heat Map
            self.fig.data[1].z = np.abs(W)
            
            # Update Phase Heat Map
            self.fig.data[2].z = np.angle(W)
            
            # Update Polar Plot
            self.fig.data[3].r = np.abs(W_polar)
            self.fig.data[3].theta = np.angle(W_polar)
            self.fig.data[3].marker.color = np.abs(W_polar)
            
            self.fig.layout.title.text = f'Improved MIS (t={t:.2f}, α={self.alpha}, β={self.beta})'

    def setup_widgets(self):
        self.play_button = widgets.Play(value=0, min=0, max=int(self.max_time/self.time_step), step=1, interval=50,
                                        description="Press play", disabled=False)
        self.slider = widgets.FloatSlider(value=0, min=0, max=self.max_time, step=self.time_step,
                                          description='Time', readout=True)
        widgets.jslink((self.play_button, 'value'), (self.slider, 'value'))
        self.slider.observe(self.on_value_change, names='value')
        
        self.alpha_real = widgets.FloatText(value=self.alpha.real, description='α (Real):')
        self.alpha_imag = widgets.FloatText(value=self.alpha.imag, description='α (Imag):')
        self.beta_real = widgets.FloatText(value=self.beta.real, description='β (Real):')
        self.beta_imag = widgets.FloatText(value=self.beta.imag, description='β (Imag):')
        
        self.max_radius_input = widgets.FloatText(value=self.max_radius, description='Max Radius:')
        self.max_time_input = widgets.FloatText(value=self.max_time, description='Max Time:')
        self.time_step_input = widgets.FloatText(value=self.time_step, description='Time Step:')
        
        for widget in [self.alpha_real, self.alpha_imag, self.beta_real, self.beta_imag, self.max_radius_input]:
            widget.observe(self.on_parameter_change, names='value')
        
        self.max_time_input.observe(self.on_time_settings_change, names='value')
        self.time_step_input.observe(self.on_time_settings_change, names='value')

    def on_value_change(self, change):
        self.update_plot(change.new)

    def on_parameter_change(self, change):
        self.alpha = complex(self.alpha_real.value, self.alpha_imag.value)
        self.beta = complex(self.beta_real.value, self.beta_imag.value)
        self.max_radius = self.max_radius_input.value
        self.update_plot(self.slider.value)

    def on_time_settings_change(self, change):
        self.max_time = self.max_time_input.value
        self.time_step = self.time_step_input.value
        self.slider.max = self.max_time
        self.slider.step = self.time_step
        self.play_button.max = int(self.max_time / self.time_step)

    def display(self):
        controls = widgets.VBox([
            widgets.HBox([self.play_button, self.slider]),
            widgets.HBox([self.alpha_real, self.alpha_imag]),
            widgets.HBox([self.beta_real, self.beta_imag]),
            widgets.HBox([self.max_radius_input, self.max_time_input, self.time_step_input])
        ])
        display(HTML("<h3>Explore the Improved Morphing Infinity Spiral</h3>"))
        display(widgets.VBox([self.fig, controls]))
        display(HTML("""
        <h4>Visualization Guide:</h4>
        <ul>
            <li><strong>Top Left:</strong> MIS in Complex Plane - Shows the spiral in the complex plane, color representing phase</li>
            <li><strong>Top Right:</strong> Magnitude Heat Map - Displays the magnitude of the MIS function</li>
            <li><strong>Bottom Left:</strong> Phase Heat Map - Shows the phase of the MIS function</li>
            <li><strong>Bottom Right:</strong> Polar Plot - Represents the MIS in polar coordinates</li>
        </ul>
        <p>Adjust α and β to explore different MIS behaviors. The time slider and play button control the temporal evolution.</p>
        <p>You can set the maximum radius, maximum time, and time step for more detailed or longer animations!</p>
        """))

# Create and display the visualization
mis = ImprovedMorphingInfinitySpiral(max_time=100, time_step=0.1)
mis.display()
