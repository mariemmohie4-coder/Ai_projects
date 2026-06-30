# Titanic Data Exploratory Data Analysis (EDA)

This repository contains the implementation of Task 2, which focuses on data preprocessing, cleaning, and exploratory data analysis (EDA) of the Titanic passenger dataset using Pandas, Matplotlib, and Seaborn. The analysis tracks passenger distributions and evaluates structural factors influencing survival rates.

## Project Architecture

### 1. Data Cleaning and Imputation Pipeline
* **Age Vector Rectification:** Missing numerical indices in the `Age` column were imputed using the dataset's median distribution. Fractional components were cast into standard integers, and logical anomalies (values recorded as zero) were systematically replaced with the median reference.
* **Text Feature Engineering (Cabin Parsing):** Extracted structural cabin locations by isolating the initial letter of the string (`Cabin_letter`). Missing entries were grouped under a explicit "Missing" categorical state to account for unassigned accommodations.
* **Categorical Imputation:** Missing instances within the `Embarked` (port of embarkation) feature were normalized by assigning a descriptive "Missing" category to maintain data completeness without deleting operational samples.

### 2. Exploratory Data Analysis (EDA)
Calculated single-variable distributions across several dimensions to observe basic baseline behaviors:
* **Histograms:** Generated frequency plots for continuous numeric intervals including `Age` and `Fare`.
* **Value Counting:** Extracted discrete categorical counts across class ratings (`Pclass`), biological classifications (`Sex`), structural deck groups (`Cabin_letter`), and target metrics (`Survived`).

### 3. Bivariate Survival Relations
Evaluated and visualized relationships between target outcomes (`Survived`) and structural passenger attributes using percentage transformations and bar plots:
* **Survival by Sex:** Grouped metrics confirm that female passengers recorded a significantly higher survival rate relative to male passengers.
* **Survival by Socio-Economic Class (Pclass):** Quantified cross-tabulations show that first-class accommodations held distinct advantages, yielding higher survival probabilities compared to third-class assignments.
* **Survival by Cabin Distribution:** Analyzed deck structural locations and highlighted that an overwhelming majority of unassigned or missing cabin flags correlated heavily with lower-tier ticketing structures.
* **Survival by Age Quantization:** Binned data into standard continuous ranges (`child`, `teenager`, `adult`, `senior`) using the `pd.cut` map. Results show elevated survival probabilities in younger demographics (`child`).
* **Survival by Financial Tiers (Fare Quantiles):** Categorized monetary properties into uniform percentile-based blocks (`Low`, `Medium`, `High`, `Very High`) via `pd.qcut`. The output indicates a monotonic rise in survival rates directly correlating with higher purchasing power.

## Output Distribution
The clean dataset containing newly transformed group categories and imputed values is exported as a separate file titled `titanic_clean.csv`, setting up a clean baseline for prospective predictive or machine learning workflows.

## Environment and Dependencies
* Python 3
* Pandas
* Matplotlib