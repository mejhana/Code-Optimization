from past.builtins.misc import execfile
import numpy as np
import time 
import re 
import os

#Userdefined Functions
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

def check_performance(text,input_filename,output_filename):
	#checking performance by executing files
	tic = time.time()
	execfile(input_filename)
	toc = time.time()
	print("\nTime taken BEFORE " + text +  "- "+ str(1000*(toc-tic))+"ms\n")

	tic = time.time()
	execfile(output_filename)
	toc = time.time()
	print("\nTime taken AFTER " + text +  "- "+ str(1000*(toc-tic))+"ms\n")


def til_loop(input_filename,output_filename):
	block_size = int(input("\nEnter Block Size - "))
	tic = time.time()
	#reading the file to optimise
	input_file = read(input_filename)

	#get starts and ends of loops and if blocks
	start_loop,end_loop,start_if,end_if = Parsing(input_file) 
	print(start_loop,end_loop,start_if,end_if)

	# for loop tilling 
	code = perform_loop_tilling(input_file,start_loop,end_loop,block_size)
	# write back into a new file! 
	write(code, output_filename)

	toc =  time.time()
	print("\nTime taken to generate optimised code is- "+ str(1000*(toc-tic))+"ms\n")

	#check performance 
	text = "Loop Tiling"
	check_performance(text,input_filename,output_filename)

def main():
	input_filename = "sample_tiling.py"
	output_filename = "output_loop_tiling.py"
	#removing comments! 
	code =  remove_comments(input_filename)
	write(code, input_filename)
	print("Performing Loop Tilling")
	til_loop(input_filename,output_filename)
		
if __name__ == "__main__":
    main()

 
	

