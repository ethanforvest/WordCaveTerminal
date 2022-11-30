import requests
import json

word = input("Enter a word: ")
URL = "https://define.wrdp.app/" + word

r = requests.get(URL)
json = r.json()

definition_1 = json['Senses'][0]['Definition']
Examples_1 = json['Senses'][0]['Examples']

definition_2 = json['Senses'][1]['Definition']
Examples_2 = json['Senses'][1]['Examples']

print("\n")
print(f"Meaning: {definition_1}")
print(f"Examples: {Examples_1}\n\n")

print(f"Meaning: {definition_2}")
print(f"Examples: {Examples_2}")


	
