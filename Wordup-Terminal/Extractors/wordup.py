def WordText(json):  # Resulted word
    try:
        WordText_ = json['WordText']
    except:
        print("Couldn't find the word :(")
    return WordText_


def definition_counter(json):  # Looking for how many definitions are there
    definition_count = 0
    for word in range(100):
        try:
            definition = json['Senses'][word]['Definition']
            definition_count = definition_count + 1
        except:
            break
    return definition_count


def example_counter(json):  # Looking for how many examples are there
    example_count = 0
    for word in range(100):
        try:
            definition = json['Senses'][word]['Examples']
            example_count = example_count + 1
        except:
            continue
    return example_count


def gifs(self):  # Looking for images and GIFs
    import requests

    URL = f"https://word-images.cdn-wordup.com/opt/{WordText(self)}/selected.json"
    r = requests.get(URL)
    gifs = r.json()


def id_finder(self):
    id = json['Senses'][word]['ID']


def printer(json):  # Putting everything together and print them
    from colorama import init, Style, Fore

    # Resetting the color back to the default color after the end of every print statement is executed
    init(autoreset=True)
    definition_count = definition_counter(json)

    print(f"Enter a word: {WordText(json)}")

    for word in range(definition_count):
        definition = json['Senses'][word]['Definition']
        try:
            word_type = json['Senses'][word]['Type']
        except:
            word_type = ""
        print(
            f"Meaning {Fore.YELLOW}({word_type}){Style.RESET_ALL}: {Fore.GREEN + definition}")
        try:
            examples = json['Senses'][word]['Examples']
        except:
            continue
        else:
            print(f"Example: {examples}")
