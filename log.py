import re


text = ''
file = open('log.txt')
for line in file:
    text = text + line
file.close()

result = re.findall('.{26}INFO.*/.*\(.*\)', text )
# result = re.findall('\(.*\)', text )
print( result )