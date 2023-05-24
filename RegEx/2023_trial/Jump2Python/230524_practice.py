import re

# Lookahead Assertions
# Positive (?=...) : ... 에 해당되는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
# Negative (?!=...) : ...에 해당되는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.

# Ex.1-1) Extracting "http:"
p = re.compile('.+:')
m = p.search("http://google.com")
print(m.group())

# Ex.1-2) Using Positive Lookahead Assertions
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())



# Ex.2-1) 확장자 형태에서 .bat 파일을 제외한다면?
p = re.compile(".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$")
print(p.search("a.txt").group())
print(p.search("b.cf").group())
print(p.search("c.bat"))
# print(p.search("c.bate"))     # 4자리 이상 파일 확장자 지원 불가

# Ex.2-2) Using Negative Lookahead Assertions
p = re.compile(".*[.](?!=bat).*$")
print(p.search("a.txt").group())
print(p.search("b.cf").group())
print(p.search("c.bat").group())
print(p.search("c.bate").group())