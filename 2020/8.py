


def assemble():
    pass



def accval(input):

    mod = 1
    if input[0] == '-':
        mod = -1
    return int(input[1:])*mod


if __name__ == '__main__':
    codes = open('input/8_test.txt').readlines()
    codes = open('input/8.txt').readlines()
    
    accumulator = 0
    pc = 0 # program counter

    ## Problem 1
    """ executed_instructions = []

    while True:

        instruction, value = codes[pc].split()

        if pc in executed_instructions:
            print(f'We\'ve reached an already executed instruction {pc}: {instruction}/{value}. Terminating')

            break
        else:
            print(f'Executing instruction {instruction}/{value}, PC {pc}, acc {accumulator}')
            executed_instructions.append(pc)

        if   instruction == 'acc':
            accumulator += accval(value)
            pc += 1
            continue
        
        elif instruction == 'nop':
            pc += 1
            continue
        
        elif instruction == 'jmp':
            pc += accval(value)
            continue
 """


    # problem 2 - brute forcing 
    nj_index = []

    for i in range(0, len(codes)):
        if codes[i][0:3] in ['jmp','nop']:
            nj_index.append(i)
        
    #print(nj_index)

    found_termination = False

    for attempt in nj_index:
        
        if found_termination == True:
            print(f'Skipping the rest of the execution {accumulator}')
            break
        mod_codes = codes.copy()
        
        #print(f'Trying to switch instruction at {attempt}: {mod_codes[attempt]}')


        #Try to switch one instruction
        if mod_codes[attempt][0:3]  == 'nop':
            mod_codes[attempt] = mod_codes[attempt].replace('nop','jmp')
        else:
            mod_codes[attempt] = mod_codes[attempt].replace('jmp','nop')

        pc = 0
        executed_instructions = []
        accumulator = 0

        while True:
            
            if pc == len(codes):
                print(f'We\'ve reaced the end of the instruction set {pc}. Yay!')
                found_termination = True
                break

            instruction, value = mod_codes[pc].split()

            if pc in executed_instructions:
                print(f'We\'ve reached an already executed instruction @attempt {attempt} - {pc}: {instruction}/{value}. Terminating')
                break
            else:
                #print(f'Executing instruction {instruction}/{value}, PC {pc}, acc {accumulator}')
                executed_instructions.append(pc)

            if   instruction == 'acc':
                accumulator += accval(value)
                pc += 1
                continue
            
            elif instruction == 'nop':
                pc += 1
                continue
            
            elif instruction == 'jmp':
                pc += accval(value)
                continue
                
    print(f'accumulator is {accumulator}')
    