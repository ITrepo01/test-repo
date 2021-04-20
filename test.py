import sys
import requests


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://itrepo.com")
print(r.status_code)

print(greet("world"))
print(greet("corey"))
