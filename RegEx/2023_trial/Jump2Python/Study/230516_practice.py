import re

'''
[Backslash Problem]

- In python, "\\" will automatically interpreted as "\"
- Thus, we should use the raw string r""

'''

p = re.compile('\section')      # Interpreted as "(white_space)ection"
print(p.match('\section'))

p = re.compile('\\section')     # Also interpreted as "(white_space)ection"
print(p.match('\section'))

p = re.compile('\\\\section')   # Finally interpreted as "(white_space)ection"
print(p.match('\section'))

p = re.compile(r'\\section')    # Raw string usage, interpreted as "(white_space)ection"
print(p.match('\section'))




"""
[Meta Characters]

"""