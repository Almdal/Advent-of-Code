




def traverse(pattern, step_right, step_down):

    tree_count = 0
    right_index = 0

    for row_index in range(0,len(pattern),step_down): # Should iterate downwards
        row = pattern[row_index]
        
        #get the value first
        if row[right_index] == '#':
            tree_count += 1        

        right_index = (right_index + step_right) % (len(row)-1) # disregard endline character
    
    return tree_count




if __name__ == '__main__':
    pattern = open('input/3.txt').readlines()
    #pattern = open('input/3_test_full.txt').readlines()
    #pattern = open('input/3_test.txt').readlines()


    # Puzzle 1
    #print('Number of trees: ', traverse(pattern, 3, 1))


    # Puzzle 2
    product =  traverse(pattern, 1, 1)
    product *= traverse(pattern, 3, 1)
    product *= traverse(pattern, 5, 1)
    product *= traverse(pattern, 7, 1)
    product *= traverse(pattern, 1, 2)

    print ('Product is: ', product)
