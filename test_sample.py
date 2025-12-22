import pytest

def test_sample_one():
    expectedText="Vivek"
    actualText="test"
    #use assert to report failure
    assert expectedText.__eq__(actualText)
def test_sample_two():
    a=100
    b=100
    assert a==b

def test_sample_third():
    a=100
    b=50
    assert a<b