# IEEE SSCS - Machine Learning Task 7

This repository contains the solutions and implementations for the first Machine Learning assignment (Level 1) provided by IEEE SSCS. The project focuses on understanding and implementing Logistic Regression from scratch, both mathematically and programmatically.

---

## Project Tasks

### Task 1: Mathematical Derivation of BCE Gradient
* Requirement: Complete mathematical derivation of the Binary Cross-Entropy (BCE) loss function gradient with respect to the model weights.
* Solution: The derivation was completed by hand using the chain rule to achieve the final gradient update expression.
* Attached File: ML_1_IEEE_Level_1.pdf

---

### Task 2: Sigmoid Function Implementation & Plotting
* Requirement: Implement the Sigmoid function using NumPy and generate its plot over an appropriate range using Matplotlib.
* Solution: An input range between -10 and 10 was selected to clearly demonstrate the S-shaped curve of the Sigmoid function and how it maps inputs to values between 0 and 1.

---

### Task 3 & 4: Logistic Regression From Scratch & XOR Testing
* Requirement: Build a reusable Logistic Regression model from scratch using only Python and NumPy (without machine learning libraries), and test it on a 4D XOR truth table.
* Code Structure:
  * classification.py: Contains the main LogisticRegression class including the fit and predict methods.
  * main.py: The main script used to define the 4D XOR dataset, import the model, train it, and print the outputs.

---

## Project Structure

* classification.py: Contains the model architecture.
* main.py: The main program to run the data and evaluate the model.
* README.md: The current documentation file.

---

## Important Technical Note on XOR Results
When running the model on the 4D XOR dataset, the predictions result in all 1s. 
The scientific reason behind this is that Logistic Regression is a linear classifier, whereas the XOR problem is non-linear and cannot be separated by a straight line or a single linear hyperplane. This outcome is expected and demonstrates the mathematical limitations of a simple linear model on non-linear data.

---

## How to Run
1. Ensure that NumPy and Matplotlib are installed.
2. Execute the main script via the terminal:
   python main.py
