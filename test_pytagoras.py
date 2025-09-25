import pytest

from possible_solutions import pythagorean_triplets_smart

def test_pytagoras():
    
    assert pythagorean_triplets_smart(0) == []

def test_test_pytagoras_invalid_type(): 
    with pytest.raises(TypeError):
        pythagorean_triplets_smart("a")
    
 