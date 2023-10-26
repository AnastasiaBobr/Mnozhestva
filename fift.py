a = open('input.txt',)
n = set()
for q in a:
    w = q.split()
    for i in w:
        n.add(i.rstrip('\n'))
a.close()
print(len(n))