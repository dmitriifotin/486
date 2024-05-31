while True:
    # file input
    file_input = input("Enter file name: ")
    # ask if forwarding or non-forwarding
    print_message = input("Select mode:\n1 - Functional Simulator only\n2 - Functional Simulator + non-forwarding Timing Simulator\n3 - Functional Simulator + forwarding Timing Simulator\n")
    while print_message not in {'1', '2', '3'}:
        print_message = input("Invalid Input! Select mode:\n1 - Functional Simulator only\n2 - Functional Simulator + non-forwarding Timing Simulator\n3 - Functional Simulator + forwarding Timing Simulator\n")
    
    # create a pipeline array
    pipeline = []
    stalls = 0
    cycles = 0
#<<<<<<< HEAD

    try:
        # open the specified file
        with open(file_input, 'r') as file:
            while True:
                # read file line by line
                data = file.readline().strip()
                # if file is empty, exit and ask for next file input
                if not data:
                    break
                
                # convert command to binary
                address = data.zfill(8)
                binary_command = ''.join(bin(int(char, 16))[2:].zfill(4) for char in address)
                pipeline.insert(0, binary_command)
                
                # Check commands
                opcode = int(pipeline[0][:6], 2)
                
#               -------------Josh's Portion-------------
                
                # ADD
                if opcode == 0b000000:
                    # Print the initial register contents
                    print("\nADD:", pipeline[0][:6])
                    rs = pipeline[0][6:11]
                    print("Source Register Contents (rs): ", rs)
                    rt = pipeline[0][11:16]
                    print("Source Register Contents (rt): ", rt)
                    rd = pipeline[0][16:21]
                    print("Destination Register Contents: ", rd)
                    # Convert to decimal to perform addition
                    rs_int = int(rs, 2)
                    rt_int = int(rt, 2)
                    rd_int = rs_int + rt_int

                    # Convert back to binary to display
                    rd = bin(rd_int)[2:].zfill(5)
                    print("Updated Destination Register Contents: ", rd)
                    
                # ADDI
                elif opcode == 0b000001:
                    # Print the initial register contents
                    print("\nADDI:", pipeline[0][:6])
                    rs = pipeline[0][6:11]
                    print("Source Register Contents (rs):", rs)
                    rt = pipeline[0][11:16]
                    print("Destination Register Contents:", rt)
                    imm = pipeline[0][16:]
                    print("Immediate Register Contents (imm):", imm)

                    # Convert to decimal to perform addition
                    rs_int = int(rs, 2)
                    imm_int = int(imm, 2)
                    rt_int = rs_int + imm_int

                    # Convert back to binary to display
                    rt = bin(rt_int)[2:].zfill(5)
                    print("Updated Destination Register Contents:", rt)
                    
                # SUB
                elif opcode == 0b000010:
                    # Print the initial register contents
                    print("\nSUB:", pipeline[0][:6])
                    rs = pipeline[0][6:11]
                    print("Source Register Contents (rs):", rs)
                    rt = pipeline[0][11:16]
                    print("Source Register Contents (rt):", rt)
                    rd = pipeline[0][16:21]
                    print("Destination Register Contents:", rd)

                    # Convert to decimal to perform subtraction
                    rs_int = int(rs, 2)
                    rt_int = int(rt, 2)
                    rd_int = rs_int - rt_int

                    # Convert back to binary to display
                    rd = bin(rd_int)[2:].zfill(5)
                    print("Updated Destination Register Contents:", rd)
                    
                # SUBI
                elif opcode == 0b000011:
                    # Print the initial register contents
                    print("\nSUBI:", pipeline[0][:6])
                    rs = pipeline[0][6:11]
                    print("Source Register Contents (rs):", rs)
                    rt = pipeline[0][11:16]
                    print("Destination Register Contents:", rt)
                    imm = pipeline[0][16:]
                    print("Immediate Register Contents (imm):", imm)

                    # Convert to decimal to perform addition
                    rs_int = int(rs, 2)
                    imm_int = int(imm, 2)
                    rt_int = rs_int - imm_int

                    # Convert back to binary to display
                    rt = bin(rt_int)[2:].zfill(5)
                    print("Updated Destination Register Contents:", rt)
                    
                # MUL
                elif opcode == 0b000100:
                	# Print the initial register contents
                    print("\nMUL:", pipeline[0][:6])
                    rs = pipeline[0][6:11]
                    print("Source Register Contents (rs):", rs)
                    rt = pipeline[0][11:16]
                    print("Source Register Contents (rt):", rt)
                    rd = pipeline[0][16:21]
                    print("Destination Register Contents:", rd)

                    # Convert to decimal to perform subtraction
                    rs_int = int(rs, 2)
                    rt_int = int(rt, 2)
                    rd_int = rs_int * rt_int

                    # Convert back to binary to display
                    rd = bin(rd_int)[2:].zfill(5)
                    print("Updated Destination Register Contents:", rd)
                    
                # MULI
                elif opcode == 0b000101:
                	# Print the initial register contents
                    print("\nMULI:", pipeline[0][:6])
                    rs = pipeline[0][6:11]
                    print("Source Register Contents (rs):", rs)
                    rt = pipeline[0][11:16]
                    print("Destination Register Contents:", rt)
                    imm = pipeline[0][16:]
                    print("Immediate Register Contents (imm):", imm)
                    
                    # Convert to decimal to perform addition
                    rs_int = int(rs, 2)
                    imm_int = int(imm, 2)
                    rt_int = rs_int * imm_int
                    
                    # Convert back to binary to display
                    rt = bin(rt_int)[2:].zfill(5)
                    print("Updated Destination Register Contents:", rt)
                    
#               ------------End Josh's Portion-------------
              
             
#               ------------John Michael's Portion-------------

                #OR
                elif opcode == 0b000110:
                    print("OR: " + pipeline[0][0:6])
                    #rs = 
                    print("Rt: " + pipeline[0][6:11] + f' (R{int(pipeline[0][6:11], 2)})')
                    #rt = 
                    print("Rs: " + pipeline[0][11:16] + f' (R{int(pipeline[0][11:16], 2)})')
                    #rd = 
                    print("Rd: " + pipeline[0][16:21] + f' (R{int(pipeline[0][16:21], 2)})')


                #ORI
                elif opcode == 0b000111:
                    print("ORi: " + pipeline[0][0:6])
                    #rs = 
                    print("Rt: " + pipeline[0][6:11] + f' (R{int(pipeline[0][6:11], 2)})')
                    #rt = 
                    print("Rs: " + pipeline[0][11:16] + f' (R{int(pipeline[0][11:16], 2)})')
                    #imm = int(pipeline[0][16:31], 2)
                    print("Imm: ", int(pipeline[0][16:31], 2))

                #AND
                elif opcode == 0b001000:
                    print("AND: " + pipeline[0][0:6])
                    #rs = 
                    print("Rt: " + pipeline[0][6:11] + f' (R{int(pipeline[0][6:11], 2)})')
                    #rt = 
                    print("Rs: " + pipeline[0][11:16] + f' (R{int(pipeline[0][11:16], 2)})')
                    #rd = 
                    print("Rd: " + pipeline[0][16:21] + f' (R{int(pipeline[0][16:21], 2)})')

                #ANDI
                elif opcode == 0b001001:
                    print("ANDi: " + pipeline[0][0:6])
                    #rs = 
                    print("Rt: " + pipeline[0][6:11] + f' (R{int(pipeline[0][6:11], 2)})')
                    #rt = 
                    print("Rs: " + pipeline[0][11:16] + f' (R{int(pipeline[0][11:16], 2)})')
                    #imm = int(pipeline[0][16:31], 2)
                    print("Imm: ", int(pipeline[0][16:31], 2))

                #XOR
                elif opcode == 0b001010:
                    print("XOR: " + pipeline[0][0:6])
                    #rs = 
                    print("Rt: " + pipeline[0][6:11] + f' (R{int(pipeline[0][6:11], 2)})')
                    #rt = 
                    print("Rs: " + pipeline[0][11:16] + f' (R{int(pipeline[0][11:16], 2)})')
                    #rd = 
                    print("Rd: " + pipeline[0][16:22] + f' (R{int(pipeline[0][16:21], 2)})')

                #XORI
                elif opcode == 0b001011:
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
	                


#               ------------End of John Michael's Portion-------------

                # LDW
                elif opcode == 0b001100:
                    print("LDW command found:", pipeline[0][:6])
                    
                # STW
                elif opcode == 0b001101:
                    print("STW command found:", pipeline[0][:6])
                    
                # BZ
                elif opcode == 0b001110:
                    print("BZ command found:", pipeline[0][:6])
                    
                # BEQ
                elif opcode == 0b001111:
                    print("BEQ command found:", pipeline[0][:6])
                    
                # JR
                elif opcode == 0b010000:
                    print("JR command found:", pipeline[0][:6])
                    
                # HALT
                elif opcode == 0b010001:
                    print("HALT command found:", pipeline[0][:6])
                    
                else:
                    print("Invalid opcode entered for given command line: " + data)
                    continue
                
            print("End of file reached")
            if input("Exit program? y/n\n") == 'y':
                break
    except FileNotFoundError:
        print("File not found. Please try again.")

