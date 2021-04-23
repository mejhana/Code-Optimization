import matplotlib.pyplot as plt
#from subprocess import call
import numpy as np
import time 
import re 
import os

#Userdefined Functions
from Loop_Tiling import *

def read(filename):
	code = open(filename, "r").readlines()
	return code

def write(code, new_file_path):
	#write code into file 
	f = open(new_file_path, "w")
	code = "".join(code)
	f.write(code)
	f.close()


def perform_tiling(input_filename,output_filename, block_size):
	#removing comments! 
	code =  remove_comments(input_filename)
	write(code, input_filename)

	print("Performing Loop Tilling")
	#reading the file to optimise
	input_file = read(input_filename)

	#get starts and ends of loops and if blocks
	start_loop,end_loop,start_if,end_if = get_line_numbers(input_file) 
	print(start_loop,end_loop,start_if,end_if)

	# for loop tilling 
	code = perform_loop_tilling(input_file,start_loop,end_loop,start_if,end_if, block_size)
	# write back into a new file! 
	write(code, output_filename)
	
	#checking performance by executing files
	tic = time.time()
	#call(["python", "sample_tiling.py"])
	exec(open(input_filename).read())
	toc = time.time()
	time_before = toc - tic

	tic = time.time()
	#call(["python", "output_loop_tiling.py"])
	exec(open(output_filename).read())
	toc = time.time()
	time_after = toc - tic
	return time_before, time_after

def plotting(input_filename,output_filename):
	blocks = [10,20,30,40,50]
	times_before = []
	times_after = []
	for i in blocks:
		time_before, time_after = perform_tiling(input_filename,output_filename,i)
		times_before.append(time_before)
		times_after.append(time_after)

	plt.plot(times_before, blocks , label = "Execution Time Before Tiling")
	plt.plot(times_after, blocks , label ="Execution Time After Tiling")
	plt.xlabel('Time')
	plt.ylabel('Block Size')
	plt.title('Time vs Block size')
	plt.legend()
	plt.show()

def main():
	input_filename = "sample_tiling.py"
	output_filename = "output_loop_tiling.py"

	block_size = int(input("\nEnter Block Size - "))
	
	time_before, time_after = perform_tiling(input_filename,output_filename,block_size)

	print("\nTime taken BEFORE " + "Loop Tiling" +  "- "+ str(time_before)+ "\n")
	print("\nTime taken AFTER " + "Loop Tiling" +  "- "+ str(time_after)+ "\n")
	
	#plotting(input_filename,output_filename)
		
if __name__ == "__main__":
    main()
 
	

