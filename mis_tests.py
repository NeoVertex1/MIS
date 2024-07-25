# these a comprehensive tests, the are "proof" of all mis known properties, have in mind the invariance breaks down with time very quickly we need to learn about it further

import mpmath as mp
from scipy import stats
import numpy as np

# Set mpmath precision
mp.dps = 50  # 50 decimal places of precision

class ImprovedMorphingInfinitySpiral:
    def __init__(self, alpha=0.5+0.5j, beta=1+0j, num_points=10000, max_radius=5):
        self.alpha = mp.mpc(alpha)
        self.beta = mp.mpc(beta)
        self.num_points = num_points
        self.max_radius = mp.mpf(max_radius)

    def mis(self, z, t):
        z = mp.mpc(z)
        t = mp.mpf(t)
        if abs(z) < 1e-50:
            return mp.mpc(0)
        log_z = mp.log(z)
        power = mp.exp(self.alpha * log_z)
        exp_term = mp.exp(1j * t * mp.exp(self.beta * mp.log(log_z)))
        return power * exp_term

    def create_spiral_points(self, t):
        r = mp.logspace(mp.log10(mp.mpf('1e-3')), mp.log10(self.max_radius), self.num_points)
        theta = mp.linspace(0, 20*mp.pi, self.num_points)
        z = [r[i] * mp.exp(1j * theta[i]) for i in range(self.num_points)]
        w = [self.mis(zi, t) for zi in z]
        return [wi.real for wi in w], [wi.imag for wi in w]

    def test_scale_invariance(self, z, t, k):
        z, t, k = mp.mpc(z), mp.mpf(t), mp.mpc(k)
        left = self.mis(k*z, t)
        right = k**self.alpha * self.mis(z, t)
        relative_error = abs((left - right) / right)
        is_invariant = relative_error < 1e-6  # Adjusted tolerance
        return is_invariant, float(relative_error)



    def test_rotational_symmetry(self, z, t, theta):
        z, t, theta = mp.mpc(z), mp.mpf(t), mp.mpf(theta)
        left = self.mis(z * mp.exp(1j*theta), t)
        right = mp.exp(1j*self.alpha*theta) * self.mis(z, t)
        return mp.almosteq(left, right, 1e-10)

    def test_time_evolution(self, z, t, dt=1e-6):
        z, t, dt = mp.mpc(z), mp.mpf(t), mp.mpf(dt)
        numerical_derivative = (self.mis(z, t + dt) - self.mis(z, t)) / dt
        analytical_derivative = 1j * self.mis(z, t) * mp.exp(self.beta * mp.log(mp.log(z)))
        return mp.almosteq(numerical_derivative, analytical_derivative, 1e-6)

    def test_complex_derivative(self, z, t, dz=1e-6):
        z, t, dz = mp.mpc(z), mp.mpf(t), mp.mpf(dz)
        numerical_derivative = (self.mis(z + dz, t) - self.mis(z, t)) / dz
        analytical_derivative = self.mis(z, t) * (self.alpha/z + 1j*self.beta*t*mp.exp((self.beta-1) * mp.log(mp.log(z)))/z)
        return mp.almosteq(numerical_derivative, analytical_derivative, 1e-6)

    def find_fixed_points(self, t, num_initial=10000, max_iter=1000):
        t = mp.mpf(t)
        z = [self.max_radius * mp.mpc(mp.rand(), mp.rand()) for _ in range(num_initial)]
        for _ in range(max_iter):
            z_new = [self.mis(zi, t) for zi in z]
            fixed = [i for i, (zi, zi_new) in enumerate(zip(z, z_new)) if mp.almosteq(zi, zi_new, 1e-6)]
            if fixed:
                return [z[i] for i in fixed]
            z = z_new
        return []

    def detect_periodic_orbits(self, t, max_period=100, num_initial=10000):
        t = mp.mpf(t)
        z = [self.max_radius * mp.mpc(mp.rand(), mp.rand()) for _ in range(num_initial)]
        orbits = [z]
        for _ in range(max_period):
            z = [self.mis(zi, t) for zi in z]
            orbits.append(z)
            for i in range(len(orbits) - 1):
                periodic = [j for j, (zj, zj_old) in enumerate(zip(z, orbits[i])) if mp.almosteq(zj, zj_old, 1e-6)]
                if periodic:
                    return [orb[periodic[0]] for orb in orbits[i:]], [i for i in range(len(orbits) - i)]
        return None, None

    def compute_lyapunov_exponent(self, z0, t, n_iter=1000):
        z0, t = mp.mpc(z0), mp.mpf(t)
        z = z0
        lyap = 0
        for _ in range(n_iter):
            z_new = self.mis(z, t)
            df = abs(self.alpha/z + 1j*self.beta*t*mp.exp((self.beta-1) * mp.log(mp.log(z)))/z)
            lyap += mp.log(df)
            z = z_new
        return lyap / n_iter

    def estimate_fractal_dimension(self, t, num_points=10000):
        x, y = self.create_spiral_points(t)
        points = np.array([(float(xi), float(yi)) for xi, yi in zip(x, y)])
        distances = mp.matrix(pdist(points))
        
        rs = mp.logspace(mp.log10(mp.mpf('1e-3')), mp.log10(mp.mpf('1')), 20)
        cors = [mp.sum(distances < r) for r in rs]
        cors = [c / (num_points * (num_points - 1)) for c in cors]
        
        slope, _, _, _, _ = stats.linregress([float(mp.log10(r)) for r in rs], [float(mp.log10(c)) for c in cors])
        return slope

    def perform_fourier_analysis(self, r, t, num_points=1000):
        r, t = mp.mpf(r), mp.mpf(t)
        theta = mp.linspace(0, 2*mp.pi, num_points)
        z = [r * mp.exp(1j * th) for th in theta]
        w = [self.mis(zi, t) for zi in z]
        return mp.fft(w)

    def comprehensive_test(self):
        print(f"Comprehensive Test for Morphing Infinity Spiral with α={self.alpha}, β={self.beta}")
        
        test_points = [1+1j, 2+3j, 0.5-0.5j, 10+10j, 100+100j]
        print("\nTesting mis function:")
        for z in test_points:
            for t in [0, 1, 10]:
                result = self.mis(z, t)
                print(f"mis({z}, {t}) = {result}")
        
        # Test scale invariance
        print("\nTesting scale invariance:")
        test_points = [0.01+0.01j, 1+1j, 10+10j, 100+100j, 1000+1000j]
        scales = [0.1, 0.5, 2, 10, 100]
        time_values = [0, 1, 10]

        for z in test_points:
            for t in time_values:
                for k in scales:
                    is_invariant, relative_error = self.test_scale_invariance(z, t, k)
                    print(f"z={z}, t={t}, k={k}: {'Passed' if is_invariant else 'Failed'}, Relative Error: {relative_error:.2e}")

        
        print("\nTesting rotational symmetry:")
        for z in test_points:
            for theta in [mp.pi/4, mp.pi/2, mp.pi]:
                result = self.test_rotational_symmetry(z, 1, theta)
                print(f"z={z}, theta={theta}: {result}")
        
        print("\nTesting time evolution:")
        for z in test_points:
            for t in [0, 1, 10]:
                result = self.test_time_evolution(z, t)
                print(f"z={z}, t={t}: {result}")
        
        print("\nTesting complex derivative:")
        for z in test_points:
            for t in [0, 1, 10]:
                result = self.test_complex_derivative(z, t)
                print(f"z={z}, t={t}: {result}")
        
        print("\nFinding fixed points:")
        fixed_points = self.find_fixed_points(1)
        print(f"Fixed points: {fixed_points}")
        
        print("\nDetecting periodic orbits:")
        orbits, periods = self.detect_periodic_orbits(1)
        print(f"Periodic orbits: {orbits is not None}")
        if orbits is not None:
            print(f"Orbit periods: {periods}")
        
        print("\nComputing Lyapunov exponent:")
        for z in test_points:
            lyap = self.compute_lyapunov_exponent(z, 1)
            print(f"z={z}: Lyapunov exponent = {lyap}")
        
        print("\nEstimating fractal dimension:")
        fractal_dim = self.estimate_fractal_dimension(1)
        print(f"Estimated fractal dimension: {fractal_dim}")
        
        print("\nPerforming Fourier analysis:")
        fourier = self.perform_fourier_analysis(2, 1)
        print(f"First 5 Fourier coefficients: {fourier[:5]}")

if __name__ == "__main__":
    mis = ImprovedMorphingInfinitySpiral(alpha=0.5+0.5j, beta=1+0j)
    mis.comprehensive_test()
