test_set = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''


def check_password(password, character, occurance_min, occurance_max):
    cnt = password.count(character)
    
    if cnt >= occurance_min and cnt <= occurance_max:
        return True
    return False

def check_password_position(password, character, occurance_min, occurance_max):
    
    if int(password[occurance_min-1] == character) ^ int(password[occurance_max - 1] == character):
        return True
    return False



if __name__ == '__main__':
    passwords = open('input/2.txt').readlines()
    #passwords = test_set.split('\n')
    #print (passwords)
    
    valid = 0
    valid_position = 0
    for password in passwords:
        cond, pwd = password.split(':')

        pwd = pwd.strip()
        bound, character = cond.split()
        bound_low = int(bound.split('-')[0])
        bound_high = int(bound.split('-')[1])
        

        """ if check_password(pwd, character, bound_low, bound_high) == True:
            print ('Valid password: ', pwd)
            valid += 1
 """
        if check_password_position(pwd, character, bound_low, bound_high) == True:
            print ('Valid password: ', pwd)
            valid_position += 1

    print ('Valid passwords: ', valid)
    print ('Valid passwords with position: ', valid_position)
