import re

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

def Parsing(file, loop_keyword, ifs_keyword):
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