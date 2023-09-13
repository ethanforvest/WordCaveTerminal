import requests
import os
import platform
from Extractors import wordup

if platform.system() == "Windows":
    system_v = "cls"
elif platform.system() == "Linux" or platform.system() == "Linux2":
    system_v = "clear"
    
while True:
    word_input = input("Enter a word: ")

    if word_input.isnumeric() is True:
        print("Please enter a valid word! not a number(s)!\n")
        continue
    try:
        word_input = word_input.strip()
    except:
        print("Please enter a valid word!")
        continue
    
    os.system(system_v) 
    
    URL = "https://define.wrdp.app/" + word_input
    response = requests.get(URL)
    content_length = response.headers['Content-Length']

    if content_length == "0":
        print(f"Not Found -> \"{word_input}\"\n")
        continue
 
    json_ = response.json()
    wordup.printer(json_)

    print("\n")
    print(f"{wordup.definition_counter(json_)} Definition(s) | {wordup.example_counter(json_)} Example(s)")
    print("\n")
