##############################################################
import re                                                       

regexPattern = re.compile(r'Pa(ranoja|tologia|rostatkiem)')     
                                                                

mo = regexPattern.search("Paranoja, Patologia plynie Parostatkiem w piękny rejs!")          #search() metod returns only first match of regex
mo2 = regexPattern.findall("Paranoja, Patologia plynie Parostatkiem w piękny rejs!")

print(mo.group())
print(mo2)

for sentence in mo2:
    print('Pa' + sentence)
