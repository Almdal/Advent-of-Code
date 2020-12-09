def find_sum(data, result):
    found_result = False
    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
            if data[i] + data[j] == result and data[i] != data[j]:
                found_result = True

    return found_result


if __name__ == '__main__':
    input = [int(x) for x in open('input/9.txt').readlines()]
    #input = [int(x) for x in open('input/9_test.txt').readlines()]
    
    preamble_length = 25
    
    invalid = 0
    index = 0

    for i in range(preamble_length, len(input)):
        if not find_sum(input[i-preamble_length:i], input[i]):
            print ('Could not find result for ', input[i])
            invalid = input[i]
            index = i
            break
    

    found = False   
    numbers = []

    for i in range(0, index):
        res = input[i] 
        numbers = [input[i]]
        found = False
        
        for j in range(i+1, index):
            res += input[j]
            numbers.append(input[j])
            
            if res == invalid:
                found = True
                print(f'Found match at {i}, {j}, {numbers}')

                numbers.sort()
                print (f'min/max; {numbers[0]},{numbers[-1]}', numbers[0]+numbers[-1])
                break

            if res > invalid:
                break
        
        
        














