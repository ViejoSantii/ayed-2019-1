from sys import stdin
def encontrar(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        m = encontrar(lista[1:])
        return m if m>lista[0] else lista[0]
    
def main():
    n=int(stdin.readline().strip())
    lista=[int(i) for i in stdin.readline().strip().split()]
    l=len(lista)//2
    if len(lista) == 0:
        return 0
    else:
        print(encontrar(lista[l:])*encontrar(lista[:l]))
        
main()
