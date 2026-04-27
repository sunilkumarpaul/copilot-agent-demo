#!/usr/bin/env python3
"""
Simple Calculator Module

Provides basic arithmetic operations: add, subtract, multiply, and divide.
Includes input validation for numeric values.
"""


def is_numeric(value):
    """
    Check if a value is numeric (int or float).
    
    Args:
        value: Value to check
        
    Returns:
        bool: True if value is int or float, False otherwise
        
    Raises:
        TypeError: If value is not a valid numeric type
    """
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(f"Expected numeric value, got {type(value).__name__}")
    return True


def validate_inputs(a, b):
    """
    Validate that both inputs are numeric.
    
    Args:
        a: First operand
        b: Second operand
        
    Raises:
        TypeError: If either input is not numeric
    """
    is_numeric(a)
    is_numeric(b)


def add(a, b):
    """
    Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
        
    Raises:
        TypeError: If inputs are not numeric
    """
    validate_inputs(a, b)
    return a + b


def subtract(a, b):
    """
    Subtract two numbers.
    
    Args:
        a: First number
        b: Second number (to be subtracted from a)
        
    Returns:
        The difference (a - b)
        
    Raises:
        TypeError: If inputs are not numeric
    """
    validate_inputs(a, b)
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
        
    Raises:
        TypeError: If inputs are not numeric
    """
    validate_inputs(a, b)
    return a * b


def divide(a, b):
    """
    Divide two numbers with zero division and input validation checks.
    
    Args:
        a: Dividend (numerator)
        b: Divisor (denominator)
        
    Returns:
        The quotient (a / b)
        
    Raises:
        TypeError: If inputs are not numeric
        ValueError: If attempting to divide by zero
    """
    validate_inputs(a, b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    """
    Main function demonstrating calculator operations with input validation.
    """
    print("Simple Calculator Demo")
    print("=" * 30)
    
    # Addition
    result = add(10, 5)
    print(f"10 + 5 = {result}")
    
    # Subtraction
    result = subtract(10, 5)
    print(f"10 - 5 = {result}")
    
    # Multiplication
    result = multiply(10, 5)
    print(f"10 * 5 = {result}")
    
    # Division
    result = divide(10, 5)
    print(f"10 / 5 = {result}")
    
    # Division by zero check
    try:
        result = divide(10, 0)
    except ValueError as e:
        print(f"Error: {e}")
    
    # Invalid input check
    try:
        result = add("10", 5)
    except TypeError as e:
        print(f"Error: {e}")
    
    print("=" * 30)


if __name__ == "__main__":
    main()
