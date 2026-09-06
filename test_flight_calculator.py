import pytest
from flight_calculator import calculate_flight_time

def test_zero_payload_returns_maximum_flight_time():
    assert calculate_flight_time(0) == 180


def test_typical_payload_uses_linear_formula():
    assert calculate_flight_time(500) == 130


def test_fractional_payload_is_supported():
    assert calculate_flight_time(125.5) == 167.45


def test_flight_time_reaches_zero_at_1800_grams():
    assert calculate_flight_time(1800) == 0


def test_flight_time_is_never_negative():
    assert calculate_flight_time(2000) == 0


def test_negative_payload_raises_value_error():
    with pytest.raises(ValueError) as error:
        calculate_flight_time(-1)

    assert str(error.value) == "Payload weight cannot be negative."




    # Additional tests for flight_time_table function
from flight_calculator import flight_time_table, calculate_flight_time
def test_flight_time_table():
    result = flight_time_table(300, 100)

    assert result == [
        (0, 180),
        (100, 170),
        (200, 160),
        (300, 150)
    ]
