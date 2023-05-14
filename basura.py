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

def posicionar_barco(n):
    fila = input("Escoje una fila: ")
    fila = fila.upper()
    columna = int(input("Escoje una columna: "))
    fila_index = ord(fila) - 64
    direccion=input("Quieres posicionar el barco en Horizontal o Vertical? Introduce H ò V : ").upper()
    if direccion == "H":
        if columna > 11 - n :
            print("Eso no está permitido")
            posicionar_barco(n)
        else:
            for i in range(0 , n ):
                if tablero[fila_index ][columna + i] == "x":
                    tablero[fila_index ][columna + i] = "$"
                    
                else:
                    print( "Esa posición no está disponible , Vuelve a posicionar tu barco")
                    posicionar_barco(n)
    if direccion == "V":
        if columna > 11 - n :
            print("Eso no está permitido")
            posicionar_barco(n)
        for i in range(0 , n ):
            if tablero[fila_index + i][columna] == "x":
                tablero[fila_index + i][columna] = "$"
            else:
                print( "Esa posición no está disponible , Vuelve a posicionar tu barco")
                posicionar_barco(n)
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
posicionar_barco(3)