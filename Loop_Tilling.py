from Parser import *

def loop_tilling(line,block_size):
	print("performing loop tilling\n")
	variables = []
	#retrieve the variables used! 
	for word in line:
		tag = tag_words(word)
		if tag == "identifier" or tag == "number":
			variables.append(word)
	
	if len(variables) == 4:
		mid = str(variables[2]) + "+" + str(block_size)
		last = "min(" + str(variables[3]) + "," + str(variables[3]) + "+" + str(block_size) + ")"
		new_loop = "for " + str(variables[0]) + " in range(" + str(variables[1] + "," + mid  + "," + str(variables[3]) + "):") 
		daughter_loop =  "for " + "daughter_var" + " in range(" + str(variables[0] + "," + str(variables[2]) + "," + last + "):") 
	elif len(variables) == 3:
		last = "min(" + str(variables[2]) + "," + str(variables[2]) + "+" + str(block_size) + ")"
		new_loop = "for " + str(variables[0]) + " in range(" + str(variables[1] + "," + str(block_size)+ "," + str(variables[2]) + "):")
		daughter_loop =  "for " + "daughter_var" + " in range(" + str(variables[0] + "," + last + "):") 
	return new_loop,daughter_loop
