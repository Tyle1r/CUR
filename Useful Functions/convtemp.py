def convtemp(temp, from_unit, to_unit):
    # Supported temperature units: 'C' (Celsius), 'F' (Fahrenheit), 'K' (Kelvin)
    if from_unit == to_unit:
        return temp  # No conversion needed
    
    if from_unit == 'C':
        if to_unit == 'F':
            return (temp * 9/5) + 32
        elif to_unit == 'K':
            return temp + 273.15
    elif from_unit == 'F':
        if to_unit == 'C':
            return (temp - 32) * 5/9
        elif to_unit == 'K':
            return (temp - 32) * 5/9 + 273.15
    elif from_unit == 'K':
        if to_unit == 'C':
            return temp - 273.15
        elif to_unit == 'F':
            return (temp - 273.15) * 9/5 + 32
    
    raise ValueError("Unsupported temperature units or conversion")

# Example usage:
celsius_temp = convtemp(100, 'C', 'F')
print(celsius_temp)  # Output: 212.0
