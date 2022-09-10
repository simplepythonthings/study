import pytest

from src.figures.triangle import Triangle
from src.figures.circle import Circle
from src.figures.square import Square
from src.figures.rectangle import Rectangle


@pytest.fixture
def positive_triangle():
    """for the positive triangle creation test"""
    return Triangle(13, 14, 15)


@pytest.fixture
def positive_circle():
    """for the positive circle creation test"""
    return Circle(13)


@pytest.fixture
def positive_square():
    """for the positive square creation test"""
    return Square(17)


@pytest.fixture
def positive_rectangle():
    """for the positive rectangle creation test"""
    return Rectangle(33, 71)
