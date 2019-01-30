from sys import stdin
def search(arreglo,n,a):
    inicio = 0
    final = len(arreglo)
    mitad = (final-inicio)//2
    if len(arreglo) == 1:
        if n == arreglo[mitad]:
            a += mitad
            return a
        else:
            a = -1
            return a
    elif n == arreglo[mitad]:
        a += mitad
        return a
    elif n > arreglo[mitad]:
        a += mitad
        return search(arreglo[mitad:final],n,a)
    else:
        return search(arreglo[inicio:mitad],n,a)
def main():
    n =int(stdin.readline().strip())
    arreglo = [int(i) for i in stdin.readline().strip().split()]
    a = 0
    s = search(arreglo,n,a)
    print(s)
main()
