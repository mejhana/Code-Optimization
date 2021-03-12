def return_condition(word,line):
	for word in line.split():
		if word == "if":





def scanning(filename):
	file = open(filename, 'r')    
    for line in file: 
   
        # reading each word         
        for word in line.split(): 

            # displaying the words            
            print(word) 

	    	#check for if, elif, while, for, do..while, etc
	    	#call a program to return the conditions example if(a==b), the condition returned is a==b
	    	#call another function that determines whether the conditions in these statements ever become true, 
	    	#if they do ignore, if not mark that line as deadcode
	    	key_words = ["if" , "elif", "while", "for"]
	    	if word in keywords:
	    		dead_code_flag = return_condition(word,line)

	file.close() 