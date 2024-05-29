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
            print(data)
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
                print("Address Read: " + address) 
                address = address.replace("\n", "")
                pipeline.append("")
                
                #convert address to binary
                for i in address:
                    #print(i)
                    j = bin(int(i,16))[2:].zfill(4)
                    #print(j)
                    pipeline[-1] += j
                    
                print("Address in binary: " + pipeline[-1])
                #pipeline[0] = ''.join(bin(int(i,16))[2:].zfill(4) for i in address)
            
            #ADD
            if pipeline[-1][0:6] == "000000":
            	print(pipeline[-1][0:6])
                
            #ADDI
            elif pipeline[-1][0:6] == "000001":
            	print(pipeline[-1][0:6])
                
            #SUB
            elif pipeline[-1][0:6] == "000010":
            	print(pipeline[-1][0:6])
                
            #SUBI
            elif pipeline[-1][0:6] == "000011":
            	print(pipeline[-1][0:6])
                
            #MUL
            elif pipeline[-1][0:6] == "000100":
            	print(pipeline[-1][0:6])
                
            #MULI
            elif pipeline[-1][0:6] == "000101":
            	print(pipeline[-1][0:6])
            
            ###################



            #OR
            elif pipeline[-1][0:6] == "000110":
            	print(pipeline[-1][0:6])

                
            #ORI
            elif pipeline[-1][0:6] == "000111":
            	print(pipeline[-1][0:6])
                
            #AND
            elif pipeline[-1][0:6] == "001000":
            	print(pipeline[-1][0:6])
                
            #ANDI
            elif pipeline[-1][0:6] == "001001":
            	print(pipeline[-1][0:6])
                
            #XOR
            elif pipeline[-1][0:6] == "001010":
            	print(pipeline[-1][0:6])
                
            #XORI
            elif pipeline[-1][0:6] == "001011":
            	print(pipeline[-1][0:6])
            


            #################

            #LDW
            elif pipeline[-1][0:6] == "001100":
            	print(pipeline[-1][0:6])
                
            #STW
            elif pipeline[-1][0:6] == "001101":
            	print(pipeline[-1][0:6])
                
            #BZ
            elif pipeline[-1][0:6] == "001110":
            	print(pipeline[-1][0:6])
                
            #BEQ
            elif pipeline[-1][0:6] == "001111":
            	print(pipeline[-1][0:6])
                
            #JR
            elif pipeline[-1][0:6] == "010000":
            	print(pipeline[-1][0:6]) 
            	
            #HALT
            elif pipeline[-1][0:6] == "010001":
            	print(pipeline[-1][0:6])
                
            else:
            	print(pipeline[-1][0:6])
            	print("Invalid opcode entered for given command line: " + data)
            	continue
                
        print("End of file reached")
        #if input("Exit program? y/n\n") == 'y':
        #    break
        break
