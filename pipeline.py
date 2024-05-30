# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:53:11 2024

@author: 
    Dmitrii Fotin       <dfotin@pdx.edu>
    John Michael Mertz  <jmertz@pdx.edu>  
    Josh Varughese       <jv23@pdx.edu>
"""

while True:
    
    #file input
    file_input = input("Enter file name: ")
    #ask if forwarding or non-forwarding
    print_message = input("Select mode:\n1 - Functional Simulator only\n2 - Functional Simulator + non-forwarding Timing Simulator\n3 - Functional Simulator + forwarding Timing Simulator")
    while print_message != '1' and print_message != '2' and print_message != '3':
        print_message = input("Invalid Input! Select mode:\n1 - Functional Simulator only\n2 - Functional Simulator + non-forwarding Timing Simulator\n3 - Functional Simulator + forwarding Timing Simulator") 
    
    #create a pipeline array
    pipeline = []
    stalls = 0
    cycles = 0
    
    
    #open the specified file
    with open(file_input, 'r') as file:
        while True:
            #read file line by line
            data = file.readline()
            #print("Address read: " + data)
            #if file is empty, exit and ask for next file input
            if not data:
                break
            #if last line in file reached, ask whether to exit the program
            #or enter next file name
            if data == "\n":
                print("Empty Line reached.")
                print("Continue? y/n")
                if input() == 'n':
                    break
                mode = None
            #for commands that are not 8 or 9, unpack line into command and hex address
            else:
                address = data.zfill(8)
                # replaces the newline at the end to empty
                address = address.replace("\n", "")
                print("Address Read: " + address) 
                pipeline.append("")
                
                #convert address to binary
                #for i in address:
                #    #print(i)
                #    j = bin(int(i,16))[2:].zfill(4)
                #    #print(j)
                #    pipeline[0] += j
                    
                pipeline[0] = ''.join(bin(int(i,16))[2:].zfill(4) for i in address)
                print("Address in binary: " + pipeline[0])
                
            #ADD
            if pipeline[0][0:6] == "000000":
            	print(pipeline[0][0:6])
                
            #ADDI
            elif pipeline[0][0:6] == "000001":
            	print(pipeline[0][0:6])
                
            #SUB
            elif pipeline[0][0:6] == "000010":
            	print(pipeline[0][0:6])
                
            #SUBI
            elif pipeline[0][0:6] == "000011":
            	print(pipeline[0][0:6])
                
            #MUL
            elif pipeline[0][0:6] == "000100":
            	print(pipeline[0][0:6])
                
            #MULI
            elif pipeline[0][0:6] == "000101":
            	print(pipeline[0][0:6])
            
            ###################



            #OR
            elif pipeline[0][0:6] == "000110":
            	
            	print("OR: " + pipeline[0][0:6])
            	#rs = 
            	print("Rt: " + pipeline[0][6:11] + f' (R{int(pipeline[0][6:11], 2)})')
            	#rt = 
            	print("Rs: " + pipeline[0][11:16] + f' (R{int(pipeline[0][11:16], 2)})')
            	#rd = 
            	print("Rd: " + pipeline[0][16:21] + f' (R{int(pipeline[0][16:21], 2)})')
 
            #ORI
            elif pipeline[0][0:6] == "000111":
            	print("ORi: " + pipeline[0][0:6])
            	#rs = 
            	print("Rt: " + pipeline[0][6:11] + f' (R{int(pipeline[0][6:11], 2)})')
            	#rt = 
            	print("Rs: " + pipeline[0][11:16] + f' (R{int(pipeline[0][11:16], 2)})')
            	#imm = int(pipeline[0][16:31], 2)
            	print("Imm: ", int(pipeline[0][16:31], 2))
                
            #AND
            elif pipeline[0][0:6] == "001000":
            	print("AND: " + pipeline[0][0:6])
            	#rs = 
            	print("Rt: " + pipeline[0][6:11] + f' (R{int(pipeline[0][6:11], 2)})')
            	#rt = 
            	print("Rs: " + pipeline[0][11:16] + f' (R{int(pipeline[0][11:16], 2)})')
            	#rd = 
            	print("Rd: " + pipeline[0][16:21] + f' (R{int(pipeline[0][16:21], 2)})')
                
            #ANDI
            elif pipeline[0][0:6] == "001001":
            	print("ANDi: " + pipeline[0][0:6])
            	#rs = 
            	print("Rt: " + pipeline[0][6:11] + f' (R{int(pipeline[0][6:11], 2)})')
            	#rt = 
            	print("Rs: " + pipeline[0][11:16] + f' (R{int(pipeline[0][11:16], 2)})')
            	#imm = int(pipeline[0][16:31], 2)
            	print("Imm: ", int(pipeline[0][16:31], 2))
                
            #XOR
            elif pipeline[0][0:6] == "001010":
            	print("XOR: " + pipeline[0][0:6])
            	#rs = 
            	print("Rt: " + pipeline[0][6:11] + f' (R{int(pipeline[0][6:11], 2)})')
            	#rt = 
            	print("Rs: " + pipeline[0][11:16] + f' (R{int(pipeline[0][11:16], 2)})')
            	#rd = 
            	print("Rd: " + pipeline[0][16:22] + f' (R{int(pipeline[0][16:21], 2)})')
                
            #XORI
            elif pipeline[0][0:6] == "001011":
            	print("XORi: " + pipeline[0][0:6])
            	#rs = 
            	print("Rt: " + pipeline[0][6:11] + f' (R{int(pipeline[0][6:11], 2)})')
            	#rt = 
            	print("Rs: " + pipeline[0][11:16] + f' (R{int(pipeline[0][11:16], 2)})')
            	#imm = int(pipeline[0][16:31], 2)
            	print("Imm: ", int(pipeline[0][16:31], 2))
            	
            	# Execution
            	# 1) Get Values from register
		# 2) Convert into integers (decimals) if needed
		# 3) Operate
		# 4) Store into register
            	
            


            #################

            #LDW
            elif pipeline[0][0:6] == "001100":
            	print(pipeline[0][0:6])
                
            #STW
            elif pipeline[0][0:6] == "001101":
            	print(pipeline[0][0:6])
                
            #BZ
            elif pipeline[0][0:6] == "001110":
            	print(pipeline[0][0:6])
                
            #BEQ
            elif pipeline[0][0:6] == "001111":
            	print(pipeline[0][0:6])
                
            #JR
            elif pipeline[0][0:6] == "010000":
            	print(pipeline[0][0:6]) 
            	
            #HALT
            elif pipeline[0][0:6] == "010001":
            	print(pipeline[0][0:6])
                
            else:
            	print(pipeline[0][0:6])
            	print("Invalid opcode entered for given command line: " + data)
            	continue
                
        print("End of file reached")
        #if input("Exit program? y/n\n") == 'y':
        #    break
        break
