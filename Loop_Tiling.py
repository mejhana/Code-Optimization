from Parser import *
import numpy as np



def loop_tilling(line,block_size,new_var):
	new_loop = " "
	daughter_loop = " "
	print("\nperforming loop tilling")
	variables = []
	#retrieve the variables used! 
	for word in line:
		tag = tag_words(word)
		if tag == "identifier" or tag == "number":
			variables.append(word)
	print(variables)
	if len(variables) == 4:
		mid = str(variables[2]) + "+" + str(block_size)
		last = "min(" + str(variables[3]) + "," + str(variables[3]) + "+" + str(block_size) + ")"
		new_loop = "for " + str(variables[0]) + " in range(" + str(variables[1] + "," + mid  + "," + str(variables[3]) + "):\n") 
		daughter_loop =  "for " + new_var + " in range(" + str(variables[0] + "," + str(variables[2]) + "," + last + "): + \n") 
	elif len(variables) == 3:
		last = "min(" + str(variables[2]) + "," + str(variables[2]) + "+" + str(block_size) + ")"
		new_loop = "for " + str(variables[0]) + " in range(" + str(variables[1] + "," + str(block_size)+ "," + str(variables[2]) + "): \n")
		daughter_loop =  "for " + new_var + " in range(" + str(variables[0] + "," + last + "): \n") 
	return new_loop,daughter_loop

def perform_loop_tilling(sample_file, start_loop,end_loop, block_size):
	code = list(sample_file)
	daughter_loops = []
	new_var = []
	old_var = []
	for i in range(len(start_loop)):
		index = start_loop[i]
		old_line = "".join(sample_file[index])
		#splitting each line into words
		line  = re.split(r'(\[|\]|\(|\)|;|,|\s)\s*',  old_line)
		var = get_var(line)
		old_var.append(var[0])
		new_var.append("var" + str(index))
		new_loop,daughter_loop = loop_tilling(line,block_size,str(new_var[-1]))
		daughter_loops.append(daughter_loop)
		tabs = "    "*(i)
		if i == 0:
			tabs = ""
		#changing loop
		code[index] = tabs + new_loop
		block_index = index
		if i == (len(start_loop) -1 ): #inner most loop, add daughter loops 
			daughter_loops.reverse()
			for j in range(len(daughter_loops)):
				daughter_tabs = "    "*(len(daughter_loops) - j) + "    "
				code.insert(index+1, "    " + daughter_tabs + daughter_loops[j])
				block_index += 1
			
			# get block of code within inner most loop !
			for block in range(start_loop[i] + 1, end_loop[i]):
				new_line = ""
				line  = replace_var(sample_file[block], new_var , old_var)
				code[block_index+1] =  "    "*(len(start_loop)) + str(line) + "\n"
				block_index += 1
	return code
