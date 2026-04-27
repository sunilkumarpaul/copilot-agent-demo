#!/usr/bin/env python3
"""
Simple Calculator Module

Provides basic arithmetic operations: add, subtract, multiply, and divide.
"""


def add(a, b):
    """
    Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtract two numbers.
    
    Args:
        a: First number
        b: Second number (to be subtracted from a)
        
    Returns:
        The difference (a - b)
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide two numbers with zero division check.
    
    Args:
        a: Dividend (numerator)
        b: Divisor (denominator)
        
    Returns:
        The quotient (a / b)
        
    Raises:
        ValueError: If attempting to divide by zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    """
    Main function demonstrating calculator operations.
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
    
    print("=" * 30)


if __name__ == "__main__":
    main()
