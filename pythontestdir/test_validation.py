#pytest is test framework for python, it is used to write test cases for python code.
# It is a simple and easy to use framework that allows you to write test cases
# in a simple and easy to understand way.

import pytest
# def sum(a, b):
#     sum = a + b
#     if sum == 3:
#         print ("Fail")
#
# sum(1, 2)



def sum(a,b):
    print("This is the sum function")






def multiply(a,b):
    print("This is the multiply function")
    return a * b
@pytest.mark.regression
def test_sum(firstPresetup,  preSessionSetup):
    assert sum(1, 2) == 3

@pytest.mark.smoke
def test_multiply(firstPresetup, preSessionSetup):
    assert multiply(1, 2) == 2
