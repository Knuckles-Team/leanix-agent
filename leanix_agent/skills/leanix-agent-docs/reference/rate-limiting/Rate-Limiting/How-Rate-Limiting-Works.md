##  How Rate Limiting Works
If you reach a rate limit, you get the HTTP 429 Too Many Requests response status code.
The API response may contain a message showing the reason for reaching the rate limit. For example, if you reach a user-based rate limit, you get a response like the following: HTTP 429 Too Many Requests. USER_INTERVAL_REQUEST_LIMIT_EXCEEDED.
In the event of rate limiting or temporary unavailability, the API response may include a Retry-After header, indicating the recommended duration the client should wait before initiating a new request. If this header is not present, the client must determine an appropriate retry interval based on the specific rate limits established by the API.
