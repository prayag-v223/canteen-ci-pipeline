
import pytest
from decimal import Decimal
from canteen import calculate_total


def test_total_without_discount():
    assert calculate_total(100) == Decimal("105.00")


def test_total_at_discount_boundary():
    assert calculate_total(300) == Decimal("315.00")


def test_total_with_discount():
    assert calculate_total(400) == Decimal("378.00")


def test_total_just_above_boundary():
    assert calculate_total(301) == Decimal("284.45")

def test_zero_order():
    assert calculate_total(0) == Decimal("0.00")


def test_negative_subtotal():
    with pytest.raises(ValueError):
        calculate_total(-100)

def test_temporary_ci_failure():
    assert calculate_total(100) == Decimal("999.00")
