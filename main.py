def deadcode(start_loop, end_loop):
	print("performing dead code elination")
	# write your code here 
	return 

def loop_tilling(start_loop, end_loop):
	print("performing loop tilling")
	# write your code here 
	return

def scanning(file,loop_keyword, ifs_keyword):
	in_loop = False
	line_number = 0
	tabs = ""
	#finding start and ending lines of loops for loop optimization
	start_loop = []
	end_loop = []
	start_if = []
	end_if = []
	all_starts =[]
	block = 0
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
	#filename = input("Enter your file path with filename and extension")
	filename = "tester code.py"
	file = open(filename, "r")
	#get starts and ends of loops and also run code for deadcode! 
	loop = ["for", "while"]
	ifs = ["if", "elif" ,"else"]
	start_loop,end_loop,start_if,end_if = scanning(file,loop,ifs) 
	print(start_loop,end_loop,start_if,end_if)

	for i in range(len(start_loop)):
		#optimising all loops in reverse
		loop_tilling(start_loop[-i], end_loop[-i])
	for i in range(len(start_loop)):
		#optimising all loops in reverse
		deadcode(start_if[-i], end_if[-i])


	file.close() 

if __name__ == "__main__":
    main()

 
	

