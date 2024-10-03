import requests
response = requests.get('https://official-joke-api.appspot.com/jokes/random')
joke = response.json()
print(joke['setup'])
print(joke['punchline'])