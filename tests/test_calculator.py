import sys
sys.path.insert(0, 'ci-cd-learning/src')

def test_add():
    from calculator import add
    assert add(2,2) == 4
    assert add(2,1) != 4
