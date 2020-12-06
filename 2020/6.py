

def p1(q):
    qq = q.replace('\n','')
        
    ch = []
    for c in qq:
        if c not in ch:
            ch.append(c)

    
    return len(ch)

def p2(q):

    lines = q.split('\n')

    if len(lines) == 1:
        return p1(q)

    if lines[-1] == '':
        lines = lines[:-1]

    #iterate over lines
    no = 0
    for character in list(lines[0]):
        match_count = 0
        for line in lines[1:]:
            if character in line:
                match_count += 1
            else:
                break
        
        if match_count == len(lines[1:]):
            no += 1
    
    return no

if __name__ == '__main__':
    input = open('input/6.txt').read()
   #input = open('input/6_test.txt').read()


    questions = input.split('\n\n')

    no = 0
    for q in questions:
        #no += p1(q) # problem 1
        no += p2(q) # problem 2
        
    print(no)

