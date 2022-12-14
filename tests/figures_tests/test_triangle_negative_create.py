import pytest

from src.figures.triangle import Triangle


def test_triangle_negative_create():
    """negative triangle creation test"""
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)
