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

def perform_loop_tilling(sample_file, start_loop,end_loop, block_size,tilling_file):
	code = list(sample_file)
	start_loop.reverse()
	end_loop.reverse()

	for i in range(len(start_loop)):
		#optimising all loops in reverse
		index = start_loop[i]
		old_line = "".join(sample_file[index])
		line  = re.split(r'(\[|\]|\(|\)|;|,|\s)\s*',  old_line)
		new_var = "var" + str(index)
		new_loop,daughter_loop = loop_tilling(line,block_size,new_var)
		tabs = "	"*2*(len(start_loop) - i-1)
		block_tab = "    "*(len(start_loop) - i)
		print(str(len(start_loop)) +  str(i))
		if i == len(start_loop) - 1:
			code[code.index(old_line)] = new_loop + "\n"
			code.insert(index+1, "    " + daughter_loop + "\n") 

		else:
			code[code.index(old_line)] = tabs + new_loop + "\n"
			code.insert(index+1, "    " + tabs + daughter_loop + "\n")
			block_len = (end_loop[i]) - (start_loop[i] +1)
			print("block len" + str(block_len))
			if i == 0: #inner most loop
				for no in range(start_loop[i]+1 ,end_loop[i]):
					print(sample_file[no])
					line = "".join(sample_file[no])
					code[code.index(line)] = block_tab +  line 
			else:
				for no in range(start_loop[i]+1 ,end_loop[i]):
					if no in range(start_loop[i-1], end_loop[i-1]):
						continue
					print(sample_file[no])
					line = "".join(sample_file[no])
					code[code.index(line)] = block_tab +  line
				

		#print("The old loop was \n"+ str(sample_file[start_loop[-i]-1]) + "\n")
		#print("The new loops are \n" + new_loop)
		#print(daughter_loop + "\n")

	#write code into file 
	f = open(tilling_file, "w")
	code = "".join(code)
	f.write(code)
	f.close()
