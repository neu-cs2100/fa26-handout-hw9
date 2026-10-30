"""HW9 Question 4

You're building a system to simulate different types of vehicles at a ride-sharing
company. Each vehicle can carry passengers and travel a certain distance, but the
way fuel cost is calculated differs by vehicle type. For example, a gas car charges
per mile, while an electric car charges based on battery usage.

Your first task is to write a Vehicle abstract base class. Its constructor should take
and save the name of the vehicle (e.g., "Toyota Camry") and capacity (number of passengers 
that can fit). It should have two methods:
- `cost`, which takes the number of miles traveled as an argument and returns the cost of the trip.
The cost cannot be calculated with the information given, so the `cost` method should be abstract.
- `trip_summary`, which takes the number of miles traveled as an argument and returns a formatted 
summary of the trip in this format: "NAME: X miles, cost $Y" where NAME is the vehicle name, X is 
the number of miles traveled, and Y is the cost of the trip (in dollars and cents).

Then, you should implement three concrete subclasses: GasCar, ElectricCar, and Bicycle.

GasCar should calculate the cost of a trip based on miles driven, fuel efficiency (miles per 
gallon), and the current gas price. It should take the fuel efficiency (`mpg`) and gas price as 
constructor arguments. The cost of a trip should be calculated as `(miles / mpg) * gas_price`.

ElectricCar should calculate the cost of a trip based on miles driven, energy consumption (kWh 
per mile), and the current electricity rate. It should take the energy consumption 
(`kwh_per_mile`) and electricity rate as constructor arguments. The cost of a trip should be 
calculated as `(miles * kwh_per_mile) * electricity_rate`.

Bicycle should calculate the cost of a trip based on a flat maintenance fee. It should take the 
maintenance fee as a constructor argument. The cost of a trip should always be this flat fee, 
regardless of miles traveled. The capacity of the bicycle should always be 1.

Don't forget to write tests in the tests directory. You may use `pytest.approx` to compare floats,
since floating-point arithmetic can introduce small rounding errors. When testing whether a class 
is abstract (and cannot be instantiated), you may use `# type: ignore[abstract]` to suppress the 
Mypy error for attempting to instantiate a class with an abstract method.
"""
