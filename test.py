from py_jwt_verifier import PyJwtVerifier, PyJwtException

jwt = "eyJraWQiOiI3Vkl4OWZKZlVSTmU2RVhTYmd3c1A0VTRHRnZXQjhFYloxcjAtNVVLazU4IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwMHVrcWlkMHF1WWJ1WDg2ajBoNyIsInZlciI6MSwiaXNzIjoiaHR0cHM6Ly9hZHJpYW4ub2t0YXByZXZpZXcuY29tIiwiYXVkIjoiMG9hbHNleTg1OXhrNlVFQ0gwaDciLCJpYXQiOjE3MDg3MDk2OTgsImV4cCI6MTcwODcxMzI5OCwianRpIjoiSUQuR0NqMG5kU29LNWJpZE52Zjh5STJta0dacmpScTB5SkkyNjlKOWJIZF85TSIsImFtciI6WyJwd2QiXSwiaWRwIjoiMG9ha3FtYWQ5OHN6WVFvV0cwaDciLCJub25jZSI6ImMyMDY0YTM1LTA0YWMtNGM5My1iZWJjLWRjYTA4MDNjMDIwZiIsImF1dGhfdGltZSI6MTcwODcwNzU3Mn0.ZEBA0J8wvcHFCWLNJ98T6240TWq-9W8GkGfa_NodYhlJ4LmrUcNfymAeceSqLsAX5o6DQw0jJHq-neskLHNJGuEJyWzuWBKQqy7XgZ--W7T5HfrM2uVXXY64LWHWmsF4HPNU1UJDOpmPHFjdei6DRBycDbAQWb6LFUV6X3sLzwzTcZ9lrcxafewW5Idrl4OFHIAS7d9MQd0fi0GK6Q6qG5D5ZQO8QYmxvOgNoTbUYx18tH8Y8O5EpkmgLuWEQJRWMAsaChwc3uz8TmRSVwn-qr3J0GPQfxwVdlemPD3YpCPq9GYIBkV4bQ9wC-AvHPw4HW9jJmrMtNspXkMKmdoN4A"

try:
    print(PyJwtVerifier(jwt, auto_verify=False, check_expiry=False).verify(True))
except PyJwtException as e:

    print(f"Exception caught. Error: {e}")
