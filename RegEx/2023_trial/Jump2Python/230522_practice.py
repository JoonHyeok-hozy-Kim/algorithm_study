import re

'''
Concept) Zerowidth Assertions
+, *, [], {} 등의 메타문자는 매치가 진행될 때 현재 매치되고 있는 문자열의 위치가 변경된다(보통 소비된다고 표현한다). 
하지만 이와 달리 문자열을 소비시키지 않는 메타 문자도 있다. 
이번에는 이런 문자열 소비가 없는(zerowidth assertions) 메타 문자에 대해 살펴보자.
'''


# | 메타 문자는 or과 동일한 의미로 사용된다. A|B라는 정규식이 있다면 A 또는 B라는 의미가 된다.
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)
m = p.search('HelloCrow')
print(m)

# ^ 메타 문자는 문자열의 맨 처음과 일치함을 의미한다. 
p = re.compile('^Life')
m = p.match('Life is too short')
print(m)

# $는 문자열의 끝과 매치함을 의미한다.
p = re.compile('short$')
m = p.search('Life is too short')
print(m)

# \A는 문자열의 처음과 매치됨을 의미한다. \A는 줄과 상관없이 전체 문자열의 처음하고만 매치된다.
s = 'abc\nkjh123'
p1 = re.compile('^kjh', re.M)   # ^의 경우 MULTILINE 옵션을 주면 먹음.
p2 = re.compile(r'\Akjh', re.M)  # \A의 경우 줄과 관련 없이 무조건 첫째줄
print('^ : {}\n\\A : {}'.format(p1.search(s), p2.search(s)))

# \Z는 문자열의 끝과 매치됨을 의미한다. 
# \A와 동일하게 re.MULTILINE 옵션을 사용할 경우 전체 문자열의 끝과 매치된다.
s = 'abc\nkjh123'
p1 = re.compile('abc$', re.M)   # $의 경우 MULTILINE 옵션을 주면 먹음.
p2 = re.compile(r'abc\Z', re.M)  # \Z의 경우 줄과 관련 없이 무조건 첫째줄
print('$ : {}\n\\A : {}'.format(p1.search(s), p2.search(s)))

# \b는 단어 구분자(Word boundary)이다. 보통 단어는 whitespace에 의해 구분된다.
p = re.compile(r'\bcloud\b')                # raw string 사용 안할경우 Python의 backspace \b로 인식!
print(p.search('aaaaaaa cloud 1111111'))    # 정상작동
print(p.search('aaaaaaacloud1111111'))      # whitespace가 없으므로 작동 안함.

# \B 메타 문자는 \b 메타 문자와 반대의 경우이다. 
# 즉 whitespace로 구분된 단어가 아닌 경우에만 매치된다.
p = re.compile(r'\Bcloud\B')                # raw string 사용 안할경우 Python의 backspace \b로 인식!
print(p.search('aaaaaaa cloud 1111111'))    # whitespace가 있으므로 작동 안함.
print(p.search('aaaaaaacloud1111111'))      # 정상작동