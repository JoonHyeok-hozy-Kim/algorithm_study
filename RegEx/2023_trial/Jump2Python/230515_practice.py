import re

# DOTALL(S) Option
print('\n* DOTALL Option : \\n will also be considered by using .')
p = re.compile('a.b')
print(' - Without DOTALL : {}'.format(p.match('a\nb')))

p = re.compile('a.b', re.DOTALL)
print(' - With DOTALL : {}'.format(p.match('a\nb')))

p = re.compile('a.b', re.S)
print(' - With S : {}'.format(p.match('a\nb')))


# IGNORECASE(I) Option
print('\n* IGNORECASE(I) Option.')
p = re.compile('[a-z]+')
print(' - Without IGNORECASE : {}'.format(p.match('Python')))

p = re.compile('[a-z]+', re.I)
print(' - With IGNORECASE : {}'.format(p.match('Python')))


# MULTILINE(M)
print('\n* MULTILINE(I) Option.')
'''
^는 문자열의 시작 / $는 문자열의 끝을 의미하는 메타문자
    EX) "^python"은 문자열의 시작이 python
    EX) "python$"는 문자열의 끝이 python
'''
# 여러줄 데이터
multiline_data = """python one
abc
python two
hhh
python three"""

p = re.compile('^python\s\w+')
print('한 줄만 찾고 끝남 : {}'.format(p.findall(multiline_data)))

p = re.compile('^python\s\w+', re.M)
print('여러줄에서 모두 찾음 : {}'.format(p.findall(multiline_data)))