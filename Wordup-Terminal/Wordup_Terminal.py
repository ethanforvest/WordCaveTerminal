import requests  
import json
import os 
from Extractors import wordup

while True:
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

    wordup.printer(json)

    print("\n")
    print(f"{wordup.definition_counter(json)} Definition(s) | {wordup.example_counter(json)} Example(s)")
    print("\n")