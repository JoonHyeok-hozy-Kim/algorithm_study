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

compile시 re.M 옵션을 주면 ^가 나왔을때 문자열 전체가 아닌 각 줄의 시작이라고 인식
 -> 모든 줄에서 찾음.
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



# VERBOSE, X
'''
white space와 주석 문들을 제거하고 정규식 받기
 - 언제 쓰는가? 
    - 복잡한 정규식을 풀어서 쓸때 사용 가능
    - 아래 두 정규식은 동일함.
'''
p1 = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
p2 = re.compile(r"""
    &[#]                # Start of a numeric entity reference
    (
        0[0-7]+         # Octal form
    | [0-9]+            # Decimal form
    | x[0-9a-fA-F]+     # Hexadecimal form
    )
    ;                   # Trailing semicolon
    """, re.VERBOSE)