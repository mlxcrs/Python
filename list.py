def list(a):
    b = []
    for i in a:
        b.append(mlist(i))
    print b
def mlist(a):
    x = 0
    for i in a:
        x = x+1
    return x
a = [6,23,12,15,19]
b = [9,29,33,56,98,1,5,9]
c = [2,6,5]
d = [4,5,6,7,8,9]
e = [a,b,c,d]
list(e)