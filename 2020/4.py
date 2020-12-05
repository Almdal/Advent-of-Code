
import re


fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
extra_fields = ['cid']

ecl_valid = ['amb', 'blu', 'brn','gry', 'grn', 'hzl', 'oth']

hcl_regex = re.compile('(#[a-f0-9]{6})')
pid_regex = re.compile('\d{9}')
unit_regex = re.compile('(cm|in)')

def validate_ecl(entry) -> bool:
    helper = ' ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.'
    if entry not in ecl_valid:
        print('ecl invalid ' + entry + helper)
        return False
    return True

def validate_pid(entry) -> bool:
    helper = ' pid (Passport ID) - a nine-digit number, including leading zeroes'
    if len(entry) != 9:
        print('pid too short ' + entry + helper)
        return False
    
    if pid_regex.match(entry) == None:
        print('pid invalid ' + entry + helper)
        return False

    return True

def validate_hcl(entry) -> bool:

    helper = ' hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.'
    if hcl_regex.match(entry) == None:
        print('hcl invalid ' + entry +  helper)
        return False

    return True

def validate_hgt(entry) -> bool:
    
    if len(entry) < 4:
        return False
 
    unit = entry[-2:]
    value = int(entry[:-2])

    # hgt (Height) - a number followed by either cm or in:
    if re.match(unit_regex, unit) == None:
        print('hgt missing units ', entry)
        return False

    # If in, the number must be at least 59 and at most 76.
    if (value < 59 or value > 76) and unit == 'in': 
        print('hgt (inch) invalid ', value)
        return False
    
    # If cm, the number must be at least 150 and at most 193.
    if (value < 150 or value > 193) and unit == 'cm': 
        print('hgt (cm) invalid ', value)
        return False
    
    return True

def validate_byr(entry) -> bool:

    # Check boundrary values
    helper = ' byr (Birth Year) - four digits; at least 1920 and at most 2002.'
    
    value = int(entry)

    if len(entry) != 4:
        return False
        
    if value < 1920 or value > 2002:
        print('byr invalid ' + entry + helper)
        return False

    return True

def validate_iyr(entry ):

    value = int(entry)

    helper = ' iyr (Issue Year) - four digits; at least 2010 and at most 2020.'
    if len(entry) != 4 or (value < 2010 or value > 2020):
        print('iyr invalid ' + entry + helper)
        return False

    return True

def validate_eyr(entry):

    value = int(entry)
    helper = ' eyr (Expiration Year) - four digits; at least 2020 and at most 2030.'
    if len(entry) != 4 or (value < 2020 or value > 2030):
        print('eyr invalid ' + entry + helper)
        return False

    return True

def check_passport_entry(entry):

    for field in fields: # could be done smarter
        if entry.find(field) == -1:
            print('Field ' + field + ' is missing')
            return False
    
    values = dict((x.strip(), y.strip()) 
             for x, y in (element.split(':')  
             for element in entry.split()))

    

    if not validate_eyr(values['eyr']):
        return False
    
    if not validate_iyr(values['iyr']):
        return False

    if not validate_byr(values['byr']):
        return False

    if not validate_hcl(values['hcl']):
        return False

    if not validate_hgt(values['hgt']):
        return False

    if not validate_pid(values['pid']):
        return False

    if not validate_ecl(values['ecl']):
        return False
 
    
        

    return True






# 2: > 123 && < 134 !113
if __name__ == '__main__':
    passports = open('input/4.txt').read()
    #passports = open('input/4_test.txt').read()
    
    #passports = open('input/42_test_valid.txt').read()
 
    #if validate_pid('000000001') == False and validate_pid('0123456789') == True: print ('pid ok')
    #if validate_ecl('brn') == True and validate_ecl('wat') == False: print ('ecl ok')
    #if validate_hcl('#123abc') == True and validate_hcl('#123abz') == False and validate_hcl('123abc') == False: print('hcl ok')

    #if validate_hgt('60in') == True and validate_hgt('190cm') == True and validate_hgt('190in') == False and validate_hgt('190') == False:
    #    print ('hgt ok')
    #else:
    #    print ('hgt nok')


    #exit()


    entries = passports.split('\n\n')

    valid_entries = 0
    for entry in entries:
               
        if check_passport_entry(entry) == True:
            valid_entries += 1
        #else:
        #    print('---------------')
        #    print(entry)
        #    print('===============\n\n')

    
    

    print('Valid entries ', valid_entries)