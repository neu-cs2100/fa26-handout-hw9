"""HW9 Question 1: Properties

Please write a Temperature class that allows users to keep track of the temperature using 
Celsius or Fahrenheit. The class should store one temperature internally, and allow the client 
to access and modify the temperature using either Celsius or Fahrenheit.

The constructor should take one argument: the initial temperature in Celsius.

The class should provide properties called `celsius` and `fahrenheit` for getting and 
setting the temperature in the respective units. If the client ever tries to set the value
to a temperature below absolute zero (including in the constructor), a ValueError should be 
raised.

Recall that absolute zero is the lowest possible temperature:
    Celsius: -273.15°C
    Fahrenheit: -459.67°F

You should use constants such as ABS_ZERO_CELSIUS and ABS_ZERO_FAHRENHEIT to represent 
absolute zero.

Recall these formulas for converting between Celsius and Fahrenheit: 
    Fahrenheit = Celsius * 9 / 5 + 32
    Celsius = (Fahrenheit - 32) * 5 / 9

Don't forget to write tests in the tests directory. You may use `pytest.approx` to compare floats,
since floating-point arithmetic can introduce small rounding errors.
"""
