from calculator import Calculator
import pytest

def test_interprete_equation():
    calculator = Calculator()
    assert calculator.interprete_equation(["1", "+", "1"]) == [1, "+", 1]

...
def test_input_equation(monkeypatch):
        # monkeypatch the "input" function, so that it returns "1 + 1".
        # This simulates the user entering "1 + 1" in the terminal:
        monkeypatch.setattr('builtins.input', lambda _: "1 + 1")
        calculator = Calculator()
        assert calculator.input_equation() == ["1", "+", "1"]


...

...
def test_operation_invalid_operator(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1 / 0")
    calculator = Calculator()
    with pytest.raises(ZeroDivisionError):
        calculator.operation()
...

...