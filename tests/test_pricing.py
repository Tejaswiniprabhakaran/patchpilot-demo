import pytest

from shop.pricing import apply_discount, basket_total, most_expensive


def test_discount():
    assert apply_discount(200.0, 10) == 180.0


def test_discount_rejects_bad_percent():
    with pytest.raises(ValueError):
        apply_discount(10.0, 150)


def test_basket_total():
    assert basket_total([10.0, 20.5, 30.25]) == 60.75


def test_basket_total_single_item():
    assert basket_total([9.99]) == 9.99


def test_basket_total_empty():
    assert basket_total([]) == 0.0


def test_most_expensive():
    assert most_expensive([3.0, 9.5, 1.0]) == 9.5
