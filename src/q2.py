"""HW9 Question 2: Read-only properties

Please create a BankAccount class that stores a balance and allows depositing and withdrawing 
money.

The constructor should take one argument, for the initial balance (in whole-number cents). If the 
initial balance is zero or negative, it should raise a ValueError.

Add a read-only property called `balance` that returns the current balance (in cents).

Also, overwrite the `__str__` method to provide a string representation of the balance in the 
bank account in dollars and cents in this format: `$D.CC` where `D` is dollars and `CC` is cents
(exactly two digits for cents).

Then, add two methods:
1. deposit`, which takes the number of cents to add to the balance, and adds it to the balance if 
it's greater than zero. If the amount to add is zero or negative, it should raise a ValueError.
`deposit` should not return anything.
2. `withdraw`, which takes the number of cents to subtract from the balance, and subtracts it 
from the balance if a) it's greater than zero and b) it does not exceed the current balance. If 
the amount is zero or negative, it should raise a ValueError. If the amount to withdraw exceeds 
the current balance, it should raise a RuntimeError. `withdraw` should not return anything.

Don't forget to write tests in the tests directory. When testing whether a property is read-only,
you may use `# type: ignore[misc]` to suppress the Mypy error for attempting to set a read-only 
property.
"""
