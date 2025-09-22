#!/usr/bin/env python3
"""
Simple Python application for CI/CD demonstration
"""

def add_numbers(a, b):
    """Add two numbers and return the result"""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers and return the result"""
    return a * b

def main():
    """Main function to demonstrate the application"""
    print("Sample Python Application")
    print("Addition: 5 + 3 =", add_numbers(5, 3))
    print("Multiplication: 4 * 6 =", multiply_numbers(4, 6))
    print("Application executed successfully!")

if __name__ == "__main__":
    main()
