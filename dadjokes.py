import requests
from random import choice 
from pyfiglet import figlet_format
from termcolor import colored

url = "https://icanhazdadjoke.com/search"
user_input = input("Let me tell you a joke! Give me a topic: ")

res = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()

num_jokes = res["total_jokes"]
results = res["results"]

if num_jokes > 1:
    print(f"I've got {num_jokes} jokes about {user_input}. Here's one.")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(f"There is one joke about {user_input}")
    print(results[0]['joke'])
else:
    print(f"Sorry, couldn't find a joke with your term: {user_input}")