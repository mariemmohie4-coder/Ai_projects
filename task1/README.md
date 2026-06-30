# Student Performance Analysis and Linear Regression Baseline

This repository contains the implementation of Task 1, which is divided into two core analytical components using pure NumPy: multidimensional array manipulation for educational data and a from-scratch parameter estimation for a Linear Regression model.

## Section 1: Multidimensional Array Analysis (Student Grades)
This component evaluates statistical operations on a matrix representing the grades of 5 students across 4 subjects.

### Implemented Operations
* **Matrix Transformation:** Converted raw data into a 2D NumPy array and verified its structural dimensions (`shape`).
* **Statistical Reduction:** Computed the mathematical mean targeted along specific dimensions—per student (`axis=1`) and per subject (`axis=0`).
* **Boolean Indexing:** Leveraged logical masking to filter and extract full grade profiles of students maintaining a cumulative average strictly above 85.
* **Broadcasting Operations:** Applied a uniform scalar operation to simulate adding bonus marks across the entire matrix structure.
* **Row-wise Min-Max Normalization:** Standardized values to a scale between 0 and 1. This was accomplished by reshaping the maximum and minimum vectors to maintain compatibility during matrix broadcasting.
* **Dimensionality Reduction:** Flattened the final matrix into a single continuous 1D vector.

---

## Section 2: Linear Regression from Scratch (Normal Equation)
This component builds a basic predictive model to forecast house prices based on size ($m^2$) without utilizing high-level machine learning libraries.

### Mathematical Pipeline
1. **Vector Reshaping:** Transformed the independent variable vector $X$ into a structural column vector.
2. **Bias Inclusion:** Horizontally stacked a column vector of ones ($\mathbf{1}$) to represent the intercept parameter ($\theta_0$).
3. **Closed-Form Parameter Estimation:** Computed the optimal parameter vector $\theta$ analytically using the Normal Equation:
   $$\theta = (X^T X)^{-1} X^T y$$
   The implementation utilizes matrix multiplication operations (`@`) alongside NumPy's linear algebra inversion module (`np.linalg.inv`).
4. **Inference:** Used the derived coefficients ($\theta_0, \theta_1$) to run prediction queries for unseen data points (e.g., forecasting the evaluation price for a $90\text{ m}^2$ property).

## Environment and Dependencies
* Python 3
* NumPy