def sort_stack2(s):
    t = []
    t2 = []
    for i in range(len(s)):
        x = s.pop()
        for _ in range(len(s) - i):
            t.append(s.pop())
        while s and s[-1] > x:
            t2.append(s.pop())
        s.append(x)
        while t2:
            s.append(t2.pop())
        while t:
            s.append(t.pop())
    return s

f =open('foSTACKE.txt','r')
s = []
s = f.read().split()
f.close()
point = sort_stack2(s)
point = list(map(int,point))
print(point)
f = open('foSTACKE', 'w')
for hleb in point:
    f.write(str(hleb))
f.close()

