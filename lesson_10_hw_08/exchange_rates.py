from pprint import pprint
import httpx
import asyncio


class ExchangeRates:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self) -> None:
        if ExchangeRates._initialized:
            return

        ExchangeRates._initialized = True

    @staticmethod
    async def fetch_from_api() -> dict:
        url = (
            "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
            "&from_currency=USD&to_currency=UAH&apikey=PASTE_YOUR_API_KEY"
        )
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        return response.json()

    @staticmethod
    async def get_rate(source: str, target: str) -> float:
        url = (
            f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
            f"&from_currency={source}&to_currency={target}&apikey=PASTE_YOUR_API_KEY"
        )
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        return response.json()['Realtime Currency Exchange Rate']['5. Exchange Rate']


async def main():
    er = ExchangeRates()
    tasks = [er.fetch_from_api(), er.get_rate("USD", "UAH")]
    results = await asyncio.gather(*tasks)

    for result in results:
        pprint(result)


if __name__ == "__main__":
    asyncio.run(main())

    # er = ExchangeRates()
    #
    # pprint(asyncio.run(er.fetch_from_api()))
    # pprint(asyncio.run(er.get_rate("USD", "UAH")))
