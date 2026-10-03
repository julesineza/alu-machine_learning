#!/usr/bin/env python3

def poly_integral(poly, C=0):
    if not isinstance(poly, list) or not poly:
        return None

    if not isinstance(C, int):
        return None

    for coefficient in poly:
        if not isinstance(coefficient, (int, float)):
            return None

    result = [C]

    for i in range(len(poly)):
        coefficient = poly[i]

        new_coefficient = coefficient / (i + 1)

        if new_coefficient.is_integer():
            new_coefficient = int(new_coefficient)

        result.append(new_coefficient)

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result
