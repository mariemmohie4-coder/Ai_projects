# Data Visualization and Visual Analytics Framework

This repository contains the implementation of a comprehensive Data Visualization task executed through a structured 6-step pipeline. The project demonstrates advanced command over plotting libraries (Matplotlib and Seaborn) to transition raw data into clear, professional, and insight-driven visual representations.

## Visualization Pipeline Architecture

### Step 1: Base Line & Scatter Implementations
* Configured basic structural plots to understand geometric relationships and feature behavior.
* Applied explicit controls over axis limits, custom labels, dynamic marker styling, and targeted color maps.
* Utilized both Matplotlib's functional layer and Seaborn's high-level statistical interface to observe plotting variations.

### Step 2: Advanced Styling & Customization
* Applied professional visual constraints to ensure readability and corporate layout compliance.
* Integrated custom UI themes, strategic gridline structures, specific color palettes, and bounding box layouts.
* Handled figure scaling and text alignment parameters to maintain structural integrity across different viewport configurations.

### Step 3: Distribution Diagnostics
Evaluated the mathematical shape and spread of continuous datasets using statistical density metrics:
* **Histograms:** Constructed frequency bins to identify positive/negative skewness and multi-modal behavior.
* **Kernel Density Estimate (KDE) Plots:** Rendered smooth probability density curves to observe continuous probability distributions.
* **Empirical Cumulative Distribution Function (ECDF) Plots:** Mapped data points to extract percentile cutoffs directly without binning bias.

### Step 4: Categorical Comparison & Outlier Auditing
Isolated and contrasted categorical groups to extract underlying variations:
* **Bar Charts:** Aggregated discrete groups to visualize categorical measurements.
* **Box Plots:** Tracked five-number summaries (minimum, first quartile, median, third quartile, maximum) to expose mathematical outliers.
* **Violin Plots:** Merged box plot metrics with underlying KDE distribution curves to capture density variations inside categorical splits.

### Step 5: Advanced Heatmaps & Subplot Matrices
Combined individual features into synchronized structural overviews:
* **Correlation Heatmaps:** Mapped complete numerical feature spaces to detect multicollinearity or correlation coefficients.
* **Object-Oriented Programming (OOP) Subplots:** Built multi-panel visualization grids explicitly configuring `fig, axes = plt.subplots()` to handle high-dimensional dashboards within a single clean interface.

### Step 6: Visual Storytelling & Analytical Insights
* Derived 2–3 data-driven observations directly from the final generated charts for each dataset.
* Focused on communicating technical anomalies, trends, and actionable conclusions rather than just describing chart structures.

## Environment and Dependencies
* Python 3
* Matplotlib
* Seaborn
* Pandas