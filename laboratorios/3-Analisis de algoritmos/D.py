from sys import stdin

def funcion(n,l,r):
    if n > 0:
        if len(l) > 1:
            v = l[0]+l[1]
            r.append(v)
            funcion(n,l[1:],r)
        else:
            r.append(1)
            print(r)
            l = r
            r = [1]
            funcion(n-1,l,r)
            
            
n = int(stdin.readline().strip())
l = [1]
r = []
funcion(n,l,r)
