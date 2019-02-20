from sys import stdin

def funcion(l):
    for i in range(1, len(l)):
        k = l[i]
        j = i
        while j > 0 and l[j-1] < k:
            l[j] = l[j-1]
            j = j-1
        l[j] = k
    for x in range(len(l[0:10])):
        l[x] = str(l[x])
    print(','.join(l[0:10]))
    
l = list(map(int,stdin.readline().strip().split()))
if len(l) > 10 or len(l)== 10:
    funcion(l)
else:
    print(l)
