# 📘 Assignment: Introduction to Unit Testing with Unittest

## 🎯 Objective

Learn how to write unit tests using Python's built-in `unittest` framework to verify code behavior, catch bugs early, and practice test-driven development. You'll write test cases that validate functions against expected inputs and outputs.

## 📝 Tasks

### 🛠️ Write Your First Unit Tests

#### Description
Create basic test cases using `unittest` to verify that simple functions work correctly.

#### Requirements
Completed program should:

- Import `unittest` and define a test class that inherits from `unittest.TestCase`
- Write at least 3 test methods using `assertEqual()` to verify function output
- Test the provided functions with both typical and edge case inputs
- Run tests using `python -m unittest` and verify they all pass

### 🛠️ Test Edge Cases and Error Conditions

#### Description
Expand your tests to handle edge cases, boundary conditions, and error scenarios.

#### Requirements
Completed program should:

- Write tests for empty inputs, negative numbers, and large values
- Use `assertRaises()` to verify that functions raise appropriate exceptions
- Test boundary conditions (e.g., zero, maximum/minimum values)
- Ensure all test methods have descriptive names that explain what they test

### 🛠️ Organize Tests and Measure Coverage

#### Description
Structure your tests professionally with multiple test classes and use coverage analysis to identify untested code paths.

#### Requirements
Completed program should:

- Organize test cases into separate test classes by functionality
- Use `setUp()` and `tearDown()` methods for test preparation and cleanup
- Install and run `coverage.py` to analyze test coverage
- Achieve at least 80% code coverage on the provided functions
- Document which code paths are tested and why any untested code exists
