
Apparently while MIS has scale invariance at some level, it can break down very easily, here is some information about it:

Mathematical Breakdown:

The Morphing Infinity Spiral (MIS) is defined as:
S_α,β(z, t) = z^α · exp(i · t · (log(z))^β)

Scale invariance property states that:
S_α,β(k·z, t) = k^α · S_α,β(z, t)

Where:
- z is a complex number
- t is time
- k is a scaling factor
- α and β are complex parameters

In our tests, we're comparing the left side (S_α,β(k·z, t)) with the right side (k^α · S_α,β(z, t)) of this equation.

Simple Explanation of Results:

1. Time t = 0:
   - For all test points (z) and all scaling factors (k), the scale invariance property holds perfectly.
   - The relative errors are extremely small (around 10^-16), which is essentially zero in computer arithmetic.

2. Time t ≠ 0 (t = 1 or t = 10):
   - For all test points (z) and all scaling factors (k), the scale invariance property fails.
   - The relative errors are large, ranging from about 0.6 to 1.8, indicating significant discrepancies.

3. Consistency in Errors:
   - For t ≠ 0, the pattern of errors is remarkably consistent across all test points.
   - The errors for k = 0.1 and k = 10 are always around 1.8.
   - The errors for k = 0.5 and k = 2 are always around 0.68.
   - The errors for k = 100 are always around 1.5.

4. Independence from z:
   - The results are identical for all values of z tested (from 0.01+0.01j to 1000+1000j).
   - This suggests that the scale invariance property (or its failure) is independent of the magnitude of z.

In simple terms:
- When time is zero, the Morphing Infinity Spiral behaves perfectly with respect to scaling. If you zoom in or out, the spiral looks the same, just bigger or smaller.
- However, as soon as time is not zero, this scaling property breaks down. The spiral no longer looks the same when you zoom in or out.
- This breakdown happens in a very consistent way, regardless of where you look in the complex plane (the value of z).
- The amount of breakdown depends on how much you're scaling (the value of k), but not on where you're looking (the value of z).

This suggests that the time component of the MIS function is what's causing the scale invariance to break down. The exp(i · t · (log(z))^β) term is likely the culprit, as it doesn't scale in the same way as z^α does.



# DATA DUMP:

Comprehensive Test for Morphing Infinity Spiral with α=(0.5 + 0.5j), β=(1.0 + 0.0j)

Testing mis function:
mis((1+1j), 0) = (0.677772505240435 + 0.430602270116838j)
mis((1+1j), 1) = (0.223960381727822 + 0.289622559260971j)
mis((1+1j), 10) = (-0.000196171251697472 - 0.000242256872381788j)
mis((2+3j), 0) = (0.492859671882141 + 1.05191138174796j)
mis((2+3j), 1) = (-0.324992032087957 + 0.288789568957069j)
mis((2+3j), 10) = (1.12013301617393e-5 + 6.16309689119526e-5j)
mis((0.5-0.5j), 0) = (1.05114598971042 - 0.66781382527896j)
mis((0.5-0.5j), 1) = (1.67085386113619 - 2.1607257840873j)
mis((0.5-0.5j), 10) = (-2018.81360581775 + 2493.08431197368j)
mis((10+10j), 0) = (-0.370630179351416 + 2.51208521134348j)
mis((10+10j), 1) = (-0.392585545824467 - 1.08916086202873j)
mis((10+10j), 10) = (-0.000983644528979775 + 6.44900201251616e-5j)
mis((100+100j), 0) = (-7.73248233583316 + 2.16520329645855j)
mis((100+100j), 1) = (0.123235914777321 + 3.65906557073847j)
mis((100+100j), 10) = (-0.00162862129554603 + 0.00265795934817857j)

Testing scale invariance:
z=(0.01+0.01j), t=0, k=0.1: Passed, Relative Error: 5.21e-16
z=(0.01+0.01j), t=0, k=0.5: Passed, Relative Error: 6.38e-16
z=(0.01+0.01j), t=0, k=2: Passed, Relative Error: 3.06e-16
z=(0.01+0.01j), t=0, k=10: Passed, Relative Error: 3.28e-16
z=(0.01+0.01j), t=0, k=100: Passed, Relative Error: 3.72e-16
z=(0.01+0.01j), t=1, k=0.1: Failed, Relative Error: 1.83e+00
z=(0.01+0.01j), t=1, k=0.5: Failed, Relative Error: 6.79e-01
z=(0.01+0.01j), t=1, k=2: Failed, Relative Error: 6.79e-01
z=(0.01+0.01j), t=1, k=10: Failed, Relative Error: 1.83e+00
z=(0.01+0.01j), t=1, k=100: Failed, Relative Error: 1.49e+00
z=(0.01+0.01j), t=10, k=0.1: Failed, Relative Error: 1.74e+00
z=(0.01+0.01j), t=10, k=0.5: Failed, Relative Error: 6.37e-01
z=(0.01+0.01j), t=10, k=2: Failed, Relative Error: 6.37e-01
z=(0.01+0.01j), t=10, k=10: Failed, Relative Error: 1.74e+00
z=(0.01+0.01j), t=10, k=100: Failed, Relative Error: 1.72e+00
z=(1+1j), t=0, k=0.1: Passed, Relative Error: 1.55e-16
z=(1+1j), t=0, k=0.5: Passed, Relative Error: 2.02e-16
z=(1+1j), t=0, k=2: Passed, Relative Error: 9.78e-17
z=(1+1j), t=0, k=10: Passed, Relative Error: 1.09e-16
z=(1+1j), t=0, k=100: Passed, Relative Error: 2.77e-16
z=(1+1j), t=1, k=0.1: Failed, Relative Error: 1.83e+00
z=(1+1j), t=1, k=0.5: Failed, Relative Error: 6.79e-01
z=(1+1j), t=1, k=2: Failed, Relative Error: 6.79e-01
z=(1+1j), t=1, k=10: Failed, Relative Error: 1.83e+00
z=(1+1j), t=1, k=100: Failed, Relative Error: 1.49e+00
z=(1+1j), t=10, k=0.1: Failed, Relative Error: 1.74e+00
z=(1+1j), t=10, k=0.5: Failed, Relative Error: 6.37e-01
z=(1+1j), t=10, k=2: Failed, Relative Error: 6.37e-01
z=(1+1j), t=10, k=10: Failed, Relative Error: 1.74e+00
z=(1+1j), t=10, k=100: Failed, Relative Error: 1.72e+00
z=(10+10j), t=0, k=0.1: Passed, Relative Error: 1.38e-16
z=(10+10j), t=0, k=0.5: Passed, Relative Error: 2.23e-16
z=(10+10j), t=0, k=2: Passed, Relative Error: 2.23e-16
z=(10+10j), t=0, k=10: Passed, Relative Error: 1.11e-16
z=(10+10j), t=0, k=100: Passed, Relative Error: 1.40e-16
z=(10+10j), t=1, k=0.1: Failed, Relative Error: 1.83e+00
z=(10+10j), t=1, k=0.5: Failed, Relative Error: 6.79e-01
z=(10+10j), t=1, k=2: Failed, Relative Error: 6.79e-01
z=(10+10j), t=1, k=10: Failed, Relative Error: 1.83e+00
z=(10+10j), t=1, k=100: Failed, Relative Error: 1.49e+00
z=(10+10j), t=10, k=0.1: Failed, Relative Error: 1.74e+00
z=(10+10j), t=10, k=0.5: Failed, Relative Error: 6.37e-01
z=(10+10j), t=10, k=2: Failed, Relative Error: 6.37e-01
z=(10+10j), t=10, k=10: Failed, Relative Error: 1.74e+00
z=(10+10j), t=10, k=100: Failed, Relative Error: 1.72e+00
z=(100+100j), t=0, k=0.1: Passed, Relative Error: 1.31e-16
z=(100+100j), t=0, k=0.5: Passed, Relative Error: 4.95e-16
z=(100+100j), t=0, k=2: Passed, Relative Error: 1.67e-16
z=(100+100j), t=0, k=10: Passed, Relative Error: 3.13e-16
z=(100+100j), t=0, k=100: Passed, Relative Error: 7.30e-16
z=(100+100j), t=1, k=0.1: Failed, Relative Error: 1.83e+00
z=(100+100j), t=1, k=0.5: Failed, Relative Error: 6.79e-01
z=(100+100j), t=1, k=2: Failed, Relative Error: 6.79e-01
z=(100+100j), t=1, k=10: Failed, Relative Error: 1.83e+00
z=(100+100j), t=1, k=100: Failed, Relative Error: 1.49e+00
z=(100+100j), t=10, k=0.1: Failed, Relative Error: 1.74e+00
z=(100+100j), t=10, k=0.5: Failed, Relative Error: 6.37e-01
z=(100+100j), t=10, k=2: Failed, Relative Error: 6.37e-01
z=(100+100j), t=10, k=10: Failed, Relative Error: 1.74e+00
z=(100+100j), t=10, k=100: Failed, Relative Error: 1.72e+00
z=(1000+1000j), t=0, k=0.1: Passed, Relative Error: 2.21e-16
z=(1000+1000j), t=0, k=0.5: Passed, Relative Error: 1.40e-16
z=(1000+1000j), t=0, k=2: Passed, Relative Error: 2.21e-16
z=(1000+1000j), t=0, k=10: Passed, Relative Error: 7.08e-16
z=(1000+1000j), t=0, k=100: Passed, Relative Error: 8.13e-16
z=(1000+1000j), t=1, k=0.1: Failed, Relative Error: 1.83e+00
z=(1000+1000j), t=1, k=0.5: Failed, Relative Error: 6.79e-01
z=(1000+1000j), t=1, k=2: Failed, Relative Error: 6.79e-01
z=(1000+1000j), t=1, k=10: Failed, Relative Error: 1.83e+00
z=(1000+1000j), t=1, k=100: Failed, Relative Error: 1.49e+00
z=(1000+1000j), t=10, k=0.1: Failed, Relative Error: 1.74e+00
z=(1000+1000j), t=10, k=0.5: Failed, Relative Error: 6.37e-01
z=(1000+1000j), t=10, k=2: Failed, Relative Error: 6.37e-01
z=(1000+1000j), t=10, k=10: Failed, Relative Error: 1.74e+00
z=(1000+1000j), t=10, k=100: Failed, Relative Error: 1.72e+00

Testing rotational symmetry:
z=(0.01+0.01j), theta=0.785398163397448: False
z=(0.01+0.01j), theta=1.5707963267949: False
z=(0.01+0.01j), theta=3.14159265358979: False
z=(1+1j), theta=0.785398163397448: False
z=(1+1j), theta=1.5707963267949: False
z=(1+1j), theta=3.14159265358979: False
z=(10+10j), theta=0.785398163397448: False
z=(10+10j), theta=1.5707963267949: False
z=(10+10j), theta=3.14159265358979: False
z=(100+100j), theta=0.785398163397448: False
z=(100+100j), theta=1.5707963267949: False
z=(100+100j), theta=3.14159265358979: False
z=(1000+1000j), theta=0.785398163397448: False
z=(1000+1000j), theta=1.5707963267949: False
z=(1000+1000j), theta=3.14159265358979: False

Testing time evolution:
z=(0.01+0.01j), t=0: True
z=(0.01+0.01j), t=1: True
z=(0.01+0.01j), t=10: True
z=(1+1j), t=0: True
z=(1+1j), t=1: True
z=(1+1j), t=10: True
z=(10+10j), t=0: False
z=(10+10j), t=1: False
z=(10+10j), t=10: True
z=(100+100j), t=0: False
z=(100+100j), t=1: False
z=(100+100j), t=10: True
z=(1000+1000j), t=0: False
z=(1000+1000j), t=1: False
z=(1000+1000j), t=10: True

Testing complex derivative:
z=(0.01+0.01j), t=0: False
z=(0.01+0.01j), t=1: False
z=(0.01+0.01j), t=10: False
z=(1+1j), t=0: True
z=(1+1j), t=1: True
z=(1+1j), t=10: True
z=(10+10j), t=0: True
z=(10+10j), t=1: True
z=(10+10j), t=10: True
z=(100+100j), t=0: True
z=(100+100j), t=1: True
z=(100+100j), t=10: True
z=(1000+1000j), t=0: True
z=(1000+1000j), t=1: True
z=(1000+1000j), t=10: True




