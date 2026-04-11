import sys

import pytest



@pytest.mark.skipif(sys.platform == "win32", reason="This test is skipped because the system platform is Windows")
def test_addition():
    sum  = 2+3
    print(sum)

@pytest.mark.xfail(reason="This test is expected to fail because the assertion is incorrect")
def test_subtraction():
    sum  = 3-1
    assert sum == 5, "Subtraction result is incorrect"

@pytest.mark.skip(reason="This test is skipped because it is not relevant for the current testing phase")
def test_multiplication():
    sum  = 2*3
    print(sum)
