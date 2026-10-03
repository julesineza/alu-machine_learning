def poly_integral(poly, C=0):
    # Validate C is an integer and not a boolean
    if not isinstance(C, int) or isinstance(C, bool):
        return None
        
    # Validate poly is a list
    if not isinstance(poly, list):
        return None
        
    # Validate all coefficients are numbers and not booleans
    for coeff in poly:
        if not isinstance(coeff, (int, float)) or isinstance(coeff, bool):
            return None
            
    # Compute the integral coefficients
    result = [C]
    for i, coeff in enumerate(poly):
        val = coeff / (i + 1)
        # Convert to integer if it is a whole number
        if val == int(val):
            val = int(val)
        result.append(val)
        
    # Clean up trailing zeros to make the list as small as possible
    while result and result[-1] == 0:
        result.pop()
        
    return result
