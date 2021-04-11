from parser import *

def deadcode(line):
	print("performing dead code elination")
	variables = []
	#retrieve the variables used! 
	for word in line:
		tag = tag_words(word)
		if tag == "identifier" or tag == "number":
			variables.append(word)
	# write your code here 
	return 