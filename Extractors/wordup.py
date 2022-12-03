def definition_count(json):
	definition_count = 0
	for word in range(100):
		try:
			definition = json['Senses'][word]['Definition']
			definition_count = definition_count + 1
		except:
			break
	return definition_count       

def example_count(json):
	example_count = 0
	for word in range(100):
		try:
			definition = json['Senses'][word]['Examples']
			example_count = example_count + 1
		except:
			continue
	return example_count