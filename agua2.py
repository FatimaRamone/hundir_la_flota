import random


O = [" ","1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
A = ["A","x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
B = ["B","x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
C = ["C","x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
D = ["D","x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
E = ["E","x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
F = ["F","x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
G = ["G","x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
H = ["H","x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
I = ["I","x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
J = ["J","x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]

tablero = [O ,A , B, C ,D ,E, F , G , H , I , J]

for lista in tablero:
    print(lista)
    print("\n")

   
def humano_disparar(n):
    fila = input("Escoje una fila: ")
    fila = fila.upper()
    fila_index = ord(fila) - 64
    columna = int(input("Escoje una columna: "))
    
    if tablero[fila_index][columna] == "x":
        tablero[fila_index][columna] = "W"
    elif tablero[fila_index][columna] == "$":
        tablero[fila_index][columna] = "0"
    for lista in tablero:
                    for item in lista:
                        if "$" in item:
                            # ANSI escape code for green color
                            print("\033[92m" + item + "\033[0m", end=' ')
                        elif "W" in item:
                            # ANSI escape code for BLUE color
                          
                             print("\033[94m" + item + "\033[0m", end=' ')
                        elif "0" in item:
                              print("\033[91m" + item + "\033[0m", end=' ')

                        else:
                            print(item, end=' ')
                    print("\n")    

humano_disparar(1)
humano_disparar(1)
humano_disparar(1)




