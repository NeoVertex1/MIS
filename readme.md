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

$$S_{\alpha, \beta}(z, t) = z^{\alpha} \cdot \exp(i \cdot t \cdot (\log(z))^{\beta})$$

Where:

- $$ z \in \mathbb{C} $$ (z is a complex number)
- $$ t \in \mathbb{R} $$ (t is a real number representing time)
- $$ \alpha, \beta \in \mathbb{C} $$ (α and β are complex parameters)
- $$ i $$ is the imaginary unit ($$ i^2 = -1 $$)
- $$ \exp(x) $$ is the exponential function
- $$ \log(z) $$ is the complex natural logarithm

## Domain and Range

- **Domain:** $$ \mathbb{C} \setminus \{0\} \times \mathbb{R} $$ (all non-zero complex numbers and all real numbers)
- **Range:** $$ \mathbb{C} $$ (the complex plane)

## Component Analysis
a) $$ z^{\alpha} $$:
This term stretches and rotates $$ z $$ based on $$ \alpha $$.  
If $$ \alpha = a + bi $$, then $$ |z^{\alpha}| = |z|^{a} $$ and $$ \arg(z^{\alpha}) = \alpha \cdot \arg(z) $$.

b) $$ (\log(z))^{\beta} $$:
$$\log(z) = \ln|z| + i \cdot \arg(z)$$
This term introduces scale-invariance and additional rotation.

c) $$ \exp(i \cdot t \cdot (\log(z))^{\beta}) $$:
This creates the time-dependent rotation.  
As $$ t $$ varies, it causes the spiral to morph.

## Key Properties
a) **Scale Invariance:**  
For any non-zero complex number $$ k $$,
$$S_{\alpha, \beta}(kz, t) = k^{\alpha} \cdot S_{\alpha, \beta}(z, t)$$

b) **Rotational Symmetry:**  
For any real number $$ \theta $$,
$$S_{\alpha, \beta}(e^{i\theta}z, t) = e^{i\alpha\theta} \cdot S_{\alpha, \beta}(z, t)$$

c) **Time Evolution:**
$$\frac{\partial S_{\alpha, \beta}}{\partial t} = i \cdot S_{\alpha, \beta} \cdot (\log(z))^{\beta}$$

d) **Complex Derivative:**
$$\frac{\partial S_{\alpha, \beta}}{\partial z} = S_{\alpha, \beta} \cdot \left(\frac{\alpha}{z} + i\beta t \cdot \frac{(\log(z))^{\beta-1}}{z}\right)$$

## Dynamical System
The MIS can be viewed as a dynamical system by iterating the function:
$$z_{n+1} = S_{\alpha, \beta}(z_n, t)$$

This leads to the study of:
- **Fixed points:** $$ z^* $$ such that $$ S_{\alpha, \beta}(z^*, t) = z^* $$
- **Periodic orbits:** sequences $$ \{z_0, z_1, \ldots, z_n\} $$ such that $$ S_{\alpha, \beta}(z_n, t) = z_0 $$
- **Attractors and repellers:** sets of points that nearby orbits converge to or diverge from

## Lyapunov Exponent
To quantify the sensitivity to initial conditions:
$$\lambda(z_0) = \lim_{n \to \infty} \left(\frac{1}{n} \sum_{k=0}^{n-1} \log\left|\frac{\partial S_{\alpha, \beta}}{\partial z}(z_k, t)\right|\right)$$
Where $$ z_k $$ is the $$ k $$-th iterate of $$ z_0 $$ under $$ S_{\alpha, \beta} $$.

## Fractal Dimension
For sets invariant under $$ S_{\alpha, \beta} $$, we can define and study various fractal dimensions, such as the Hausdorff dimension or box-counting dimension.

## Conformal Properties
$$ S_{\alpha, \beta} $$ is conformal (angle-preserving) at points where its derivative is non-zero. The points where $$ \frac{\partial S_{\alpha, \beta}}{\partial z} = 0 $$ are critical points of the mapping.

## Fourier Analysis
We can study the frequency components of $$ S_{\alpha, \beta} $$ along circular paths:
$$F(r, \omega, t) = \frac{1}{2\pi} \int_{0}^{2\pi} S_{\alpha, \beta}(re^{i\theta}, t) \cdot e^{-i\omega\theta} d\theta$$
This gives insight into the spiral's structure at different scales.

## Partial Differential Equation
$$ S_{\alpha, \beta} $$ satisfies the following PDE:
$$\frac{\partial S}{\partial t} + z \cdot \frac{\partial S}{\partial z} = \alpha \cdot S \cdot \log|S| + i \cdot \beta \cdot S \cdot (\log|z|)^{\beta}$$
This PDE encapsulates the spiral's morphing behavior and scale invariance.

## Analytic Continuation
While $$ S_{\alpha, \beta} $$ is initially defined for $$ z \neq 0 $$, it can potentially be analytically continued to a larger domain in the complex plane, depending on the values of $$ \alpha $$ and $$ \beta $$.

## Parameter Space Analysis
The behavior of $$ S_{\alpha, \beta} $$ can be classified based on the values of $$ \alpha $$ and $$ \beta $$. This leads to a parameter space study, potentially revealing regions of similar behavior or bifurcations.
