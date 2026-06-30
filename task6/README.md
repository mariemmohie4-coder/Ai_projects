# Vehicle Fuel Efficiency Prediction (MPG)

A systematic machine learning project evaluating Ordinary Least Squares (OLS) Linear Regression against higher-order Polynomial models, combined with Ridge and Lasso regularization.

## Key Project Steps
1. **Data Preprocessing:** Standardized numerical features using Z-score scaling.
2. **Baseline vs. Polynomial Expansion:** Evaluated linear trends against higher degrees ($d=2$ to $d=5$) to isolate non-linear boundaries.
3. **Regularization:** Deployed Ridge ($L_2$) and Lasso ($L_1$) to control multicollinearity and prevent catastrophic overfitting.

## Core Performance Summary
* **Best Model:** Polynomial Degree 2 + Ridge Regularization ($\alpha = 0.01$)
* **Top Metric Performance:** $R^2 = 0.8599$ | $RMSE = 2.6737$ | $MAPE = 8.91\%$
* **Insight:** Going beyond Degree 2 triggers an immediate overfitting cliff due to pure noise absorption.

## Technical Stack
* Python 3
* Scikit-Learn (Regression & Regularization frameworks)
* NumPy & Pandas (Data manipulation)
* Matplotlib & Seaborn (Data visualization and residual plots)
