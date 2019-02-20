from sys import stdin
n = int(stdin.readline().strip())
l = list(map(int,stdin.readline().strip().split()))
low = 0
up = 0
star = 0

def min_max(l,low,up,star):
    end = len(l)
    mid = (end-star)//2
    if len(l) > 0:
        if l[0] > up:
            up = l[0]
        if l[0] < low:
            low = l[0]
        return min_max(l[1:],low,up,star)
    else:
        print(low,up)
min_max(l,low,up,star)
