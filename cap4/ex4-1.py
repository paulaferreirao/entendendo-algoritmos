# Cap4. Quicksort.

"""
def soma(lista):
    total = 0
    for x in lista:
        total += x
    return total
print(soma([1,2,3,4,5]))
"""

#4.1.escreva o código para função soma, vista anteriormente.

def soma(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + soma(lista[1:])
print(soma([1,2,3,4,5])) # 5+4+3+2+1 = 15