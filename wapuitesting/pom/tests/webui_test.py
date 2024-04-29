import pytest
def test_sample_one():
    a=5
    b=10
    assert a == b

def test_sample_two():
    a=7
    b=30
    assert a > b
def test_sample_three():
    a="dog"
    b="dog"
    assert a.__eq__(b)
