# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def caller(url, inner):
    pp1 = re.compile(r'href\s*=\s*"([^"]*)"')
    mm1 = pp1.search(url)
    print(mm1.group(1), end=",")

    while True:
        pp2 = re.compile(r'<\s([\w]*)\s>(.*)<\s/\s\1\s>')
        mm2 = pp2.search(inner)
        if mm2:
            inner = mm2.group(2)
        else:
            print(inner)
            break


N = int(input())
for t in range(N):
    H = input()
    p1 = re.compile(r'<a\s*(.*)\s*>(.*)<\s*/a\s*>')
    for found in p1.finditer(H):
        caller(found.group(1), found.group(2))

'''
1
<a href="http://www.hackerrank.com"><h1><b>HackerRank</b></h1></a>
'''