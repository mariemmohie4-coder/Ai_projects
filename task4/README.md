# Zara Sales Exploratory Data Analysis (EDA)

This repository contains a comprehensive Exploratory Data Analysis (EDA) framework executed on the Zara Sales Dataset. The primary objective is to audit data quality, uncover latent operational patterns, isolate distribution anomalies, and deliver clear, actionable business intelligence for technical and corporate stakeholders.

## Project Architecture and Technical Pipeline

### 1. Structural Assessment and Data Auditing
* **Dimensionality Profiling:** Mapped the total record counts, isolated individual features, and audited native data types (categorical, numerical, and datetime vectors).
* **Schema Validation:** Evaluated structural integrity to confirm data alignment with expected retail schema definitions.

### 2. Data Quality Engineering and Preprocessing
* **Missing Value Analysis:** Quantified missing entries across feature columns, applying strategic imputation mechanics or drop-conditions where appropriate.
* **Inconsistency Resolution:** Handled data quality issues, syntax variations in text features, and structural formatting anomalies.

### 3. Univariate Statistical Profiling
Examined the statistical properties and distribution shapes of isolated variables:
* **Numerical Features:** Plotted probability spreads, checked for skewness, and evaluated metrics including skew directional tails across features like prices and sales volumes.
* **Categorical Features:** Visualized class distributions to identify volume variations and operational balances across clothing lines, sizes, and seasonal categories.

### 4. Bivariate, Multivariate, and Correlation Analysis
Evaluated complex interactions within the feature space to discover driving business elements:
* **Feature Interactions:** Mapped relationships between numerical pricing structures, discounting behaviors, and net transaction velocities.
* **Correlation Matrices:** Computed full-scale correlation matrices to isolate high-affinity pairs and screen for structural multicollinearity.
* **Categorical Splitting:** Evaluated performance margins across mixed categorical dimensions (e.g., assessing sales performance across product lines cross-referenced with seasonal timelines).

### 5. Outlier Detection and Risk Assessment
* Leveraged statistical boundaries (such as Interquartile Range [IQR] fencing and Z-score distributions) to pinpoint anomalies.
* Audited extreme values to separate true operational spikes (e.g., high-volume holiday transactions) from data-entry corruption, assessing their impact on baseline downstream estimators.

### 6. Visual Analytics Portfolio
The codebase generates and embeds the following core diagnostic visualizations:
* **Histograms & KDE Overlays:** Tracking pricing and sales distribution shapes.
* **Boxplots:** Identifying outlier variations across product groups and operational seasons.
* **Correlation Heatmaps:** Quantifying linear dependencies across numeric indicators.
* **Scatter Plots:** Isolating pricing vs. sales volume density boundaries.
* **Bar & Categorical Counts:** Benchmarking performance distributions across categories.

---

## Key Core Findings & Operational Insights

* **Distribution Patterns:** Pricing and transaction attributes demonstrate a distinct right-skewed log-normal distribution, reflecting standard high-volume, lower-price retail operations.
* **Correlation Structures:** Strong correlation boundaries exist between promotional discounting depths and inventory turnover rates, highlighting price elasticity patterns.
* **Anomaly Isolations:** Outliers in sales volumes correlate heavily with specific localized promotional events and micro-seasonal transitions rather than systematic logging failures.

## Analytical Summary
The structural insights derived from this pipeline reveal critical performance differences between core clothing categories and fast-fashion inventory components. These visualizations provide a clear, data-backed foundation for downstream predictive modeling, demand forecasting, and price optimization frameworks.

## Environment and Dependencies
* Python 3
* Pandas & NumPy (Data manipulation)
* Matplotlib & Seaborn (Visual analytics)
* SciPy (Statistical auditing)