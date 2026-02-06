from fuel import convert
from fuel import gauge
import pytest


def main():
    test_full()
    test_empty()
    test_regular()
    test_convert()
    test_str()
    test_larger_numerator()
    test_zero_denonominator()
    test_negative_fraction()


def test_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_empty():
    assert gauge(1) == "E"
    assert gauge(0.9) == "E"


def test_regular():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(12) == "12%"


def test_convert():
    assert convert("1/2") == 50
    assert convert("9/10") == 90
    assert convert("3/4") == 75
    assert convert("0/100") == 0


def test_str():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_larger_numerator():
    with pytest.raises(ValueError):
        convert("9/2")


def test_negative_fraction():
    with pytest.raises(ValueError):
        convert("-1/4")


def test_zero_denonominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


if __name__ == "__main__":
    main()
