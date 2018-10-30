from mysoftware import * 
from pytest import *

def test_square_integers(): 
    assert square(2) == 4
    assert square(0) == 0
    assert square(-1) == 1

def test_coulomb(): 
    with pytest.raises(ZeroDivisionError):
        coulomb(0)
