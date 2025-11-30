def test_add():
    from calculator_pkg.calculator import add
    assert add(2,2) == 4
    assert add(2,1) != 4
