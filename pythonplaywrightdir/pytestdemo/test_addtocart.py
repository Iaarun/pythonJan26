import pytest

@pytest.mark.sanity
def test_addtocart():
    print("This is add to cart test")

@pytest.mark.regression
def test_checkout():
    print("This is checkout test")