def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    celsius: Temperature in Celsius
    Equivalent temperature in Fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    fahrenheit: Temperature in Fahrenheit
    Equivalent temperature in Celsius
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius_temperature = 100
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} degrees Celsius is {fahrenheit_temperature} degrees Fahrenheit")

fahrenheit_temperature = 212
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} degrees Fahrenheit is {celsius_temperature} degrees Celsius")
