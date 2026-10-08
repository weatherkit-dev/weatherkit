import httpx


class AsyncWeatherClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def current(self, city: str) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://api.example-weather.test/v1/current", params={"q": city, "key": self.api_key})
            return response.json()
