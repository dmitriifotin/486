while True:
    # file input
    #file_input = input("Enter file name: ")
    # ask if forwarding or non-forwarding
    print_message = input("Select mode:\n1 - Functional Simulator only\n2 - Functional Simulator + non-forwarding Timing Simulator\n3 - Functional Simulator + forwarding Timing Simulator\n")
    while print_message not in {'1', '2', '3'}:
        print_message = input("Invalid Input! Select mode:\n1 - Functional Simulator only\n2 - Functional Simulator + non-forwarding Timing Simulator\n3 - Functional Simulator + forwarding Timing Simulator\n")
    
    # create a pipeline array
    pipeline = [0 for _ in range(5)]
    register = [0 for _ in range(32)]
    bit_length = 33
    stalls = 0
    cycles = 0
    
    def bin_to_int(val, bit_length):
        if val[0] == '0':
            print(int(val, 2))
            return int(val, 2)
        else:
            print(int(val, 2) - (1 << bit_length))
            return int(val, 2) - (1 << bit_length)
        
    def int_to_bin(number, bit_length):
        if number >= 0:
        # For non-negative numbers, format directly with leading zeros
            binary_str = format(number, f'0{bit_length}b')
        else:
        # For negative numbers, compute two's complement
        # Mask to ensure the binary number fits in the specified bit length
            mask = (1 << bit_length) - 1
            binary_str = format((number & mask), f'0{bit_length}b')
        return binary_str

    try:
        # open the specified file
        #with open(file_input, 'r') as file:
            while True:
                # read file line by line
                data = input().strip()
                #data = file.readline().strip()
                # if file is empty, exit and ask for next file input
                if not data:
                    break
                
                # convert command to binary
                address = data.zfill(8)
                print(address)
                pipeline[0] = ''.join(bin(int(char, 16))[2:].zfill(4) for char in address)
                
                # Check commands
                opcode = int(pipeline[0][:6], 2)
                
#               -------------Josh's Portion-------------
                
                # ADD
                if opcode == 0b000000:
                	# Print the initial register contents
                    print("\nADD:", opcode)
                    rs = int(pipeline[0][6:11], 2)
                    print("Source Register (rs): ", rs)
                    rt = int(pipeline[0][11:16], 2)
                    print("Source Register (rt): ", rt)
                    rd = int(pipeline[0][16:21], 2)
                    print("Destination Register: ", rd)
                    
                    register[rs] = '0001'
                    register[rt] = '111111111111111111111111111111101'
                    
                    # Convert to decimal to perform addition
                    register[rd] = int_to_bin(bin_to_int(register[rs], bit_length) + bin_to_int(register[rt], bit_length), bit_length)
                    
                    print("Updated Destination Register Contents: ", bin_to_int(register[rd], bit_length))
                    
                # ADDI
                elif opcode == 0b000001:
                	# Print the initial register contents
                    print("\nADDI:", opcode)
                    rs = int(pipeline[0][6:11], 2)
                    print("Source Register (rs): ", rs)
                    rt = int(pipeline[0][11:16], 2)
                    print("Source Register (rt): ", rt)
                    imm = bin_to_int(pipeline[0][16:])
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
                    print("\nSUB:", opcode)
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
                    print("\nSUBI:", opcode)
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
                    print("\nMUL:", opcode)
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
                    print("\nMULI:", opcode)
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
              
                # OR
                elif opcode == 0b000110:
                    print("OR command found:", opcode)
                    
                # ORI
                elif opcode == 0b000111:
                    print("ORI command found:", opcode)
                    
                # AND
                elif opcode == 0b001000:
                    print("AND command found:", opcode)
                    
                # ANDI
                elif opcode == 0b001001:
                    print("ANDI command found:", opcode)
                    
                # XOR
                elif opcode == 0b001010:
                    print("XOR command found:", opcode)
                    
                # XORI
                elif opcode == 0b001011:
                    print("XORI command found:", opcode)
                    
                # LDW
                elif opcode == 0b001100:
                    print("LDW command found:", opcode)
                    
                    
                # STW
                elif opcode == 0b001101:
                    print("STW command found:", opcode)
                    
                # BZ
                elif opcode == 0b001110:
                    print("BZ command found:", opcode)
                    
                # BEQ
                elif opcode == 0b001111:
                    print("BEQ command found:", opcode)
                    
                # JR
                elif opcode == 0b010000:
                    print("JR command found:", opcode)
                    
                # HALT
                elif opcode == 0b010001:
                    print("HALT command found:", opcode)
                    
                else:
                    print("Invalid opcode entered for given command line: " + data)
                    continue
                
            print("End of file reached")
            if input("Exit program? y/n\n") == 'y':
                break
    except FileNotFoundError:
        print("File not found. Please try again.")