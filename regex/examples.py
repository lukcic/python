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

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
#####################################################################################################################################
# This construction is looking for regular expressions in groups

phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')          # grouping using parenthesis
mo = phoneNumRegex2.search('My phone number is: 785-033-2222.')

print(mo.group())                                                   # group() with n argument (od argument 0) returns all groups 
print(mo.group(1))                                                  # argument '1' returns firsth group
print(mo.group(2))                                                  # argument '2' returns second group

print('-----------------------------------------------------------------')

print(mo.groups())                                                  # groups() returns all groups as a tupple
variable1, variable2 = mo.groups()                                  # assigning tupple values to variables

print('group1= ',variable1)
print('group2= ',variable2)

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
#####################################################################################################################################
# This construction 

heroRegex = re.compile(r'Batman|Robin')                             # Dopasowanie wielu grup za pomocą potoku: 'Batman' lub 'Robin'

mo1 = heroRegex.search('Batman, Superman i Robin')                  # W przypadku wystąpienia więcej niż jednego dopasowania obiekt Match zwraca tylko pierwsze dopaosowanie
print(mo1.group())

mo2 = heroRegex.findall('Batman, Superman i Robin')                 # Metoda findall() przeszukuje ciąg tekstowy i zwraca wszystkie dopasowania w formie listy ciągów tekstowych (jeżeli nie ma grup)
print(mo2)                                                          # Jeżeli w wyrażeniu są grupy, findall() zwróci listę krotek.
print('-----------------------------------------------------------------')

batRegex = re.compile(r'Bat(man|mobil|copter|woman)')
mo3 = batRegex.search('Batmobil stracił koło, a Batwoman wypadła z wozu.')
mo4 = batRegex.findall('Batmobil stracił koło, a Batwoman wypadła z wozu.')

print(mo3.group())
print(mo4)

for i in mo4:
    print('Bat'+ i)

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

#####################################################################################################################################