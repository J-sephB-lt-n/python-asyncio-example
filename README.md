# python-asyncio-example
Example usage of threaded concurrency in python using asyncio

Run a very basic example:

```bash
$ python main.py

...
```

Run an example of concurrent HTTP requests:

```bash
$ python -m api_requests_example.main

12:58:51.692451 started GET https://www.google.com
12:58:51.693251 started GET https://www.duckduckgo.com
12:58:52.497299 finished GET https://www.google.com response was: 200 OK
12:58:54.338485 finished GET https://www.duckduckgo.com response was: 200 OK
-- SUMMARY OF RESULTS --
https://www.google.com/ 200
https://duckduckgo.com/ 200
```
