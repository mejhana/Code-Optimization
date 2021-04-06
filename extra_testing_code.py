def loop_tilling(file, start_loop, end_loop,block_size):
	print("performing loop tilling")
	code_block = file[start_loop-1].split()
	print(code_block)

	new_loop = "for " + str(code_block[1]) + " in range(" + str(code_block[6]) +',' + str(block_size) + ',' + str(code_block[7]) + ')'
	print(new_loop)
	daughter_loop = "for daughter in range(" + str(code_block[2]) +  "min(" + str(code_block[7]) + "," + str(code_block[5]) + str(block_size) + "))"
	print(daughter_loop)
	return

def retrieving_variables(file,start_loop,end_loop):
	line = []
	for word in file[start_loop-1].split():
		line.append(word)
	variables = [line[1] , line[5] , line [7] , line[9]]
	return variables