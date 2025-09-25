import pytest

from possible_solutions import solutions_diophantine_equation

def test_pytagoras():
    
    assert solutions_diophantine_equation(0) == []
    
    with pytest.raises{TypeError}:
        solutions_diophantine_equation(1)
    
 