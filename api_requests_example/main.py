import asyncio
import datetime
import requests

now = datetime.datetime.now


async def async_request(**kwargs) -> requests.models.Response:
    method: str = kwargs.get("method")
    url: str = kwargs.get("url")
    print(now().time(), "started", method, url)
    response: requests.models.Response = await asyncio.to_thread(
        requests.request, **kwargs
    )
    print(
        now().time(),
        "finished",
        method,
        url,
        "response was:",
        response.status_code,
        response.reason,
    )
    return response


async def main():
    tasks = [
        async_request(method=method, url=url, timeout=10)
        for method, url in [
            ("GET", "https://www.google.com"),
            ("GET", "https://www.duckduckgo.com"),
        ]
    ]
    return await asyncio.gather(*tasks)


if __name__ == "__main__":
    results = asyncio.run(main())
    print("-- SUMMARY OF RESULTS --")
    for result in results:
        print(result.url, result.status_code)
