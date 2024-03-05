import re

contact ='Doe, John: 555-1212'
match =re.search(r'\w+, \w+: \s+', contact)


out =match.group(0)
#
# for i in 'hello': res= len (i)
#
# print(res)