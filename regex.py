##############################################################
'''
Regular expressions:
Used to validate text and search through text.

https://regexr.com

/   /   -search pattern, by default works once 
/   /g  -makes search/changes many times 
/bob/   -literal patter

atom -the smalles (basic) element of regular expression.
.       -one any character
^       -atom is on the beginning of the line
$       -atom is on the end of the line
\<      -here new word is beginning
\>      -here word is ending
\b      -here is the edge of the word (any new word isn`t beginning here and any word is ending here)
\B      -here is`t the edge of  the word
[ab]    -a or b, eg. [AEO]la = Ala, Ela, Ola
[1-9]   -digits from 1 to 9
()      -grouping, eg. /(Bob|Alice) Smith/g

Quantifiers:
*       -previous atom MAY occur 0 or more times, eg. /color*/g gives 'colo', 'color' or 'colorrrrrr'
11*0  -1 (second sign) must appear 0 ore more times, so answer: 10, 110, 111110, 11111111111111111111110 etc

+       -previous atom MAY occur 1 or more times
?       -previous atom MAY occur 0 or 1 times, eg. /colou?r/g gives 'color' and 'colour'

Bounds (granice):
{i}     -atom (previous character) must appear exactly i times, eg. [[:blank:]]{2} matches with exactly 2 blank characters
{i,}    -atom MUST appear at least i times, eg. [[:blank:]]{2,} matches with any sequence of 2 or more blank characters 
{,i}    -atom MUST appear at most i times
{i,j}   -atom MUST apper at least i times and at most j times, eg. xyz{2,4} matches the xy string followed by 2 to 4 the z character

10\{2,4}1 - zero (second sign) must appear at min 2 max 4 times, so answer: 1001, 10001, 100001 

Any email addres:
egrep "\S+@\S+.\S+"

Any IP addres:
egrep "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"

List the content of file without comments:
grep -V ^# [FILENAME]

Remove tags from html:
s/<[^>]*>//g                -will replace any content enclosed in <> by an empty string.

Classes:
[:alnum:]   -alphanumeric character
[:alpha:]   -alphabetic character
[:ascii:]   -ASCII character
[:blank:]   -blank character (tab or space)
[:cntrl:]   -control character
[:digit:]   -gigit character (0-9)
[:graph:]   -any printable character except space
[:print:]   -any printable character even space
[:space:]   -white-space character (space, newline \n, carriage return \r, horizontal tab \t...)
[:lower:]   -lowercase character
[:upper:]   -uppercase letter
[:punct:]   -any printable character which is not space or an alphanumeric character
[:xdigit:]  -hexadecimat digit (0-F)

Basic and regular expressions???????????'''

import re           #regular exresiions module import

regexPattern = re.compile(r'Pa(ranoja|tologia|rostatkiem)')     #

mo = regexPattern.search("Paranoja, Patologia plynie Parostatkiem w piękny rejs!")          #search() metod returns only first match of regex
mo2 = regexPattern.findall("Paranoja, Patologia plynie Parostatkiem w piękny rejs!")

print(mo.group())
print(mo2)

for sentence in mo2:
    print('Pa' + sentence)
