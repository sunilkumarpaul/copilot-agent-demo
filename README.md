# Copilot Agent Demo

A simple Python calculator project demonstrating basic arithmetic operations.

## Description

This project provides a straightforward calculator module with the following operations:
- **Add**: Sum two numbers
- **Subtract**: Difference between two numbers
- **Multiply**: Product of two numbers
- **Divide**: Quotient of two numbers with zero division protection

## Features

- Simple, clean API for basic arithmetic
- Input validation (division by zero check)
- Comprehensive docstrings
- Example usage in main function

## Installation

No external dependencies are required. Simply clone the repository:

```bash
git clone https://github.com/sunilkumarpaul/copilot-agent-demo.git
cd copilot-agent-demo
```

## Usage

Run the calculator demo:

```bash
python main.py
```

Or import and use in your own code:

```python
from main import add, subtract, multiply, divide

# Perform calculations
print(add(10, 5))        # Output: 15
print(subtract(10, 5))   # Output: 5
print(multiply(10, 5))   # Output: 50
print(divide(10, 5))     # Output: 2.0

# Division by zero raises ValueError
try:
    divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Cannot divide by zero
```

## Project Structure

```
.
├── main.py          # Calculator functions and demo
├── requirements.txt # Project dependencies
└── README.md        # This file
```

## License

MIT License
