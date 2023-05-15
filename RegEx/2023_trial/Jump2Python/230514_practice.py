import re

p = re.compile('a[abc]c')
print(p.match('abc'))
print(p.match('azc'))

p = re.compile('a.c')
print(p.match('a가c'))
print(p.match('a\nc'))

p = re.compile('a[.]c')
print(p.match('a가c'))
print(p.match('a.c'))

p = re.compile('ab*c')
print(p.match('ac'))
print(p.match('abc'))
print(p.match('abbbbbc'))
print(p.match('akc'))

p = re.compile('ab+c')
print(p.match('ac'))
print(p.match('abc'))
print(p.match('abbbbbc'))
print(p.match('akc'))

p = re.compile('ab{2}c')
print(p.match('abc'))
print(p.match('abbc'))
print(p.match('abbbc'))

p = re.compile('ab{2,3}c')
print(p.match('abc'))
print(p.match('abbc'))
print(p.match('abbbc'))
print(p.match('abbbbc'))

p = re.compile('ab?c')
print(p.match('ac'))
print(p.match('abc'))
print(p.match('abbc'))
print(p.match('abbbc'))

p = re.compile('abc')
print(p.match('kkkabczzz'))             # match
print(p.search('kkkabczzz'))            # search
print(p.findall('kabcabczzzzabc333ab')) #findall
for x in p.finditer('kabcabczzzzabc333ab'):
    print(x)


p = re.compile('[a-z]{3}-\d{3}')
m = p.search('The new title, abc-001')
print(m.group())
print(m.start())
print(m.end())
print(m.span())


m = re.search('[a-z]{3}-\d{3}', 'The new title, abc-001')
print(m.group())
print(m.start())
print(m.end())
print(m.span())