# Matrix Operations Tool

A pure Python command-line utility for executing basic matrix and scalar mathematical operations without relying on external libraries like NumPy.

## Features
The tool supports the following mathematical computations:
1. **Matrix Sum:** Adds two matrices of identical dimensions.
2. **Matrix Subtraction:** Subtracts one matrix from another of identical dimensions.
3. **Matrix Multiplication:** Performs standard dot-product multiplication on compatible matrices.
4. **Scalar Addition:** Adds a uniform scalar value to every element within a matrix.
5. **Scalar Multiplication:** Multiplies every element within a matrix by a uniform scalar value.
6. **Normalization:** Scales all elements of a matrix into a range between 0 and 1 using Min-Max normalization.

## Technical Specifications
* **Input Parsing:** Uses the `ast.literal_eval` library to securely convert text input directly into Python nested lists representing matrices.
* **Dimension Validation:** Checks for structural compatibility before executing matrix operations to prevent indexing errors.
* **Zero Variance Handling:** Includes a safeguard during normalization to return a zero-matrix if all elements in the input matrix are identical (avoiding division-by-zero errors).

## Sample Execution Formats
When running the script, matrices should be formatted as nested lists. For example:
* **Matrix 1:** `[[1, 2], [3, 4]]`
* **Matrix 2:** `[[5, 6], [7, 8]]`
* **Scalar:** `2.5`