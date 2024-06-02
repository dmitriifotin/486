def bin_to_int(val, bit_length):
    if val[0] == '0':
        return int(val, 2)
    else:
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

def shift(pipeline, writ_reg):
    pipeline[4] = pipeline[3]
    pipeline[3] = pipeline[2]
    pipeline[2] = pipeline[1]
    pipeline[1] = pipeline[0]
    writ_reg[4] = writ_reg[3]
    writ_reg[3] = writ_reg[2]
    writ_reg[2] = writ_reg[1]
    writ_reg[1] = writ_reg[0]
    #print(pipeline)
    #print(writ_reg)
    
def check_gap(rs, rt, writ_reg, pipeline, print_message):
    for i in writ_reg:
        if i == rs or i == rt:
            gap = writ_reg.index(i)
            if print_message == '2' and gap < 3 and gap != 0:
                gap = 3 - gap
                
            if print_message == '3':
                if int(pipeline[writ_reg.index(i)][:6], 2) == 12:
                    gap = 1
                else:
                    gap = 0
            if gap == 3 or gap == 4:
                gap = 0
            
            print ("GAP: ", gap)
            return gap

while True:
    # file input
    file_input = input("Enter file name: ")
    # ask if forwarding or non-forwarding
    print_message = input("Select mode:\n1 - Functional Simulator only\n2 - Functional Simulator + non-forwarding Timing Simulator\n3 - Functional Simulator + forwarding Timing Simulator\n")
    while print_message not in {'1', '2', '3'}:
        print_message = input("Invalid Input! Select mode:\n1 - Functional Simulator only\n2 - Functional Simulator + non-forwarding Timing Simulator\n3 - Functional Simulator + forwarding Timing Simulator\n")
    
    # create a pipeline array
    pipeline = ['0' for _ in range(5)]
    register = ['0' for _ in range(32)]
    writ_reg = [-1 for _ in range(5)]
    pipeline_index = 0
    bit_length = 32
    opcode_bit_length = 6
    stalls = 0
    cycles = 0
    data = ['0' for _ in range(1025)]
    ins_index = 0
    pc = 0
    arith_cnt = 0
    log_cnt = 0
    mem_cnt = 0
    ctrl_cnt = 0
    exit = 0

    try:
        # open the specified file
        with open(file_input, 'r') as file:
            while not exit:
                #read file line by line
                while True:
                    data[ins_index] = file.readline().strip().replace("\n", "")
                    if not data[ins_index]:
                        break
                    ins_index += 1

                # if file is empty, exit and ask for next file input
                
                # convert command to binary
                address = data[pc//4].zfill(8)
                print(address, end=' ')
                pipeline[0] = ''.join(bin(int(char, 16))[2:].zfill(4) for char in address)
                # Check commands
                opcode = int(pipeline[0][:6], 2)
                print("STALLS: ", stalls)
                pc += 4
                
                # ADD
                if opcode == 0b000000:
                	# Print the initial register contents
                    print("ADD:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    
                    rs = int(pipeline[0][6:11], 2)
                    rt = int(pipeline[0][11:16], 2)
                    rd = int(pipeline[0][16:21], 2)
                    writ_reg[0] = rd
                    if rs in writ_reg or rt in writ_reg:
                        gap = check_gap(rs, rt, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                    
                    print("RS ", rs, bin_to_int(register[rs], bit_length), " RT ", rt, bin_to_int(register[rt], bit_length), " RD ", rd, bin_to_int(register[rd], bit_length))
                    
                    # Convert to decimal to perform addition
                    register[rd] = int_to_bin(bin_to_int(register[rs], bit_length) + bin_to_int(register[rt], bit_length), bit_length)
                    
                    print("Updated Destination Register Contents: ", bin_to_int(register[rd], bit_length))
                    shift(pipeline, writ_reg)
                    cycles += 1
                    arith_cnt += 1
                    
                # ADDI
                elif opcode == 0b000001:
                	# Print the initial register contents
                    print("ADDI:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    rs = int(pipeline[0][6:11], 2)
                    rt = int(pipeline[0][11:16], 2)
                    imm = bin_to_int(pipeline[0][16:], bit_length)
                    writ_reg[0] = rt
                    if rs in writ_reg:
                        gap = check_gap(rs, 0, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                    
                    print("RS ", rs, bin_to_int(register[rs], bit_length), " RT ", rt, bin_to_int(register[rt], bit_length), " Imm ", imm)

                    # Convert to decimal to perform addition
                    register[rt] = int_to_bin(bin_to_int(register[rs], bit_length) + imm, bit_length)

                    # Convert back to binary to display
                    print("Updated Destination Register Contents:", bin_to_int(register[rt], bit_length))
                    shift(pipeline, writ_reg)
                    cycles += 1
                    arith_cnt += 1
                    
                # SUB
                elif opcode == 0b000010:
                	# Print the initial register contents
                    print("SUB:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    rs = int(pipeline[0][6:11], 2)
                    rt = int(pipeline[0][11:16], 2)
                    rd = int(pipeline[0][16:21], 2)
                    
                    writ_reg[0] = rd
                    if rs in writ_reg or rt in writ_reg:
                        gap = check_gap(rs, rt, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                            
                    print("RS ", rs, bin_to_int(register[rs], bit_length), " RT ", rt, bin_to_int(register[rt], bit_length), " RD ", rd, bin_to_int(register[rd], bit_length))

                    # Convert to decimal to perform subtraction
                    register[rd] = int_to_bin(bin_to_int(register[rs], bit_length) - bin_to_int(register[rt], bit_length), bit_length)
                    
                    # Convert back to binary to display
                    
                    print("Updated Destination Register Contents:", bin_to_int(register[rd], bit_length))
                    shift(pipeline, writ_reg)
                    cycles += 1
                    arith_cnt += 1
                    
                # SUBI
                elif opcode == 0b000011:
                	# Print the initial register contents
                    print("SUBI:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    rs = int(pipeline[0][6:11], 2)
                    rt = int(pipeline[0][11:16], 2)
                    imm = bin_to_int(pipeline[0][16:], bit_length)
                    writ_reg[0] = rt
                    if rs in writ_reg:
                        gap = check_gap(rs, 0, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                    
                    print("RS ", rs, bin_to_int(register[rs], bit_length), " RT ", rt, bin_to_int(register[rt], bit_length), " Imm ", imm)

                    # Convert to decimal to perform addition
                    register[rt] = int_to_bin(bin_to_int(register[rs], bit_length) - imm, bit_length)
                    
                    # Convert back to binary to display
                    print("Updated Destination Register Contents:", bin_to_int(register[rt], bit_length))
                    shift(pipeline, writ_reg)
                    cycles += 1
                    arith_cnt += 1
                    
                # MUL
                elif opcode == 0b000100:
                	# Print the initial register contents
                    print("MUL:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    rs = int(pipeline[0][6:11], 2)
                    rt = int(pipeline[0][11:16], 2)
                    rd = int(pipeline[0][16:21], 2)
                    writ_reg[0] = rd
                    if rs in writ_reg or rt in writ_reg:
                        gap = check_gap(rs, rt, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                    
                    print("RS ", rs, bin_to_int(register[rs], bit_length), " RT ", rt, bin_to_int(register[rt], bit_length), " RD ", rd, bin_to_int(register[rd], bit_length))

                    # Convert to decimal to perform subtraction
                    register[rd] = int_to_bin(bin_to_int(register[rs], bit_length) * bin_to_int(register[rt], bit_length), bit_length)
                    
                    # Convert back to binary to display
                    print("Updated Destination Register Contents:", bin_to_int(register[rd], bit_length))
                    shift(pipeline, writ_reg)
                    cycles += 1
                    arith_cnt += 1
                    
                # MULI
                elif opcode == 0b000101:
                	# Print the initial register contents
                    print("MULI:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    rs = int(pipeline[0][6:11], 2)
                    rt = int(pipeline[0][11:16], 2)
                    imm = bin_to_int(pipeline[0][16:], bit_length)
                    writ_reg[0] = rt
                    if rs in writ_reg:
                        gap = check_gap(rs, 0, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                    
                    print("RS ", rs, bin_to_int(register[rs], bit_length), " RT ", rt, bin_to_int(register[rt], bit_length), " Imm ", imm)

                    # Convert to decimal to perform addition
                    register[rt] = int_to_bin(bin_to_int(register[rs], bit_length) * imm, bit_length)
                    
                    # Convert back to binary to display
                    print("Updated Destination Register Contents:", bin_to_int(register[rt], bit_length))
                    shift(pipeline, writ_reg)
                    cycles += 1
                    arith_cnt += 1
                    
                # OR
                elif opcode == 0b000110:
                    # Print the initial register contents
                    print("OR:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    rs = int(pipeline[0][6:11], 2)
                    rt = int(pipeline[0][11:16], 2)
                    rd = int(pipeline[0][16:21], 2)
                    writ_reg[0] = rd
                    if rs in writ_reg or rt in writ_reg:
                        gap = check_gap(rs, rt, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                    
                    print("RS ", rs, register[rs], " RT ", rt, register[rt], " RD ", rd, register[rd])

                    register[rd] = int_to_bin(bin_to_int(register[rs], bit_length) | bin_to_int(register[rt], bit_length), bit_length)
                    
                    print("Updated Destination Register Contents:", bin_to_int(register[rd], bit_length))
                    shift(pipeline, writ_reg)
                    cycles += 1
                    log_cnt += 1
                    
                # ORI
                elif opcode == 0b000111:
                    print("ORI:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    rs = int(pipeline[0][6:11], 2)
                    rt = int(pipeline[0][11:16], 2)
                    imm = bin_to_int(pipeline[0][16:], bit_length)
                    writ_reg[0] = rt
                    if rs in writ_reg:
                        gap = check_gap(rs, 0, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                    
                    print("RS ", rs, register[rs], " RT ", rt, register[rt], " Imm ", imm)

                    # Convert to decimal to perform addition
                    register[rt] = int_to_bin(bin_to_int(register[rs], bit_length) | imm, bit_length)
                    
                    # Convert back to binary to display
                    print("Updated Destination Register Contents:", bin_to_int(register[rt], bit_length))
                    shift(pipeline, writ_reg)
                    cycles += 1
                    log_cnt += 1
                    
                # AND
                elif opcode == 0b001000:
                    # Print the initial register contents
                    print("AND:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    rs = int(pipeline[0][6:11], 2)
                    rt = int(pipeline[0][11:16], 2)
                    rd = int(pipeline[0][16:21], 2)
                    writ_reg[0] = rd
                    if rs in writ_reg or rt in writ_reg:
                        gap = check_gap(rs, rt, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                    
                    print("RS ", rs, register[rs], " RT ", rt, register[rt], " RD ", rd, register[rd])

                    register[rd] = int_to_bin(bin_to_int(register[rs], bit_length) & bin_to_int(register[rt], bit_length), bit_length)
                    
                    print("Updated Destination Register Contents:", bin_to_int(register[rd], bit_length))
                    shift(pipeline, writ_reg)
                    cycles += 1
                    log_cnt += 1
                    
                # ANDI
                elif opcode == 0b001001:
                    print("ANDI:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    rs = int(pipeline[0][6:11], 2)
                    rt = int(pipeline[0][11:16], 2)
                    imm = bin_to_int(pipeline[0][16:], bit_length)
                    writ_reg[0] = rt
                    if rs in writ_reg:
                        gap = check_gap(rs, 0, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                    
                    print("RS ", rs, register[rs], " RT ", rt, register[rt], " Imm ", imm)

                    # Convert to decimal to perform addition
                    register[rt] = int_to_bin(bin_to_int(register[rs], bit_length) & imm, bit_length)
                    
                    # Convert back to binary to display
                    print("Updated Destination Register Contents:", bin_to_int(register[rt], bit_length))
                    shift(pipeline, writ_reg)
                    cycles += 1
                    log_cnt += 1
                    
                # XOR
                elif opcode == 0b001010:
                    # Print the initial register contents
                    print("XOR:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    rs = int(pipeline[0][6:11], 2)
                    rt = int(pipeline[0][11:16], 2)
                    rd = int(pipeline[0][16:21], 2)
                    writ_reg[0] = rd
                    if rs in writ_reg or rt in writ_reg:
                        gap = check_gap(rs, rt, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                    
                    print("RS ", rs, register[rs], " RT ", rt, register[rt], " RD ", rd, register[rd])

                    register[rd] = int_to_bin(bin_to_int(register[rs], bit_length) ^ bin_to_int(register[rt], bit_length), bit_length)
                    
                    print("Updated Destination Register Contents:", bin_to_int(register[rd], bit_length))
                    shift(pipeline, writ_reg)
                    cycles += 1
                    log_cnt += 1
                    
                # XORI
                elif opcode == 0b001011:
                    print("XORI:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    rs = int(pipeline[0][6:11], 2)
                    rt = int(pipeline[0][11:16], 2)
                    imm = bin_to_int(pipeline[0][16:], bit_length)
                    writ_reg[0] = rt
                    if rs in writ_reg:
                        gap = check_gap(rs, 0, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                    
                    print("RS ", rs, register[rs], " RT ", rt, register[rt], " Imm ", imm)

                    # Convert to decimal to perform addition
                    register[rt] = int_to_bin(bin_to_int(register[rs], bit_length) ^ imm, bit_length)
                    
                    # Convert back to binary to display
                    print("Updated Destination Register Contents:", bin_to_int(register[rt], bit_length))
                    shift(pipeline, writ_reg)
                    cycles += 1
                    log_cnt += 1
                    
                # LDW
                elif opcode == 0b001100:
                    print("LDW:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    
                    rs = int(pipeline[0][6:11], 2)
                    rt = int(pipeline[0][11:16], 2)
                    imm = bin_to_int(pipeline[0][16:], bit_length)
                    
                    address = data[(bin_to_int(register[rs], bit_length) + imm)//4].zfill(8)
                    register[rt] = ''.join(bin(int(char, 16))[2:].zfill(4) for char in address)
                    
                    writ_reg[0] = rt
                    if rs in writ_reg:
                        gap = check_gap(rs, 0, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                    
                    print("RS ", rs, bin_to_int(register[rs], bit_length), " RT ", rt, bin_to_int(register[rt], bit_length), " Imm ", imm)
                    print("Updated Destination Register Contents:", bin_to_int(register[rt], bit_length))
                    shift(pipeline, writ_reg)
                    cycles += 1
                    mem_cnt += 1
                    
                # STW
                elif opcode == 0b001101:
                    print("STW:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    
                    rs = int(pipeline[0][6:11], 2)
                    rt = int(pipeline[0][11:16], 2)
                    imm = bin_to_int(pipeline[0][16:], bit_length)
                    
                    data[(bin_to_int(register[rs], bit_length) + imm)//4] = str(hex(bin_to_int(register[rt], bit_length)))
                    
                    writ_reg[0] = rt
                    if rs in writ_reg:
                        gap = check_gap(rs, 0, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                    
                    print("RS ", rs, bin_to_int(register[rs], bit_length), " RT ", rt, bin_to_int(register[rt], bit_length), " Imm ", imm)
                    print("Updated Destination Register Contents:", data[(bin_to_int(register[rs], bit_length) + imm)//4])
                    shift(pipeline, writ_reg)
                    cycles += 1
                    mem_cnt += 1
                    
                # BZ
                elif opcode == 0b001110:
                    print("BZ:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    
                    rs = int(pipeline[0][6:11], 2)
                    imm = bin_to_int(pipeline[0][16:], bit_length)
                    print("RS ", rs, bin_to_int(register[rs], bit_length), " Imm ", imm)
                    
                    writ_reg[0] = -1
                    if rs in writ_reg:
                        gap = check_gap(rs, 0, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                        
                    if register[rs] == int_to_bin(0, bit_length):
                        pc += (imm - 1) * 4
                        print("Going to instruction: ", data[pc//4], " on line: ", pc//4)
                        cycles += 2
                        
                    else:
                        print("Proceeding without branching\n")
                    shift(pipeline, writ_reg)
                    shift(pipeline, writ_reg)
                    shift(pipeline, writ_reg)
                    cycles += 1
                    ctrl_cnt += 1
                    
                # BEQ
                elif opcode == 0b001111:
                    print("BEQ:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    
                    rs = int(pipeline[0][6:11], 2)
                    rt = int(pipeline[0][11:16], 2)
                    imm = bin_to_int(pipeline[0][16:], bit_length) - 1
                    print("RS ", rs, bin_to_int(register[rs], bit_length), " RT ", rt, bin_to_int(register[rt], bit_length), " Imm ", imm)
                    
                    writ_reg[0] = -1
                    if rt in writ_reg or rs in writ_reg:
                        gap = check_gap(rs, rt, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                    
                    if register[rs] == register[rt]:
                        pc += imm * 4
                        print("Going to instruction: ", data[pc//4], " on line: ", pc//4)
                        cycles += 2
                    else:
                        print("Proceeding without branching\n")
                    shift(pipeline, writ_reg)
                    shift(pipeline, writ_reg)
                    shift(pipeline, writ_reg)
                    cycles += 1
                    ctrl_cnt += 1
                    
                # JR
                elif opcode == 0b010000:
                    print("JR:", int_to_bin(opcode, opcode_bit_length), end=' ')
                    
                    rs = int(pipeline[0][6:11], 2)
                    print("Source Register (rs): ", rs, bin_to_int(register[rs], bit_length))
                    
                    writ_reg[0] = -1
                    if rs in writ_reg:
                        gap = check_gap(rs, 0, writ_reg, pipeline, print_message)
                        print("Dependency: ", gap)
                        stalls += gap
                        cycles += gap
                    
                    pc = bin_to_int(register[rs], bit_length)
                    
                    print("Going to instruction: ", data[pc//4], " on line: ", pc//4)
                    shift(pipeline, writ_reg)
                    shift(pipeline, writ_reg)
                    shift(pipeline, writ_reg)
                    #stalls += 2
                    cycles += 3
                    ctrl_cnt += 1
                    
                # HALT
                elif opcode == 0b010001:
                    print("HALT:", int_to_bin(opcode, opcode_bit_length), "\nProgram halted\n\n")
                    exit = 1
                    cycles += 5
                    ctrl_cnt += 1
                    print("Cycles: ", cycles, " Stalls: ", stalls)
                    
                else:
                    print("Invalid opcode entered for given command line: " + data)
                    continue
            
            total_instr = arith_cnt + log_cnt + mem_cnt + ctrl_cnt
        
            print("Instruction counts:")
            print("\nTotal number of instructions: ", total_instr)
            print("Arithmetic instructions: ", arith_cnt)
            print("Logical Instructions: ", log_cnt)
            print("Memory access instructions: ", mem_cnt)
            print("Control transfer instructions: ", ctrl_cnt)
            print("\nFinal Register State:\n")
            print("Program Counter: ", pc)
#            print(register)
            i = 0
            for reg in register:
                if reg != '0':
                    print(f'R{i} :', bin_to_int(reg, bit_length))
                i += 1
            print("Total Stalls: ", stalls)
            i = 0
            for d in data:
                if d.startswith('0x'):
                    print("Address:", i*4, ",Contents:",int(d,16))
                i += 1
            print("\nTiming Simulator:\n")
            print("Total number of clock cycles: ", cycles)
            print("\nProgram halted\n\n")
          #  print(data)
            
            print("End of file reached")
            if input("Exit program? y/n\n") == 'y':
                break
    except FileNotFoundError:
        print("File not found. Please try again.")