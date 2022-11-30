import requests
import json
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)
word = input("Enter a word: ")
URL = "https://define.wrdp.app/" + word

r = requests.get(URL)
json = r.json()

for word in range(5):
	try:
  		definition = json['Senses'][word]['Definition']
  		examples = json['Senses'][word]['Examples']
	except:
  		break
	print(f"Meaning: {Fore.GREEN + definition}")
	print(f"Example: {examples}")