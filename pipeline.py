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
                #convert address to binary
                pipeline[0] = ''.join(bin(int(i,16))[2:].zfill(4) for i in address)
            
            #ADD
            if pipeline[0][0:5] == 0b000000:
                print(pipeline[0][0:5])
                #HI
                
            #ADDI
            elif pipeline[0][0:5] == 0b000001:
                print(pipeline[0][0:5])
                
            #SUB
            elif pipeline[0][0:5] == 0b000010:
                print(pipeline[0][0:5])
                
            #SUBI
            elif pipeline[0][0:5] == 0b000011:
                print(pipeline[0][0:5])
                
            #MUL
            elif pipeline[0][0:5] == 0b000100:
                print(pipeline[0][0:5])
                
            #MULI
            elif pipeline[0][0:5] == 0b000101:
                print(pipeline[0][0:5])
                
            #OR
            elif pipeline[0][0:5] == 0b000110:
                print(pipeline[0][0:5])
                
            #ORI
            elif pipeline[0][0:5] == 0b000111:
                print(pipeline[0][0:5])
                
            #AND
            elif pipeline[0][0:5] == 0b001000:
                print(pipeline[0][0:5])
                
            #ANDI
            elif pipeline[0][0:5] == 0b001001:
                print(pipeline[0][0:5])
                
            #XOR
            elif pipeline[0][0:5] == 0b001010:
                print(pipeline[0][0:5])
                
            #XORI
            elif pipeline[0][0:5] == 0b001011:
                print(pipeline[0][0:5])
                
            #LDW
            elif pipeline[0][0:5] == 0b001100:
                print(pipeline[0][0:5])
                
            #STW
            elif pipeline[0][0:5] == 0b001101:
                print(pipeline[0][0:5])
                
            #BZ
            elif pipeline[0][0:5] == 0b001110:
                print(pipeline[0][0:5])
                
            #BEQ
            elif pipeline[0][0:5] == 0b001111:
                print(pipeline[0][0:5])
                
            #JR
            elif pipeline[0][0:5] == 0b010000:
                print(pipeline[0][0:5])
                
            #HALT
            elif pipeline[0][0:5] == 0b010001:
                print(pipeline[0][0:5])
                
            else:
                print("Invalid opcode entered for given command line: " + data)
                continue
                
        print("End of file reached")
        if input("Exit program? y/n\n") == 'y':
            break
        