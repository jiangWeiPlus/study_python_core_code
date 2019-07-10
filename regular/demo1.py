# coding = utf-8 
import re

# match
base_str = '''hello
world
ello
orld
'''

m = re.match('.*ll.*', base_str)
if m is not None:
    print(m.group())
else:
    print('not match')

m = re.search('ll', base_str)
if m is not None:
    print(m.group())
else:
    print('search failed.')

m = re.findall('.*aa.*', base_str)
if m:
    print(m)
else:
    print('findall none.')
