



if __name__ == '__main__':
    print ('ok')
    expenses = [int(x) for x in open('input/1.txt').readlines()]

    for i in range(1, len(expenses)):
        for j in range(i+1,len(expenses)):
            if expenses[i] + expenses[j] == 2020:
                print('Product at ' + str(i) + '/' + str(j) + ' is ', expenses[i]*expenses[j])



    for i in range(1, len(expenses)):
        for j in range(i+1,len(expenses)):
            for k in range(j+1,len(expenses)):
                if expenses[i] + expenses[j] + expenses[k] == 2020:
                    print('Product at ' + str(i) + '/' + str(j) + '/' + str(k) + ' is ', expenses[i]*expenses[j]*expenses[k])
    
    



