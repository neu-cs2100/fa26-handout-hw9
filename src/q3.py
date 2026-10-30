"""HW9 Question 3

Let's design animal classes for an animal shelter's website. The website
allows users to view information about the animals in the shelter. They
can search specifically for cats or dogs, but they can also view all animals together
(including rabbits, hamsters, etc.). To make our code more organized and reusable,
we will use inheritance.

Your first task is to write an Animal class that will serve as the base class for all animals in 
the shelter. Its constructor should take the name, age, and species as arguments, and save them
as attributes. It should also provide a method called `describe` that returns a string description 
of the animal in the format "NAME is a AGE-year-old SPECIES." (where NAME, AGE, and SPECIES are 
replaced with the animal's name, age, and species).

Then, you should write subclasses for Cat and Dog that inherit from Animal. They should
use super().__init__() to initialize the common attributes before setting their species-specific 
attributes.

The Dog constructor should take the name, age, breed, and training status (`is_trained`) as 
arguments. Its species should always be set to "Dog".

The Cat constructor should take the name, age, color, and indoor-only status (`indoor_only`) as 
arguments. Its species should always be set to "Cat".

You are not required to write tests for this question, but we have provided the tests 
from the autograder.
"""
