#!/usr/bin/env python3
"""
Module to calculate the derivative of a polynomial.
"""


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.

    Args:
        poly: A list of coefficients representing a polynomial.
              The index represents the power of x.

    Returns:
        A new list of coefficients representing the derivative,
        or None if poly is not valid.
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    for coef in poly:
        if not isinstance(coef, (int, float)):
            return None

    if len(poly) == 1:
        return [0]

    derivative = []
    for i in range(1, len(poly)):
        derivative.append(poly[i] * i)

    return derivative
