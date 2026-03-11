# QF214800 Linear Algebra
Offered by [Department of Quantitative Finance](https://qf.site.nthu.edu.tw/)

**Grade:** B+ (Fall 2025)

**Textbook:** [Linear Algebra and Its Applications](https://rksmvv.ac.in/wp-content/uploads/2021/04/Gilbert_Strang_Linear_Algebra_and_Its_Applicatio_230928_225121.pdf)

## About
I studied and duplicated the results in [Valuing American Options by Simulation: A Simple Least-Squares Approach](https://people.math.ethz.ch/~hjfurrer/teaching/LongstaffSchwartzAmericanOptionsLeastSquareMonteCarlo.pdf) for my final project in Linear Algebra.  
This project implements the Least-Squares Monte Carlo (LSM) algorithm for American option pricing, modeling the valuation as an orthogonal projection of future cash flows onto a finite-dimensional subspace. I successfully validated the algorithm by replicating the benchmark results from Longstaff and Schwartz (2001) using a vector-based Python implementation. A core focus of the research is the numerical stability analysis, specifically investigating how the Condition Number of the design matrix evolves with increasing polynomial degrees. The empirical findings reveal a critical trade-off where higher-degree polynomials, while theoretically more accurate, amplify simulation noise due to matrix ill-conditioning. Ultimately, the study concludes that a cubic basis ($K=3$) provides the optimal balance between pricing precision and robust numerical stability for this model.
