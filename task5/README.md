# California Housing Prices Prediction (Regression Analysis)

This repository contains the implementation of Task 5 (Level 1), which focuses on building, evaluating, and optimization of regression models to predict the `Median House Value` based on geographic, demographic, and structural metrics derived from the 1990 California census dataset.

## Dataset Features and Schema
The predictive framework processes the following architectural attributes:
* **Target Variable:**
  * `Median House Value`: Median house value within a specific census block (USD).
* **Demographic & Structural Features:**
  * `Median Income`: Median household income within a block (measured in tens of thousands of USD).
  * `Median Age`: Median age of houses within a block (years).
  * `Total Rooms` / `Total Bedrooms`: Total counts of functional structural spaces within a block.
  * `Population` / `Households`: Demographic density metrics capturing total residents and family units per block.
* **Geographic & Spatial Features:**
  * `Latitude` / `Longitude`: Raw geographic coordinates (°).
  * `Distance to Coast`: Geodesic distance to the nearest coastal boundary (meters).
  * `Distance to Major Cities`: Proximity parameters measuring the exact distance (meters) to the urban centers of Los Angeles, San Diego, San Jose, and San Francisco.

---

## Machine Learning Pipeline Architecture

### 1. Feature Engineering and Spatial Preprocessing
* **Scale Normalization:** Handled extreme value variances between features (e.g., matching coordinates in degrees with distances in meters) using scaling techniques to prevent parameter distortion during optimization.
* **Geospatial Processing:** Leveraged proximity vectors to urban centers and coastal boundaries as essential predictors, capturing the structural premium associated with California real estate.

### 2. Regression Frameworks and Optimization
* **Baseline Linear Modeling:** Constructed an Ordinary Least Squares (OLS) linear model to capture standard linear relationships between socioeconomic features (like income) and housing values.
* **Polynomial Feature Expansion:** Mapped feature boundaries using higher-order polynomial relationships to catch localized non-linear trends.
* **Regularized Systems (Ridge and Lasso):** Integrated L1 and L2 regularization penalties to stabilize parameter tracking, manage multicollinearity among spatial vectors, and prevent overfitting.

### 3. Model Evaluation Metrology
The models were benchmarked across a series of continuous evaluation metrics to track predictive error profiles:
* **Root Mean Squared Error (RMSE):** Used as the primary index to measure the physical error margin in USD while penalizing high-variance forecasting failures.
* **Mean Absolute Error (MAE):** Tracking average absolute deviation trends in housing costs.
* **Coefficient of Determination ($R^2$ Score):** Quantifying the proportion of structural variance explained by the model compared to the baseline mean.

## Summary of Insights
* **Income Predominance:** Exploratory analysis confirms that `Median Income` holds the highest linear correlation with property pricing structures.
* **Geospatial Dominance:** Proximity parameters—specifically `Distance to Coast` and distance to major metropolitan areas—act as critical non-linear weights that significantly improve model accuracy when expanded via polynomial mapping.

## Environment and Dependencies
* Python 3
* NumPy & Pandas (Data wrangling)
* Scikit-Learn (Model architectures, scaling, and validation tools)
* Matplotlib & Seaborn (Diagnostic visualization mapping)