# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


N = int(input())
words = []
p = re.compile(r'[a-zA-Z0-9_]([a-zA-Z0-9_]+)[a-zA-Z0-9_]')
for _ in range(N):
    for word in p.finditer(input()):
        words.append(word.group(1))

Q = int(input())
for _ in range(Q):
    result = 0
    query = input()
    regex = query[0]
    if len(query) > 1:
        regex += '(?=(' + query[1:] +'))'

    p = re.compile(regex)
    for word in words:
        for f in p.finditer(word):
            result += 1

    print(result)


'''
1
eeee eeeee
1
ee

'''

# p = re.compile('e(?=ee)')
# print(p.findall('eeee'))