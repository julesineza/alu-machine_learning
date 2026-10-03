#!/usr/bin/env python3
def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.

    Args:
        poly: A list of coefficients representing a polynomial.
              The index represents the power of x.
        C: The constant of integration (default is 0).

    Returns:
        A new list of coefficients representing the integral,
        or None if poly is not valid.
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    for coef in poly:
        if not isinstance(coef, (int, float)):
            return None

    integral = [C]  # Start with the constant of integration
    for i in range(len(poly)):
        integral.append(poly[i] / (i + 1))

    return integral
