from past.builtins.misc import execfile
import numpy as np
import time 
import re 
import os

#Userdefined Functions

from loop_vectorization import *
from Loop_Unrolling import *
from Loop_Tiling import *


def write(code, new_file_path):
	#write code into file 
	f = open(new_file_path, "w")
	code = "".join(code)
	f.write(code)
	f.close()

def read(filename):
	code = open(filename, "r").readlines()
	return code

def til_loop(input_filename,output_filename):
	block_size = int(input("\nEnter Block Size - "))
	#reading the file to optimise
	input_file = read(input_filename)

	#get starts and ends of loops and if blocks
	start_loop,end_loop,start_if,end_if = Parsing(input_file) 
	print(start_loop,end_loop,start_if,end_if)

	# for loop tilling 
	code = perform_loop_tilling(input_file,start_loop,end_loop,block_size)
	# write back into a new file! 
	write(code, output_filename)

	#checking performance by executing files
	tic = time.time()
	execfile(input_filename)
	toc = time.time()
	print("Time taken BEFORE Loop Tiling - "+ str(1000*(toc-tic))+"ms")

	tic = time.time()
	execfile(output_filename)
	toc = time.time()
	print("Time taken AFTER Loop Tiling - "+ str(1000*(toc-tic))+"ms")

def vect(input_filename,output_filename):
	print("Shruthi do this lol")
	#reading the file to optimise
	input_file = read(input_filename)

	#get starts and ends of loops and if blocks
	start_loop,end_loop,start_if,end_if = Parsing(input_file) 
	print(start_loop,end_loop,start_if,end_if)

	#code = performing vectorization or something 
	# write back into a new file! 
	#write(code, output_filename)

	#checking performance by executing files
	tic = time.time()
	execfile(input_filename)
	toc = time.time()
	print("Time taken BEFORE Loop Vectorization - "+ str(1000*(toc-tic))+"ms")

	tic = time.time()
	execfile(output_filename)
	toc = time.time()
	print("Time taken AFTER Loop Vectorization - "+ str(1000*(toc-tic))+"ms")
	
def unrolling(input_filename,output_filename):
	print("Shreya do this lol")
	#reading the file to optimise
	input_file = read(input_filename)

	#get starts and ends of loops and if blocks
	start_loop,end_loop,start_if,end_if = Parsing(input_file) 
	print(start_loop,end_loop,start_if,end_if)

	#code = performing unrolling or something 
	# write back into a new file! 
	#write(code, output_filename)

	#checking performance by executing files
	tic = time.time()
	execfile(input_filename)
	toc = time.time()
	print("Time taken BEFORE Loop Vectorization - "+ str(1000*(toc-tic))+"ms")

	tic = time.time()
	execfile(output_filename)
	toc = time.time()
	print("Time taken AFTER Loop Vectorization - "+ str(1000*(toc-tic))+"ms")

def main():
	choice = int(input("Enter \n1 for Loop Tilling \n2 for Loop Vectorization \n3 for Loop Unrolling"))
	if choice == 1:
		input_filename = "sample_inputs\sample_tiling.py"
		output_filename = "sample_outputs\output_loop_tiling.py"
		print("Performing Loop Tilling")
		til_loop(input_filename,output_filename)
	elif choice == 2:
		#vectorization
		input_filename = "sample_inputs\sample_vector.py"
		output_filename = "sample_outputs\output_loop_vectorization.py"
		vect(input_filename,output_filename)
		print("Performing vectorization")
	elif choice == 3:
		#Loop Unrolling
		input_filename = "sample_inputs\sample_unroll.py"
		output_filename = "sample_outputs\output_loop_unroll.py"
		print("Performing Loop Unrolling")








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

 
	

