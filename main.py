from past.builtins.misc import execfile
from shutil import copyfile
import numpy as np
import fileinput
import time 
import re 
import os

#Userdefined Functions

from loop_vectorization import *
from Deadcode_Removal import *
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
	sample_file = read(input_filename)

	#get starts and ends of loops and if blocks
	start_loop,end_loop,start_if,end_if = Parsing(sample_file) 
	print(start_loop,end_loop,start_if,end_if)

	# for loop tilling 
	code = perform_loop_tilling(sample_file,start_loop,end_loop,block_size)
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



def vect(input,output):
	print("Shruthi do this lol")
	# for loop vectorization
	a = np.random.rand(1000000)
	b = np.random.rand(1000000)

	tic = time.time()
	c = np.dot(a,b)
	toc = time.time()

	print(c)
	print("Vectorization version:"+ str(1000*(toc-tic))+"ms")


	c=0
	tic = time.time()
	for i in range(1000000):
		c+= a[i]*b[i]
	toc = time.time()

	print(c)
	print("for Loop:"+ str(1000*(toc-tic))+"ms")



def main():
	#choice = int(input("Enter \n0 for Deadcode elimination \n1 for Loop Tilling \n2 for Loop Vectorization \n3 for Loop Unrolling"))
	#input_filename = input("Enter your input file path with filename and extension")
	#output_filename = input("Enter your output file path with filename and extension")
	choice = 1
	if choice == 1:
		input_filename = "sample_code.py"
		output_filename = "after_loop_tiling.py"
		print("Performing Loop Tilling")
		til_loop(input_filename,output_filename)
	elif choice == 2:
		#vectorization
		vect(input_filename,output_filename)
		print("Performing vectorization")
	elif choice == 3:
		#Loop Unrolling
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

 
	

