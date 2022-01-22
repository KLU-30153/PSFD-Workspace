#content of test_sample.py
import pytest
def func(x):
    return x+1
@pytest.mark.vamsi
def test_answer():
    assert func(3) == 4