# caso recursivo sem condição de parada

"""

def regressiva(i):
    print(i)
    regressiva(i-1)
    
regressiva(10)

"""



# caso recursivo com condição de parada

def regressiva(i):
    print(i)
    if i <= 1:
        return
    else:
        regressiva(i - 1)
regressiva(10)