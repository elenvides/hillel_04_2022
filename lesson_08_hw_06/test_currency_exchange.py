import pytest
from currency_exchange_v2 import Currency, Price


def test_same_currency_addition():
    price1 = Price(100, Currency.UAH)
    price2 = Price(50, Currency.UAH)
    result = price1 + price2
    assert result.amount == 150
    assert result.currency == Currency.UAH


def test_same_currency_subtraction():
    price1 = Price(100, Currency.UAH)
    price2 = Price(50, Currency.UAH)
    result = price1 - price2
    assert result.amount == 50
    assert result.currency == Currency.UAH


def test_different_currency_addition():
    price1 = Price(100, Currency.UAH)
    price2 = Price(1, Currency.USD)
    result = price1 + price2
    assert result.amount == 137.5
    assert result.currency == Currency.UAH


def test_different_currency_subtraction():
    price1 = Price(100, Currency.UAH)
    price2 = Price(1, Currency.USD)
    result = price1 - price2
    assert result.amount == 62.5
    assert result.currency == Currency.UAH


def test_double_conversion_currency_addition():
    price1 = Price(100, Currency.UAH)
    price2 = Price(10, Currency.GBP)
    result = price1 + price2
    assert result.amount == pytest.approx(585.1, 0.01)
    assert result.currency == Currency.UAH
