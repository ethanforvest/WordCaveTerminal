import requests
import json
from colorama import init
from colorama import Fore, Back, Style
import os

while True:
	init(autoreset=True)
	word_input = input("Enter a word: ")
	os.system("cls")
	URL = "https://define.wrdp.app/" + word_input

	r = requests.get(URL)
	json = r.json()

	for word in range(5):
		try:
	  		definition = json['Senses'][word]['Definition']
	  		examples = json['Senses'][word]['Examples']
		except:
	  		break
		print(f"Enter a word: {word_input}")
		print(f"Meaning: {Fore.GREEN + definition}")
		print(f"Example: {examples}")
	print("\n")


