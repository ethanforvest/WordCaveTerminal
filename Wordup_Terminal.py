import requests  
import json
from colorama import init
from colorama import Fore, Back, Style
import os 
from Extractors import wordup

definition_count = 0
example_count = 0

while True:
    init(autoreset=True)
    word_input = input("Enter a word: ")

    if word_input.isnumeric() == True:
        print("Please enter a valid word! not a number(s)!\n")
        continue

    try:
        word_input = word_input.strip()
    except:
        print("Please enter a valid word!")
        continue

    os.system("cls")
    URL = "https://define.wrdp.app/" + word_input

    r = requests.get(URL)
    json = r.json()

    definition_count = wordup.definition_count(json)
    example_count = wordup.example_count(json)

    print(f"Enter a word: {word_input}")

    for word in range(definition_count):
        definition = json['Senses'][word]['Definition']
        print(f"Meaning: {Fore.GREEN + definition}")
        try:
            examples = json['Senses'][word]['Examples']
        except:
            continue
        else:
            print(f"Example: {examples}")
      
    print("\n")
    print(f"{definition_count} Definition(s) | {example_count} Example(s)")
    print("\n")


