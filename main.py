import re

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

# works for certain cases, example spaces must be there!! 

def tag_words(word):
	identifier = re.compile(r"^[^\d\W]\w*\Z", re.UNICODE)
	digits = re.compile(r"([0-9]+(?:\.[0-9]+)?)")
	tag = ""
	keywords = ["for", "in", "range" ,"while" ,"if", "elif" ,"else"]
	if word in keywords:
		tag = "keyword"
	elif re.match(identifier, word):   
		tag = "identifier"
	elif re.match(digits ,word):
		tag = "number"
	return tag

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

def scanning(file, loop_keyword, ifs_keyword):
	in_loop = False
	line_number = 0
	block = 0
	tabs = ""

	#finding start and ending lines of loops and if-else blocks !!
	start_loop = []
	end_loop = []
	start_if = []
	end_if = []
	all_starts =[]
	
	for line in file:
		line_number +=1
		if line.startswith(tabs):
			for word in line.split():
				#increment line number with each line
				if word in loop_keyword:
					tabs = tabs + '  '
					start_loop.append(line_number)
					all_starts.append(word)
					block +=1
				elif word in ifs_keyword:
					tabs = tabs + '  '
					start_if.append(line_number)
					all_starts.append(word)
					block +=1
		else: 
			#decrementing the tabs_loop for nested loops
			if not (block == 0):
				tabs.replace('  ', '')
				if all_starts[block-1] in loop_keyword:
					end_loop.append(line_number)
					block -=1
					
				else:
					end_if.append(line_number)	
					block -=1
	#condition where more than 2 blocks end in same line
	if all_starts[block-1] in loop_keyword and not(block == 0):
		end_loop.append(line_number)
		block -=1
		
	elif not(block == 0):
		end_if.append(line_number)	
		block -=1		
	print("number of lines in this code is " +str(line_number))				

	return start_loop,end_loop,start_if,end_if


def main():
	block_size = 2
	#filename = input("Enter your file path with filename and extension")
	filename = "sample_code.py"
	file = open(filename, "r").readlines()
	#get starts and ends of loops and also run code for deadcode! 
	loop = ["for", "while"]
	ifs = ["if", "elif" ,"else"]
	start_loop,end_loop,start_if,end_if = scanning(file,loop,ifs) 
	print(start_loop,end_loop,start_if,end_if)
	# for loop tilling 
	for i in range(len(start_loop)):
		#optimising all loops in reverse
		line  = file[start_loop[-i]-1].split()
		new_loop,daughter_loop = loop_tilling(line,block_size)
		print("The old loop was \n"+ str(file[start_loop[-i]-1]) + "\n")
		print("The new loops are \n" + new_loop)
		print(daughter_loop + "\n")

	# for deadcode 
	for i in range(len(start_loop)):
		#optimising all loops in reverse
		line  = file[start_loop[-i]-1].split()
		deadcode(line)

if __name__ == "__main__":
    main()

 
	

