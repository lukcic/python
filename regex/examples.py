# This functions checks if given string is a phone number in format xxx-xxx-xxxx

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
            return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

'''
print('415-555-4242 that's phone number')
print(isPhoneNumber('415-555-4242'))
print('Dupa dupa that's phone number')
print(isPhoneNumber('Dupa dupa'))
'''
#####################################################################################################################################
# This contruction is looking for phone numbers in given text - is using isPhoneNumber() function
 
message = "Call number 415-555-1211 after break. 415-555-9999 thats my office number."

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Found phone number: " + chunk)
print('Finish!')

#####################################################################################################################################
# This construction is looking for phone number in gien text - is using regular expressions

import re                                                           # regular expresions module import

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')               # Sending string with regular expression to compile() function returns regex object
                                                                    # r in beginning of expressions means 'unmodified string' - don't need steering signs (\n instead \\n)

mo = phoneNumRegex.search("My phone number is: 723-333-2222.")      # search() method of Regex object is looking for this regex in given string, if doesn't find it will return 'None'
                                                                    # If find match, it returns first match only as Match object type

print("Foud phone number: " + mo.group())                           # group() method of Match type returns matched string

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
#####################################################################################################################################
# This construction is looking for regular expressions in groups

phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')          # grouping using parenthesis
mo = phoneNumRegex2.search('My phone number is: 785-033-2222.')

print(mo.group())                                                   # group() with no argument (or argument 0) returns all groups of firsth match as a full sentence (string)
print(mo.group(1))                                                  # argument '1' returns firsth group
print(mo.group(2))                                                  # argument '2' returns second group

print('-----------------------------------------------------------------')

print(mo.groups())                                                  # groups() returns all groups (not matches!) divided as a tupple
variable1, variable2 = mo.groups()                                  # assigning tupple values to variables

print('group1= ',variable1)
print('group2= ',variable2)

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
#####################################################################################################################################
# This construction is looking for regular expressions using streams

heroRegex = re.compile(r'Batman|Robin')                             # Matching many matches using stream: 'Batman' or 'Robin'

mo1 = heroRegex.search('Batman, Superman i Robin')                  # In case there is more than 1 match, object Match returns only first of them 
print(mo1.group())

mo11 = heroRegex.findall('Batman, Superman i Robin')                 # findall() method returns all matches and returns them as list of strings (in case there are no groups), with groups in regex returns list of tupples
print(mo11)                                                          

print('-----------------------------------------------------------------')

batRegex = re.compile(r'Bat(man|mobil|woman)')
mo111 = batRegex.search('Batmobil stracił koło, a Batwoman wypadła z wozu.')
mo1111 = batRegex.findall('Batmobil stracił koło, a Batwoman wypadła z wozu.')

print(mo111.groups())                                                 # Returns only one match, because there is only one group with more matches, need to use findall() 
print(mo1111)                                                          # findall() returns only matches without prefix

for i in mo1111:                                                       # Printing full words from findall() using loop
    print('Bat'+ i)

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

#####################################################################################################################################
# This construction is looking for regular expressions with optional sentences (atom may occur 0 or 1 times)

batwomanRegex = re.compile(r'Bat(wo)?man')

mo11 = batwomanRegex.search("Batman is the best superhero!")
print(mo11.group())

mo12 = batwomanRegex.search("Batwoman is the best superhero!")
print(mo12.group())

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

#####################################################################################################################################
# This construction is lookig for regular expressions with optional sentences (atom may occur 0 or MORE times)

haRegex = re.compile('Bua(ha)*ha')  

mo6 = haRegex.search("Buaha")
print(mo6.group())

mo66 = haRegex.search("Buahahahahaha")
print(mo66.group())                         

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

#####################################################################################################################################
# This construction is looking for regular expressions with repeted sentences i given range times
 
haRegex2 = re.compile('Bua(ha){3,5}')
mo9 = haRegex2.search("Buahahahahaha")        # group() in Python is greedy, so it returns the longest case
print(mo9.group())    

print('-----------------------------------------------------------------')

haRegex2 = re.compile('Bua(ha){3,5}?')
mo9 = haRegex2.search("Buahahahahaha")        # sign ? after range means, this is non-greedy fit - returns the shortest case
print(mo9.group())  

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

#####################################################################################################################################
# This construction is looking for regular expressions ingoring cause sensitive

regexPattern = re.compile(r'Pa(\w+)', re.I)                   # re.I argument tells re.compile() to ignore cause sinsitive

mo2 = regexPattern.findall("Paranoja, patologia plynie parostatkiem w piękny rejs!")

for i in mo2:
    print('Pa' + i)

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

#####################################################################################################################################
# This construction will replace strings finded by regular expressions using sub() method

changeRegex = re.compile('Agent \w+')
mo00 = changeRegex.sub('CENSORED', 'Agent Alicia gived top secret documents to Agent Mary.')
print(mo00)

chaneRegex2 = re.compile(r'Agent (\w)(\w*)')                                                # Firsth group means firsth letter of name
mo000 = chaneRegex2.sub(r'\1****','Agent Alicia gived top secret documents to Agent Mary.')  # \1 means leve the firsth group as is, change the rest to '****'
print(mo000)

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

#####################################################################################################################################