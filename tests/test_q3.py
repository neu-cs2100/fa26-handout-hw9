"""HW9 Question 3 Tests"""

import sys
import unittest
from unittest.mock import patch
sys.path.append('.')
from src.q3 import Dog, Cat

# Parameter names for Animal.__init__ (excluding self), in order
_ANIMAL_INIT_PARAMS = ['name', 'age', 'species']


def _get_animal_init_kwargs(mock_call: unittest.mock._Call) -> dict[str, object]:
    """Normalize a mock call to Animal.__init__ into a dict, regardless of 
    positional/keyword usage."""
    args, kwargs = mock_call
    result = {_ANIMAL_INIT_PARAMS[i]: val for i, val in enumerate(args)}
    result.update(kwargs)
    return result

class TestAnimalCatDog:
    """Tests for Dog and Cat constructors."""
    def test_cat_constructor_calls_super(self) -> None:
        """Test that the Cat constructor calls super().__init__()."""
        with patch('src.q3.Animal.__init__') as mock_super_init:
            Cat(name="Mini", age=2, color="Tuxie", indoor_only=False)
            mock_super_init.assert_called_once()
            called_with = _get_animal_init_kwargs(mock_super_init.call_args)
            assert called_with == {"name": "Mini", "age": 2, "species": "Cat"}

    def test_dog_constructor_calls_super(self) -> None:
        """Test that the Dog constructor calls super().__init__()."""
        with patch('src.q3.Animal.__init__') as mock_super_init:
            Dog(name="Mono", age=3, breed="Golden Retriever", is_trained=True)
            mock_super_init.assert_called_once()
            called_with = _get_animal_init_kwargs(mock_super_init.call_args)
            assert called_with == {"name": "Mono", "age": 3, "species": "Dog"}

    def test_dog_attributes(self) -> None:
        """Test the Dog constructor sets attributes correctly."""
        dog = Dog(name="Mono", age=3, breed="Golden Retriever", is_trained=True)
        assert dog.name == "Mono"
        assert dog.age == 3
        assert dog.species == "Dog"
        assert dog.breed == "Golden Retriever"
        assert dog.is_trained

    def test_cat_attributes(self) -> None:
        """Test the Cat constructor sets attributes correctly."""
        cat = Cat(name="Mini", age=2, color="Tuxie", indoor_only=False)
        assert cat.name == "Mini"
        assert cat.age == 2
        assert cat.species == "Cat"
        assert cat.color == "Tuxie"
        assert not cat.indoor_only
