Hello and welcome to the toy mathematics project 👋!

The purpose of this project is to explore new cool mathematical objects! Yes you heard that right, it is possible to create completely new mathematical objects, while these objects build upon the foundationss of our science, the properties that they exhibit are not yet fully explored or solved. In this repo you will find interesting new mathematical objects.

Ideally, those who decide to explore this rabbit hole will be able to help each other research these new properties and interesting lil number thingies. It's unknown to me how much of an impact these math objects can make but I enjoy inventing and exploring them. If you are excited about mathematics and code, this will be a wild adventure for you. Most of the math posted here can be tested and "proved" with code! For each new math object we create we will provide extensive testing suits to play around with it. Now without further ado, lets delve... 🤖🤝🤓

Our first proposal and contribution:



# Morphing Infinity Spiral: Mathematical Analysis

## 1. Core Definition

The Morphing Infinity Spiral is defined by the complex function:

$$ S_{\alpha,\beta}(z, t) = z^{\alpha} \cdot \exp(i \cdot t \cdot (\log(z))^{\beta}) $$

## Core Definition

The Morphing Infinity Spiral is defined by the complex function:

`S_{α,β}(z, t) = z^α * exp(i * t * (log(z))^β)`

Where:
- `z ∈ ℂ` (z is a complex number)
- `t ∈ ℝ` (t is a real number representing time)
- `α, β ∈ ℂ` (α and β are complex parameters)
- `i` is the imaginary unit (`i² = -1`)
- `exp(x)` is the exponential function
- `log(z)` is the complex natural logarithm

## Domain and Range

- **Domain:** `ℂ \ {0} × ℝ` (all non-zero complex numbers and all real numbers)
- **Range:** `ℂ` (the complex plane)

## Component Analysis

1. `z^α`:
   - This term stretches and rotates z based on α
   - If `α = a + bi`, then `|z^α| = |z|^a` and `arg(z^α) = α * arg(z)`

2. `(log(z))^β`:
   - `log(z) = ln|z| + i*arg(z)`
   - This term introduces scale-invariance and additional rotation

3. `exp(i * t * (log(z))^β)`:
   - This creates the time-dependent rotation
   - As t varies, it causes the spiral to morph

## Key Properties

1. **Scale Invariance:**
   - For any non-zero complex number k,
   `S_{α,β}(kz, t) = k^α * S_{α,β}(z, t)`

2. **Rotational Symmetry:**
   - For any real number θ,
   `S_{α,β}(e^(iθ)z, t) = e^(iαθ) * S_{α,β}(z, t)`

3. **Time Evolution:**
   `∂S_{α,β}/∂t = i * S_{α,β} * (log(z))^β`

4. **Complex Derivative:**
   `∂S_{α,β}/∂z = S_{α,β} * (α/z + iβt(log(z))^(β-1)/z)`

## Dynamical System

The MIS can be viewed as a dynamical system by iterating the function:
`z_{n+1} = S_{α,β}(z_n, t)`

This leads to the study of:
- **Fixed points:** `z*` such that `S_{α,β}(z*, t) = z*`
- **Periodic orbits:** sequences `{z_0, z_1, ..., z_n}` such that `S_{α,β}(z_n, t) = z_0`
- **Attractors and repellers:** sets of points that nearby orbits converge to or diverge from

## Lyapunov Exponent

To quantify the sensitivity to initial conditions:
`λ(z_0) = lim(n→∞) (1/n) * Σ(k=0 to n-1) log(|∂S_{α,β}/∂z(z_k, t)|)`
Where `z_k` is the k-th iterate of `z_0` under `S_{α,β}`.

## Fractal Dimension

For sets invariant under `S_{α,β}`, we can define and study various fractal dimensions, such as the Hausdorff dimension or box-counting dimension.

## Conformal Properties

`S_{α,β}` is conformal (angle-preserving) at points where its derivative is non-zero. The points where `∂S_{α,β}/∂z = 0` are critical points of the mapping.

## Fourier Analysis

We can study the frequency components of `S_{α,β}` along circular paths:
`F(r, ω, t) = (1/2π) * ∫(0 to 2π) S_{α,β}(re^(iθ), t) * e^(-iωθ) dθ`
This gives insight into the spiral's structure at different scales.

## Partial Differential Equation

`S_{α,β}` satisfies the following PDE:
`∂S/∂t + z * (∂S/∂z) = α * S * log|S| + i * β * S * (log|z|)^β`
This PDE encapsulates the spiral's morphing behavior and scale invariance.

## Analytic Continuation

While `S_{α,β}` is initially defined for `z ≠ 0`, it can potentially be analytically continued to a larger domain in the complex plane, depending on the values of `α` and `β`.

## Parameter Space Analysis

The behavior of `S_{α,β}` can be classified based on the values of `α` and `β`. This leads to a parameter space study, potentially revealing regions of similar behavior or bifurcations.
