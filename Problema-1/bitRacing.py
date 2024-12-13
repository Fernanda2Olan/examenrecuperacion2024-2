import math
 
def suma_de_dos_digitos(num): 
    while num >= 10:
        num = sum(int(d) for d in str(num))
    return num

def carrera(num):
    digitos = [int(d) for d in str(num)]
    