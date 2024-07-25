Hello and welcome to the toy mathematics project 👋!

The purpose of this project is to explore new cool mathematical objects! Yes you heard that right, it is possible to create completely new mathematical objects, while these objects build upon the foundationss of our science, the properties that they exhibit are not yet fully explored or solved. In this repo you will find interesting new mathematical objects.

Ideally, those who decide to explore this rabbit hole will be able to help each other research these new properties and interesting lil number thingies. It's unknown to me how much of an impact these math objects can make but I enjoy inventing and exploring them. If you are excited about mathematics and code, this will be a wild adventure for you. Most of the math posted here can be tested and "proved" with code! For each new math object we create we will provide extensive testing suits to play around with it. Now without further ado, lets delve... 🤖🤝🤓

If you feel like solving a "problem" [here](https://github.com/toymathematician/toy-mathematics/blob/main/mis_time_breakdown.md) is the current problem im working on for this project.

Our first proposal and contribution:

# Morphing Infinity Spiral (MIS)

## A Novel Mathematical Object

The Morphing Infinity Spiral (MIS) is defined as:

$$ S_{\alpha,\beta}(z, t) = z^{\alpha} \cdot \exp(i \cdot t \cdot (\log(z))^{\beta}) $$

where z ∈ ℂ\{0}, t ∈ ℝ, α, β ∈ ℂ

Novelty:
1. Combines complex exponentiation, logarithms, and time-dependent rotation
2. Introduces time evolution into complex dynamics
3. Maintains scale invariance while evolving over time
4. Generalizes power functions and logarithmic spirals
5. Satisfies a new class of partial differential equations

Significance:
1. Bridges complex analysis, dynamical systems, and fractal geometry
2. Potential applications in physics, engineering, and data science
3. Opens new avenues in mathematical research
4. May require development of new numerical methods
5. Offers fresh perspectives on symmetry and invariance in mathematics

The MIS represents a new frontier in mathematical exploration, with implications spanning pure and applied mathematics.

# Morphing Infinity Spiral: Mathematical Analysis

## 1.Mathematical Definition

The Morphing Infinity Spiral is defined by the complex function:

$$ S_{\alpha,\beta}(z, t) = z^{\alpha} \cdot \exp(i \cdot t \cdot (\log(z))^{\beta}) $$

Where:
- $z \in \mathbb{C}$ (z is a complex number)
- $t \in \mathbb{R}$ (t is a real number representing time)
- $\alpha, \beta \in \mathbb{C}$ ($\alpha$ and $\beta$ are complex parameters)
- $i$ is the imaginary unit ($i^2 = -1$)
- $\exp(x)$ is the exponential function
- $\log(z)$ is the complex natural logarithm

## 2. Domain and Range

- Domain: $\mathbb{C} \setminus \{0\} \times \mathbb{R}$ (all non-zero complex numbers and all real numbers)
- Range: $\mathbb{C}$ (the complex plane)

## 3. Component Analysis

a) $z^{\alpha}$: This term stretches and rotates $z$ based on $\alpha$
   If $\alpha = a + bi$, then $|z^{\alpha}| = |z|^a$ and $\arg(z^{\alpha}) = \alpha \cdot \arg(z)$

b) $(\log(z))^{\beta}$: $\log(z) = \ln|z| + i\cdot\arg(z)$
   This term introduces scale-invariance and additional rotation

c) $\exp(i \cdot t \cdot (\log(z))^{\beta})$: This creates the time-dependent rotation
   As $t$ varies, it causes the spiral to morph

## 4. Key Properties

a) Scale Invariance: For any non-zero complex number $k$,
   $$S_{\alpha,\beta}(kz, t) = k^{\alpha} \cdot S_{\alpha,\beta}(z, t)$$

b) Rotational Symmetry: For any real number $\theta$,
   $$S_{\alpha,\beta}(e^{i\theta}z, t) = e^{i\alpha\theta} \cdot S_{\alpha,\beta}(z, t)$$

c) Time Evolution:
   $$\frac{\partial S_{\alpha,\beta}}{\partial t} = i \cdot S_{\alpha,\beta} \cdot (\log(z))^{\beta}$$

d) Complex Derivative:
   $$\frac{\partial S_{\alpha,\beta}}{\partial z} = S_{\alpha,\beta} \cdot \left(\frac{\alpha}{z} + \frac{i\beta t(\log(z))^{\beta-1}}{z}\right)$$

## 5. Dynamical System

The MIS can be viewed as a dynamical system by iterating the function:

$$z_{n+1} = S_{\alpha,\beta}(z_n, t)$$

This leads to the study of:
a) Fixed points: $z^*$ such that $S_{\alpha,\beta}(z^*, t) = z^*$
b) Periodic orbits: sequences $\{z_0, z_1, ..., z_n\}$ such that $S_{\alpha,\beta}(z_n, t) = z_0$
c) Attractors and repellers: sets of points that nearby orbits converge to or diverge from

## 6. Lyapunov Exponent

To quantify the sensitivity to initial conditions:

$$\lambda(z_0) = \lim_{n\to\infty} \frac{1}{n} \sum_{k=0}^{n-1} \log\left|\frac{\partial S_{\alpha,\beta}}{\partial z}(z_k, t)\right|$$

Where $z_k$ is the $k$-th iterate of $z_0$ under $S_{\alpha,\beta}$.

## 7. Fractal Dimension

For sets invariant under $S_{\alpha,\beta}$, we can define and study various fractal dimensions, such as the Hausdorff dimension or box-counting dimension.

## 8. Conformal Properties

$S_{\alpha,\beta}$ is conformal (angle-preserving) at points where its derivative is non-zero. The points where $\frac{\partial S_{\alpha,\beta}}{\partial z} = 0$ are critical points of the mapping.

## 9. Fourier Analysis

We can study the frequency components of $S_{\alpha,\beta}$ along circular paths:

$$F(r, \omega, t) = \frac{1}{2\pi} \int_0^{2\pi} S_{\alpha,\beta}(re^{i\theta}, t) \cdot e^{-i\omega\theta} \, d\theta$$

This gives insight into the spiral's structure at different scales.

## 10. Partial Differential Equation

$S_{\alpha,\beta}$ satisfies the following PDE:

$$\frac{\partial S}{\partial t} + z \cdot \frac{\partial S}{\partial z} = \alpha \cdot S \cdot \log|S| + i \cdot \beta \cdot S \cdot (\log|z|)^{\beta}$$

This PDE encapsulates the spiral's morphing behavior and scale invariance.

## 11. Analytic Continuation

While $S_{\alpha,\beta}$ is initially defined for $z \neq 0$, it can potentially be analytically continued to a larger domain in the complex plane, depending on the values of $\alpha$ and $\beta$.

## 12. Parameter Space Analysis

The behavior of $S_{\alpha,\beta}$ can be classified based on the values of $\alpha$ and $\beta$. This leads to a parameter space study, potentially revealing regions of similar behavior or bifurcations.



# Morphing Infinity Spiral: Comprehensive Analysis

## 1. Novelty

The Morphing Infinity Spiral (MIS) is novel due to:

1. Combination of elements:
   - Complex exponentiation
   - Complex logarithm
   - Time-dependent rotation
   - Nested exponentiation

2. Time-dependent complex dynamics:
   - Bridges static complex functions and time-evolving systems

3. Scale invariance with time evolution:
   - Maintains scale invariance while changing over time

4. Generalization of existing objects:
   - Encompasses power functions and logarithmic spirals

5. New partial differential equation:
   - Combines transport and nonlinear growth terms

## 2. Mathematical Definition and Properties

Definition:
$$S_{\alpha,\beta}(z, t) = z^{\alpha} \cdot \exp(i \cdot t \cdot (\log(z))^{\beta})$$
Where $z \in \mathbb{C} \setminus \{0\}$, $t \in \mathbb{R}$, $\alpha, \beta \in \mathbb{C}$

Properties:

1. Scale invariance:
   $$S_{\alpha,\beta}(kz, t) = k^{\alpha} \cdot S_{\alpha,\beta}(z, t)$$

2. Rotational symmetry:
   $$S_{\alpha,\beta}(e^{i\theta}z, t) = e^{i\alpha\theta} \cdot S_{\alpha,\beta}(z, t)$$

3. Time evolution:
   $$\frac{\partial S_{\alpha,\beta}}{\partial t} = i \cdot S_{\alpha,\beta} \cdot (\log(z))^{\beta}$$

4. Complex derivative:
   $$\frac{\partial S_{\alpha,\beta}}{\partial z} = S_{\alpha,\beta} \cdot \left(\frac{\alpha}{z} + \frac{i\beta t(\log(z))^{\beta-1}}{z}\right)$$

5. Partial differential equation:
   $$\frac{\partial S}{\partial t} + z \cdot \frac{\partial S}{\partial z} = \alpha \cdot S \cdot \log|S| + i \cdot \beta \cdot S \cdot (\log|z|)^{\beta}$$

## 3. Mathematical Analysis

1. Complex analysis:
   - Analytic continuation beyond $\mathbb{C} \setminus \{0\}$
   - Singularities and branch points
   - Riemann surface structure

2. Dynamical systems:
   - Fixed points: $S_{\alpha,\beta}(z^*, t) = z^*$
   - Periodic orbits
   - Strange attractors
   - Lyapunov exponents

3. Fractal geometry:
   - Hausdorff dimension of MIS-generated sets
   - Box-counting dimension
   - Multifractal analysis

4. Fourier analysis:
   $$F(r, \omega, t) = \frac{1}{2\pi} \int_0^{2\pi} S_{\alpha,\beta}(re^{i\theta}, t) \cdot e^{-i\omega\theta} \, d\theta$$

5. Conformal mapping:
   - Angle preservation properties
   - Critical points where $\frac{\partial S_{\alpha,\beta}}{\partial z} = 0$

6. Group theory:
   - Symmetry groups of MIS for different $\alpha$, $\beta$

7. Number theory:
   - Behavior for rational/irrational $\alpha$, $\beta$
   - Connections to algebraic number fields

## 4. Computational Aspects

1. Numerical methods:
   - Efficient computation of MIS
   - Error analysis and stability

2. Visualization techniques:
   - 2D and 3D representations
   - Time-evolving animations

3. Parallel computing:
   - GPU acceleration for MIS computation

4. Machine learning:
   - Pattern recognition in MIS-generated sets
   - Parameter estimation from observed patterns

## 5. Potential Applications

1. Physics:
   - Fluid dynamics: vortex modeling
   - Plasma physics: magnetic field configurations
   - Astrophysics: spiral galaxy formation

2. Engineering:
   - Antenna design: fractal antennas
   - Signal processing: time-frequency analysis

3. Biology:
   - Morphogenesis: modeling growth patterns
   - Neuroscience: spiral wave patterns in neural activity

4. Finance:
   - Time series analysis
   - Risk assessment models

5. Computer graphics:
   - Procedural texture generation
   - Organic shape modeling

## 6. Research Directions

1. Parameter space analysis:
   - Classification of MIS behavior for different $\alpha$, $\beta$
   - Bifurcation diagrams

2. Ergodic theory:
   - Invariant measures for MIS-generated dynamical systems

3. Algebraic geometry:
   - Algebraic properties of MIS for special $\alpha$, $\beta$ values

4. Differential geometry:
   - Curvature properties of MIS-generated surfaces

5. Operator theory:
   - MIS as an operator on function spaces

6. Quantum mechanics:
   - Quantum analogues of MIS

7. Information theory:
   - Entropy of MIS-generated sequences

8. Category theory:
   - MIS in the context of categorical dynamics

## 7. Interdisciplinary Connections

1. Complex systems science:
   - Self-organization in MIS dynamics

2. Cognitive science:
   - Visual perception of MIS-generated patterns

3. Art and design:
   - MIS-inspired artistic creations

4. Philosophy of mathematics:
   - Implications of MIS for mathematical realism/nominalism

5. Data science:
   - MIS-based feature extraction methods

## 8. Open Problems

1. Closed-form solutions for fixed points and periodic orbits
2. Rigorous bounds on fractal dimensions of MIS-generated sets
3. Existence and uniqueness of solutions to MIS-related PDEs
4. Classification of MIS behavior for transcendental $\alpha$, $\beta$
5. Connections between MIS and zeta function theory

## 9. Historical Context and Future Outlook

1. Relation to classical spiral studies (Archimedes, Galileo)
2. Comparison with other complex dynamical systems (Mandelbrot set, Julia sets)
3. Potential impact on future mathematical research
4. Possibilities for generalizing MIS further

