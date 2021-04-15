from Deadcode_Removal import *
from Loop_Tiling import *
from Loop_Unrolling import *
from loop_vectorization import *
from shutil import copyfile
import re 
import os
import fileinput

def write(code, new_file_path):
	#write code into file 
	f = open(new_file_path, "w")
	code = "".join(code)
	f.write(code)
	f.close()


def main():
	block_size = 2
	#filename = input("Enter your file path with filename and extension")
	#sample_code
	filename = "sample_code.py"
	#write back for tiling
	tilling_file = "after_loop_tiling.py"

	sample_file = open(filename, "r").readlines()

	#get starts and ends of loops and also run code for deadcode! 
	start_loop,end_loop,start_if,end_if = Parsing(sample_file) 
	print(start_loop,end_loop,start_if,end_if)

	#choice = input("Enter \n0 for Deadcode elimination \n1 for Loop Tilling \n2 for Code Motion \n3 for Loop Unrolling")

	# for loop tilling 
	code = perform_loop_tilling(sample_file,start_loop,end_loop,block_size)
	# write back into a new file! 
	write(code, tilling_file)

	# for deadcode 
	'''
	for i in range(len(start_loop)):
		#optimising all loops in reverse
		line  = sample_file[start_loop[-i]-1].split()
		deadcode(line)
	

	#for loop unrolling
	#for all loops in sample_file! 
	variable_list = []
	for i in range(len(start_loop)):
		#get all variables inside loop!
		lines = []
		for j in range(start_loop[-i]-1,end_loop[-i]-2):
			lines.append(re.split(r'(\[|\]|\(|\)|;|,|\s)\s*', sample_file[j]))
		var = get_var(lines)
		for j in var:
			if not(j in variable_list):
				variable_list.append(j)

	print("All the variables are - " + str(variable_list))
	#do loop unrolling only if it has 2 indexes 
	#Line = "array(i+1, k-2) = array(i+0, k-2) + array(i+1, k-2) - array(i+3, k-256877845);"
	#print(unroll(unroll(Line, "k", 4), "i", 3, False))
	'''
if __name__ == "__main__":
    main()

 
	

