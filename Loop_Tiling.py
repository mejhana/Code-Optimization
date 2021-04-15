from Parser import *

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
		new_loop = "for " + str(variables[0]) + " in range(" + str(variables[1] + "," + mid  + "," + str(variables[3]) + "):") 
		daughter_loop =  "for " + new_var + " in range(" + str(variables[0] + "," + str(variables[2]) + "," + last + "):") 
	elif len(variables) == 3:
		last = "min(" + str(variables[2]) + "," + str(variables[2]) + "+" + str(block_size) + ")"
		new_loop = "for " + str(variables[0]) + " in range(" + str(variables[1] + "," + str(block_size)+ "," + str(variables[2]) + "):")
		daughter_loop =  "for " + new_var + " in range(" + str(variables[0] + "," + last + "):") 
	return new_loop,daughter_loop

def perform_loop_tilling(sample_file, start_loop,end_loop, block_size):
	code = list(sample_file)
	#optimising all loops in reverse
	start_loop.reverse()
	end_loop.reverse()

	for i in range(len(start_loop)):
		index = start_loop[i]
		old_line = "".join(sample_file[index])
		#splitting each line into words
		line  = re.split(r'(\[|\]|\(|\)|;|,|\s)\s*',  old_line)
		new_var = "var" + str(index)
		new_loop,daughter_loop = loop_tilling(line,block_size,new_var)
		tabs = "	"*2*(len(start_loop) - i-1)
		block_tab = "    "*(len(start_loop) - i)
		print(str(len(start_loop)) +  str(i))
		#due last loops need not have their tabs changed! 
		if i == len(start_loop) - 1:
			tabs = ""
		code[code.index(old_line)] = tabs + new_loop + "\n"
		code.insert(index+1, "    " + tabs + daughter_loop + "\n")
		block_len = (end_loop[i]) - (start_loop[i] +1)
		print("block len" + str(block_len))
		for no in range(start_loop[i]+1 ,end_loop[i]):
			if not(i == 0) and no in range(start_loop[i-1], end_loop[i-1]): #outerloops need not change inner loops
				continue
			print(sample_file[no])
			line = "".join(sample_file[no])
			code[code.index(line)] = block_tab +  line 

	return code
