import re

# sub method 문자열 바꾸기
p = re.compile('(red|blue|white)')
print(p.sub('purple', 'A red hat and a blue coat'))             # 있는 것 다 바꾸기
print(p.sub('purple', 'A red hat and a blue coat', count=1))    # 한번만 바꾸기

# subn : 바꾼 결과물과 횟수를 튜플로
p = re.compile('(red|blue|white)')
print(p.subn('purple', 'A red hat and a blue coat'))

# sub에서 참조값 사용하기 : \g
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub('\g<phone> \g<name>', "Park 010-3323-6675"))
print(p.sub('\g<2> \g<1>', "Park 010-3323-6675"))

# 함수를 arg로 받기
def replace_to_hex(match):
    value = int(match.group())
    return hex(value)
p = re.compile(r'\d+')
print(p.sub(replace_to_hex, 'Call 65490 for printing, 49152 for user code.'))



# Greedy vs Non-Greedy
# 정규식에서 *는 greedy 하므로, 매치가능한 최대한의 문자열을 return함.
s = '<html><head><title>Title</title>'
p = re.compile('<.*>')     # Greedy!
print(p.match(s).group())

# ? 문자를 추가하면 non-greedy하게 매치결과를 return함.
p = re.compile('<.*?>')    # Non-greedy!
print(p.match(s).group())