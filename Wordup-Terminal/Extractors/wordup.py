def WordText(self):  # Resulted word
    try:
        WordText_ = self['WordText']
    except:
        print("Couldn't find the word :(")
    else:
        return WordText_


def definition_counter(self):  # Looking for how many definitions are there
    definition_count = 0
    for word in range(100):
        try:
            definition = self['Senses'][word]['Definition']
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

    URL = f"https://word-images.cdn-wordup.com/opt/{self}/selected.json"
    r = requests.get(URL)
    gifs = r.json()
    return gifs


def printer(json):  # Putting everything together and print them
    from colorama import init, Style, Fore

    init(autoreset=True)
    definition_count = definition_counter(json)

    found_word = WordText(json)
    print(f"Enter a word: {found_word}")

    gif_json = gifs(found_word)   # All the avilable GIFS/IMGs

    for word in range(definition_count):

        definition = json['Senses'][word]['Definition']
        i_d = json['Senses'][word]['ID']

        try:
            word_type = json['Senses'][word]['Type']
        except:
            word_type = ""
        print(f"Meaning {Fore.YELLOW}({word_type}){Style.RESET_ALL}: {Fore.GREEN + definition}")
        try:
            examples = json['Senses'][word]['Examples']
        except:
            continue
        else:
            print(f"Example: {examples}")
        finally:
            # looking for the correct GIF/IMG
            for key, value in gif_json.items():
                if key == i_d:
                    if "https" not in value:
                        if "opt" not in value:
                            print(f"{Fore.CYAN}GIF/IMG:{Style.RESET_ALL} https://word-images.cdn-wordup.com/opt/{value}")
                        else:
                            print(f"{Fore.CYAN}GIF/IMG:{Style.RESET_ALL} https://word-images.cdn-wordup.com/{value}")
                    else:
                        print(f"{Fore.CYAN}GIF/IMG:{Style.RESET_ALL} {value}")