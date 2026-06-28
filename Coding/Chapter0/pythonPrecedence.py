#!/usr/bin/env python3
"""
Program to print the Python Operator Precedence Table
"""

def print_precedence_table():
    precedence = [
        (1, "Parentheses / Function Call / Subscription / Slicing / Attribute", "(a+b), f(x), a[0], a[1:5], obj.attr"),
        (2, "Await", "await x"),
        (3, "Exponentiation", "**"),
        (4, "Unary Operators", "+x, -x, ~x"),
        (5, "Multiplication, Matrix Multiplication,\n   Division, Floor Division, Modulus", "*, @, /, //, %"),
        (6, "Addition, Subtraction", "+, -"),
        (7, "Bitwise Shift", "<<, >>"),
        (8, "Bitwise AND", "&"),
        (9, "Bitwise XOR", "^"),
        (10, "Bitwise OR", "|"),
        (11, "Comparison, Membership, Identity", "<, <=, >, >=, !=, ==, in, not in, is, is not"),
        (12, "Logical NOT", "not"),
        (13, "Logical AND", "and"),
        (14, "Logical OR", "or"),
        (15, "Conditional Expression", "x if condition else y"),
        (16, "Lambda Expression", "lambda"),
        (17, "Assignment Expression", ":=")
    ]

    print("PYTHON OPERATOR PRECEDENCE TABLE")
    print("=" * 100)
    print(f"{'Level':<6} {'Operator Category':<45} {'Operators / Example'}")
    print("-" * 100)

    for level, category, operators in precedence:
        print(f"{level:<6} {category:<45} {operators}")

    print("-" * 100)
    print("Note: Level 1 has the highest precedence, while Level 17 has the lowest.")

if __name__ == "__main__":
    print_precedence_table()