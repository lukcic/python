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

#print('415-555-424c to jest numer telefonu')
#print(isPhoneNumber('415-555-4242'))
#print('Dupa dupa to jest numer telefonu')
#print(isPhoneNumber('Dupa dupa'))

#####################################################################################################################################
message = "Zadzwoń pod numer 415-555-1211 po przerwie. 415-555-9999 to moje biuro."

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("znaleziono numer telefonu: " + chunk)
print('Gotowe!')

#####################################################################################################################################
import re                                                           #re.compile() -przekazenie ciagu tekstowego zawierającego wyrażenie regularne do funkcji compile() powoduje zwrot obiektu typu Regex

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')               # przypisanie zmiennej obiektu Regex, r na początku wyrażenia oznacza "niezmodyfikowany ciąg tekstowy", czyli nie wymaga // do wpisania /
mo = phoneNumRegex.search("Mój numer telefonu to 723-333-2222.")    # metoda search() obiektu Regex przeszukuje ciąg w celu znalezienia dopasowań wzorca, jeżeli nic nie znajdzie zwraca None
print("Znaleziono numer telefonu: " + mo.group())                   # Jeżeli znajdzie - zwróci obiekt typu Match, metoda group() obiektu match zwraca faktycznie znaleziony tekst.

#####################################################################################################################################
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')          # grupowanie wyrażen przy pomocy nawiasów
mo = phoneNumRegex2.search('Mój numer telefonu to 785-033-2222.')

print(mo.group())                                                   # brak argumentu (lub argument 0) powoduje zwrócenie wszystkich grup
print(mo.group(1))                                                  # argument '1' zwraca pierwszą grupę
print(mo.group(2))                                                  # argument '2' zwraca grugą grupę

print(mo.groups())                                                  # metoda groups() zwraca wszystkie grupy w postaci krotki (tupple)
zmienna1, zmienna2 = mo.groups()                                    # przypisanie dwóm zmiennym wartości z krotki
print('zmienna1= ',zmienna1)
print('zmienna2= ',zmienna2)

#####################################################################################################################################
heroRegex = re.compile(r'Batman|Robin')                             # Dopasowanie wielu grup za pomocą potoku: 'Batman' lub 'Robin'

mo1 = heroRegex.search('Batman, Superman i Robin')                  # W przypadku wystąpienia więcej niż jednego dopasowania obiekt Match zwraca tylko pierwsze dopaosowanie
print(mo1.group())

mo2 = heroRegex.findall('Batman, Superman i Robin')                 # Metoda findall() przeszukuje ciąg tekstowy i zwraca wszystkie dopasowania w formie listy ciągów tekstowych (jeżeli nie ma grup)
print(mo2)                                                          # Jeżeli w wyrażeniu są grupy, findall() zwróci listę krotek.

batRegex = re.compile(r'Bat(man|mobil|copter|woman)')
mo3 = batRegex.search('Batmobil stracił koło, a Batwoman wypadła z wozu.')
mo4 = batRegex.findall('Batmobil stracił koło, a Batwoman wypadła z wozu.')

print(mo3.group())
print(mo4)

for i in mo4:
    print('Bat'+ i)

