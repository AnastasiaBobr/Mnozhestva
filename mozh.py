def first(lst):
    print(len(set(lst)))    

def second(l, l2):
    print(set(l)& set(l2))
    print(len(set(l)& set(l2)))
    
def third(l, l2):
    res=sorted(list(set(l)&set(l2)))
    print(res)
    
def fourth(nams):
    numbers = set()
    for number in nams:
        if number in numbers:
             print("YES")
        else:
            print("NO")
            numbers.add(number)
            
def fift(file_name):
    a = open('input.txt',)
    n = set()
    for q in a:
        w = q.split()
        for i in w:
            n.add(i.rstrip('\n'))
    a.close()
    print(len(n))

    

lst=[1,2,3,4,5,3,2,5,3,6]
lst2=[9,8,7,6,5,7,6,5,4]


first(lst)
second(lst, lst2)
third(lst, lst2)
fourth(lst)
fift(input.txt)