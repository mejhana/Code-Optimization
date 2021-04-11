from Parser import *
from Deadcode_Removal import *
from Loop_Tilling import *
from Loop_Unrolling import *
from Code_Motion import *

def main():
	block_size = 2
	#filename = input("Enter your file path with filename and extension")
	filename = "sample_code.py"
	file = open(filename, "r").readlines()
	#get starts and ends of loops and also run code for deadcode! 
	loop = ["for", "while"]
	ifs = ["if", "elif" ,"else"]
	start_loop,end_loop,start_if,end_if = Parsing(file,loop,ifs) 
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
	#for loop unrolling
	Line = "array(i+1, k-2) = array(i+0, k-2) + array(i+1, k-2) - array(i+3, k-256877845);"
        print(unroll(unroll(Line, "k", 4), "i", 3, False))

if __name__ == "__main__":
    main()

 
	

