def base():
     binario = input()
     l = len(binario)-1
     entero  = 0
     for i in binario:
          potencia=2**1
          entero = entero+(int(i)*potencia)
          l=l-1
     return entero
