import re

# Grouping : 문자열이 계속해서 반복되는지 조사하는 정규식 : ()
p = re.compile('(ABC)+')
print(p.search('ABAB'))
print(p.search('ABCAB'))
print(p.search('ABCABC'))


# Indexing a group
#    group(0)	매치된 전체 문자열
#    group(1)	첫 번째 그룹에 해당되는 문자열
#    group(2)	두 번째 그룹에 해당되는 문자열
#    group(n)	n 번째 그룹에 해당되는 문자열
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")              # (문자반복) whitespace반복 (숫자반복 - 숫자반복 - 숫자반복)
m = p.search('park 010-4879-5588')
print('name : {} / mobile : {}'.format(m.group(1), m.group(2)))


# Nested Group : 그룹이 중첩되어 있는 경우는 바깥쪽부터 시작하여 안쪽으로 들어갈수록 인덱스가 증가한다.
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")              # (문자반복) whitespace반복 ((숫자반복) - 숫자반복 - 숫자반복)
m = p.search('park 010-4879-5588')
print('name : {} / mobile : {} / type : {}'.format(m.group(1), m.group(2), m.group(3)))


# Back Reference
p = re.compile(r'(\b\w+)\s\1')
print(p.search('Paris in the the spring spring').group())


# Naming the Group : (?P<name>____)
p = re.compile(r"(?P<person_name>\w+)\s+(\d+[-]\d+[-]\d+)")   # (문자반복) whitespace반복 (숫자반복 - 숫자반복 - 숫자반복)
m = p.search('park 010-4879-5588')
print(m.group("person_name"))