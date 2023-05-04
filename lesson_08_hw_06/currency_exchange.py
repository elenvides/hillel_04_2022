from enum import Enum


class Currency(Enum):
    USD = "USD"
    UAH = "UAH"
    GBP = "GBP"


class Price:
    def __init__(self, amount: int, currency: Currency) -> None:
        self.amount: int = amount
        self.currency: Currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Price(self.amount + other.amount, self.currency)
        else:
            exchanged_amount = self._exchange(other, self.currency)
            return Price(self.amount + exchanged_amount, self.currency)

    def __sub__(self, other):
        if self.currency == other.currency:
            return Price(self.amount - other.amount, self.currency)
        else:
            exchanged_amount = self._exchange(other, self.currency)
            return Price(self.amount - exchanged_amount, self.currency)

    @staticmethod
    def _get_exchange_rates():
        return {
            Currency.USD: {Currency.UAH: 37.5, Currency.GBP: 0.7727},
            Currency.UAH: {Currency.USD: 0.02667, Currency.GBP: 0.0216},
            Currency.GBP: {Currency.USD: 1.2936, Currency.UAH: 46.45}
        }

    def _exchange(self, other, target_currency):
        conversion_rates = self._get_exchange_rates()

        if other.currency == Currency.USD:
            usd_amount = other.amount
        else:
            usd_amount = other.amount * conversion_rates[other.currency][Currency.USD]

        if target_currency == Currency.USD:
            return usd_amount
        else:
            rate_to_target_currency = conversion_rates[Currency.USD][target_currency]
            return usd_amount * rate_to_target_currency

    def __str__(self):
        return f'{self.amount} {self.currency.value}'
