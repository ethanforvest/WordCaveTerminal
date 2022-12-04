<<<<<<< HEAD
def definition_count(json):
=======
def WordText(json): #Resulted word
	try:
		WordText = json['WordText']
	except:
		print("Couldn't find the word :(")
	return WordText

def definition_counter(json): #Looking for how many definitions are there
>>>>>>> beta
	definition_count = 0
	for word in range(100):
		try:
			definition = json['Senses'][word]['Definition']
			definition_count = definition_count + 1
		except:
			break
	return definition_count       

<<<<<<< HEAD
def example_count(json):
=======
def example_counter(json): #Looking for how many examples are there
>>>>>>> beta
	example_count = 0
	for word in range(100):
		try:
			definition = json['Senses'][word]['Examples']
			example_count = example_count + 1
		except:
			continue
<<<<<<< HEAD
	return example_count
=======
	return example_count

def printer(json): #Putting everything together and print them
	from colorama import init
	from colorama import Fore, Back, Style

	init(autoreset=True) #Resetting the color back to the default color after the end of every print statement is executed
	definition_count = definition_counter(json)
	example_count = example_counter(json)

	print(f"Enter a word: {WordText(json)}")

	for word in range(definition_count):
	    definition = json['Senses'][word]['Definition']
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
>>>>>>> beta
