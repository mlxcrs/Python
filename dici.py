def fun(b):
    m = 0
    s = 0
    vp = -999999999
    vm = 999999999
    q = 0
    for i,j in b.iteritems():
        s = s+j
        if vp<j:
            vp = j
        if vm>j:
            vm = j
        q = q+1
    m = s/q
    print "media e: %d" %m
    print "soma e: %d" %s
    print "Valores estao entre {%d,%d}" %(vm,vp)
    
c = {'a':1,'b':2,'c':3,'d':4,'e':5}
fun(c)