import re
import tokenize
from io import StringIO

def scan(line):
	words = re.split(r'(\[|\]|\(|\)|;|,|\s)\s*', line)
	return words


def replace_var(line, new_var, old_var):
	sep = scan(line)
	var = get_var(sep)
	for v in var:
		for n,o in zip(new_var,old_var):
			if v == o:
				line = line.replace(v,n)
	return line

def tag_words(word):
	identifier = re.compile(r"^[^\d\W]\w*\Z", re.UNICODE)
	digits = re.compile(r"([0-9]+(?:\.[0-9]+)?)")
	tag = ""
	keywords = ["for", "in", "range" ,"while" ,"if", "elif" ,"else","continue","break","print"]
	if word in keywords:
		tag = "keyword"
	elif re.match(identifier, word):   
		tag = "identifier"
	elif re.match(digits ,word):
		tag = "number"
	return tag

def get_var(line):
	var = []
	for word in line:
		tag = tag_words(word)
		#append word to var if it is an identifer and not already present in var
		if tag == "identifier" and not(word in var):
			var.append(word)
	return var

def Parsing(file):
	loop_keyword = ["for", "while"]
	ifs_keyword = ["if", "elif" ,"else"]
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
		if line.startswith(tabs):
			for word in scan(line):
				#increment line number with each line
				if word in loop_keyword:
					start_loop.append(line_number)
					tabs = tabs + '  '
					all_starts.append(word)
					block +=1
				elif word in ifs_keyword:
					start_if.append(line_number)
					tabs = tabs + '  '
					all_starts.append(word)
					block +=1
			line_number +=1	
		elif not (block == 0):
			#decrementing the tabs_loop for nested loops
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

	while(len(end_loop)<len(start_loop)):
		end_loop.append(line_number)			

	return start_loop,end_loop,start_if,end_if

def remove_comments(file_name):
	fileObj = open(file_name, 'r')
	code = list(open(file_name, 'r'))
	for toktype, tok, start, end, line in tokenize.generate_tokens(fileObj.readline):
		if toktype == tokenize.COMMENT:
			code[code.index(line)] = ""
	return(code)


