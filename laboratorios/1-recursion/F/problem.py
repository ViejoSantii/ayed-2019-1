import json
from sys import stdin
def hanoi1(n ,inicio, aux, final):
    if n==1:
        print(inicio, "->", final)
    else:
        hanoi1(n-1,inicio, final, aux)
        print(inicio, "->", final)
        hanoi1(n-1, aux, inicio, final)



# TODO Complete!
def hanoi(n):
    return hanoi1(n, "A", "B", "C")


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            hanoi(n)
        print('OK!')
