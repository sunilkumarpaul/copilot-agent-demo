#!/usr/bin/env python3
"""
Test suite for the calculator module (main.py)

Tests all arithmetic operations, input validation, and error handling.
"""

import unittest
from main import add, subtract, multiply, divide, is_numeric, validate_inputs


class TestIsNumeric(unittest.TestCase):
    """Test cases for the is_numeric function."""
    
    def test_integer_input(self):
        """Test that integers are recognized as numeric."""
        self.assertTrue(is_numeric(5))
        self.assertTrue(is_numeric(0))
        self.assertTrue(is_numeric(-10))
    
    def test_float_input(self):
        """Test that floats are recognized as numeric."""
        self.assertTrue(is_numeric(5.5))
        self.assertTrue(is_numeric(0.0))
        self.assertTrue(is_numeric(-10.5))
    
    def test_string_input(self):
        """Test that strings raise TypeError."""
        with self.assertRaises(TypeError):
            is_numeric("5")
        with self.assertRaises(TypeError):
            is_numeric("")
    
    def test_boolean_input(self):
        """Test that booleans raise TypeError."""
        with self.assertRaises(TypeError):
            is_numeric(True)
        with self.assertRaises(TypeError):
            is_numeric(False)
    
    def test_none_input(self):
        """Test that None raises TypeError."""
        with self.assertRaises(TypeError):
            is_numeric(None)
    
    def test_list_input(self):
        """Test that lists raise TypeError."""
        with self.assertRaises(TypeError):
            is_numeric([1, 2, 3])
    
    def test_dict_input(self):
        """Test that dictionaries raise TypeError."""
        with self.assertRaises(TypeError):
            is_numeric({"key": "value"})


class TestValidateInputs(unittest.TestCase):
    """Test cases for the validate_inputs function."""
    
    def test_valid_integers(self):
        """Test that valid integers pass validation."""
        validate_inputs(5, 10)
        validate_inputs(0, 0)
        validate_inputs(-5, -10)
    
    def test_valid_floats(self):
        """Test that valid floats pass validation."""
        validate_inputs(5.5, 10.5)
        validate_inputs(0.0, 0.0)
        validate_inputs(-5.5, -10.5)
    
    def test_mixed_numeric_types(self):
        """Test that mixed int/float pass validation."""
        validate_inputs(5, 10.5)
        validate_inputs(5.5, 10)
    
    def test_invalid_first_argument(self):
        """Test that invalid first argument raises TypeError."""
        with self.assertRaises(TypeError):
            validate_inputs("5", 10)
    
    def test_invalid_second_argument(self):
        """Test that invalid second argument raises TypeError."""
        with self.assertRaises(TypeError):
            validate_inputs(5, "10")
    
    def test_both_invalid_arguments(self):
        """Test that invalid arguments raise TypeError."""
        with self.assertRaises(TypeError):
            validate_inputs("5", "10")


class TestAdd(unittest.TestCase):
    """Test cases for the add function."""
    
    def test_positive_integers(self):
        """Test addition of positive integers."""
        self.assertEqual(add(5, 10), 15)
        self.assertEqual(add(1, 1), 2)
    
    def test_positive_floats(self):
        """Test addition of positive floats."""
        self.assertAlmostEqual(add(5.5, 10.5), 16.0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=1)
    
    def test_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(add(-5, 10), 5)
        self.assertEqual(add(5, -10), -5)
        self.assertEqual(add(-5, -10), -15)
    
    def test_mixed_types(self):
        """Test addition with mixed int/float types."""
        self.assertAlmostEqual(add(5, 10.5), 15.5)
        self.assertAlmostEqual(add(5.5, 10), 15.5)
    
    def test_with_zero(self):
        """Test addition with zero."""
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(0, 0), 0)
    
    def test_invalid_input_string(self):
        """Test that string input raises TypeError."""
        with self.assertRaises(TypeError):
            add("5", 10)
    
    def test_invalid_input_both_strings(self):
        """Test that both string inputs raise TypeError."""
        with self.assertRaises(TypeError):
            add("5", "10")


class TestSubtract(unittest.TestCase):
    """Test cases for the subtract function."""
    
    def test_positive_integers(self):
        """Test subtraction of positive integers."""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 5), 0)
    
    def test_positive_floats(self):
        """Test subtraction of positive floats."""
        self.assertAlmostEqual(subtract(10.5, 5.5), 5.0)
    
    def test_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(subtract(-5, 10), -15)
        self.assertEqual(subtract(10, -5), 15)
        self.assertEqual(subtract(-5, -10), 5)
    
    def test_mixed_types(self):
        """Test subtraction with mixed int/float types."""
        self.assertAlmostEqual(subtract(10, 5.5), 4.5)
        self.assertAlmostEqual(subtract(10.5, 5), 5.5)
    
    def test_with_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(0, 0), 0)
    
    def test_invalid_input(self):
        """Test that invalid input raises TypeError."""
        with self.assertRaises(TypeError):
            subtract(10, "5")


class TestMultiply(unittest.TestCase):
    """Test cases for the multiply function."""
    
    def test_positive_integers(self):
        """Test multiplication of positive integers."""
        self.assertEqual(multiply(5, 10), 50)
        self.assertEqual(multiply(7, 8), 56)
    
    def test_positive_floats(self):
        """Test multiplication of positive floats."""
        self.assertAlmostEqual(multiply(5.5, 10.0), 55.0)
        self.assertAlmostEqual(multiply(2.5, 4.0), 10.0)
    
    def test_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(multiply(-5, 10), -50)
        self.assertEqual(multiply(5, -10), -50)
        self.assertEqual(multiply(-5, -10), 50)
    
    def test_mixed_types(self):
        """Test multiplication with mixed int/float types."""
        self.assertAlmostEqual(multiply(5, 10.5), 52.5)
        self.assertAlmostEqual(multiply(5.5, 10), 55.0)
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(0, 0), 0)
    
    def test_multiply_by_one(self):
        """Test multiplication by one."""
        self.assertEqual(multiply(5, 1), 5)
        self.assertEqual(multiply(1, 5), 5)
    
    def test_invalid_input(self):
        """Test that invalid input raises TypeError."""
        with self.assertRaises(TypeError):
            multiply(5, [10])


class TestDivide(unittest.TestCase):
    """Test cases for the divide function."""
    
    def test_positive_integers(self):
        """Test division of positive integers."""
        self.assertEqual(divide(10, 5), 2.0)
        self.assertEqual(divide(20, 4), 5.0)
    
    def test_positive_floats(self):
        """Test division of positive floats."""
        self.assertAlmostEqual(divide(10.5, 5.0), 2.1)
        self.assertAlmostEqual(divide(20.0, 4.0), 5.0)
    
    def test_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(divide(-10, 5), -2.0)
        self.assertEqual(divide(10, -5), -2.0)
        self.assertEqual(divide(-10, -5), 2.0)
    
    def test_mixed_types(self):
        """Test division with mixed int/float types."""
        self.assertAlmostEqual(divide(10, 5.0), 2.0)
        self.assertAlmostEqual(divide(10.5, 5), 2.1)
    
    def test_division_resulting_in_decimal(self):
        """Test division resulting in decimal."""
        self.assertAlmostEqual(divide(10, 3), 3.333333, places=5)
        self.assertAlmostEqual(divide(5, 2), 2.5)
    
    def test_divide_by_zero(self):
        """Test that division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))
    
    def test_divide_zero_by_number(self):
        """Test division of zero by a number."""
        self.assertEqual(divide(0, 5), 0.0)
    
    def test_invalid_input_string(self):
        """Test that string input raises TypeError."""
        with self.assertRaises(TypeError):
            divide(10, "5")
    
    def test_invalid_input_boolean(self):
        """Test that boolean input raises TypeError."""
        with self.assertRaises(TypeError):
            divide(10, True)


class TestIntegration(unittest.TestCase):
    """Integration tests combining multiple operations."""
    
    def test_chained_operations(self):
        """Test chaining multiple operations."""
        # (10 + 5) * 2 - 6 / 3 = 29
        result = add(10, 5)
        self.assertEqual(result, 15)
        
        result = multiply(result, 2)
        self.assertEqual(result, 30)
        
        result = subtract(result, divide(6, 3))
        self.assertEqual(result, 28.0)
    
    def test_error_recovery(self):
        """Test error handling during operations."""
        # Test that valid operation works after invalid one
        with self.assertRaises(TypeError):
            add("invalid", 5)
        
        # Next valid operation should work
        result = add(5, 10)
        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()
