from random import randrange


s = set()
while len(s) < 65-6:
    temp = int(randrange(25, 576))
    if temp in s:
        continue
    s.add(temp)

ls = list(s)
ls.sort()
print('---')
for i, n in enumerate(ls):
    print('{} / {}. '.format(i+7, n))
print('---')