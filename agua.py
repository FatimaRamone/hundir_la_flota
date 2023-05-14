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


#esto imprime el tablero original 
#for lista in tablero:
    #print(lista)
    #print("\n")




#la funcion posicionar barco recibe un valor N , la longitud del barco
#el usuario escoje una posición
#se comprueba que la posición esté libre:
                      #else : raise Error ---> meterle un while para que retorne?
#pregunta al usuario si quiere posicionar en vertical u en horizontal
                   #si posiciona en horizontal : fila[posicion_elegida] ="#" , fila[posicion_elegida - N] ---> bucle 
                   # si se posicional
for lista in tablero:
    print(lista)
    print("\n")


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
                    
#importar random
def posicionar_barco_random(n):
    lista_fila = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    fila = random.choice(lista_fila)
    lista_columna = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    columna = int(random.choice(lista_columna))
    fila_index = lista_fila.index(fila)
    lista_posicion = ["H", "V"]
    direccion = random.choice(lista_posicion)
    if direccion == "H":
        if columna > 11 - n:
            posicionar_barco_random(n)
            return
        if all(tablero[fila_index][columna+i] == "x" for i in range(n)):
            for i in range(n):
                tablero[fila_index][columna+i] = "$"
        else:
            posicionar_barco_random(n)
            return
    elif direccion == "V":
        if fila_index > 11 - n:
            posicionar_barco_random(n)
            return
        if all(tablero[fila_index+i][columna] == "x" for i in range(n)):
            for i in range(n):
                tablero[fila_index+i][columna] = "$"
        else:
            posicionar_barco_random(n)
            return
    for lista in tablero:
        for item in lista:
            if "$" in item:
                # ANSI escape code for green color
                print("\033[92m" + item + "\033[0m", end=' ')
            else:
                print(item, end=' ')
        print("\n")

 # x = agua , $ (verde) = barco posicionado ,W(azul)= disparo al agua , !(rojo) = tocado , ~ = tocado_y_hundido

def humano_disparar():
    fila = input("Escoje una fila: ")
    fila = fila.upper()
    fila_index = ord(fila) - 64
    columna = int(input("Escoje una columna: "))
    
    if tablero[fila_index][columna] == "x":
        tablero[fila_index][columna] = "W"
    elif tablero[fila_index][columna] == "$":
        tablero[fila_index][columna] = "!"
    for lista in tablero:
                    for item in lista:
                        if "$" in item:
                            # ANSI escape code for green color
                            print("\033[92m" + item + "\033[0m", end=' ')
                        elif "W" in item:
                            # ANSI escape code for BLUE color
                          
                             print("\033[94m" + item + "\033[0m", end=' ')
                        elif "!" in item:
                              print("\033[91m" + item + "\033[0m", end=' ')

                        else:
                            print(item, end=' ')
                    print("\n")       

def maquina_disparar():
    lista_fila = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    fila = random.choice(lista_fila)
    lista_columna = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    columna = int(random.choice(lista_columna))
    fila_index = lista_fila.index(fila)
    
    if tablero[fila_index][columna] == "x":
        tablero[fila_index][columna] = "W"
    elif tablero[fila_index][columna] == "$":
        tablero[fila_index][columna] = "!"
    for lista in tablero:
                    for item in lista:
                        if "$" in item:
                            # ANSI escape code for green color
                            print("\033[92m" + item + "\033[0m", end=' ')
                        elif "W" in item:
                            # ANSI escape code for BLUE color
                          
                             print("\033[94m" + item + "\033[0m", end=' ')
                        elif "!" in item:
                              print("\033[91m" + item + "\033[0m", end=' ')

                        else:
                            print(item, end=' ')
                    print("\n")       




#------------------------------------------------------------

def posicionar_barco_random(n):
    lista_fila= [ "A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J"]
    fila = random.choice(lista_fila)
    lista_columna= [ "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10"]
    columna = int(random.choice(lista_columna))
    fila_index = ord(fila) - 64
    lista_posicion=["H" , "V"]
    direccion=random.choice(lista_posicion)
    if direccion == "H":
        if columna > 11 - n :
            posicionar_barco_random(n)
        if all([columna+i<11 and tablero[fila_index ][columna + i] == "x" for i in range(n)]):
            for i in range(n):
                tablero[fila_index ][columna + i] = "$"
        else:
            posicionar_barco_random(n)
       # else:
           # for i in range(0 , n ):
               # if tablero[fila_index ][columna + i] == "x":
                 #   tablero[fila_index ][columna + i] = "$"
                #else:
                    
                    #posicionar_barco_random(n)
    if direccion == "V":
        if columna > 11 - n :
            
            posicionar_barco_random(n)
        
        if all([fila_index+i<11 and tablero[fila_index + i][columna] == "x" for i in range(n)]):
            for i in range(n):
                tablero[fila_index + i][columna] = "$"
        else:
            posicionar_barco_random(n)
        #for i in range(0 , n ):
            
            #if tablero[fila_index + i][columna] == "x": #hay algo mal en esta linea
            #    tablero[fila_index + i][columna] = "$"
            #else:
            #    
            #    posicionar_barco_random(n)
    for lista in tablero:
                    for item in lista:
                        if "$" in item:
                            # ANSI escape code for green color
                            print("\033[92m" + item + "\033[0m", end=' ')
                        else:
                            print(item, end=' ')
                    print("\n")




#for lista in tablero:
    #print(lista)
    #print("\n")

posicionar_barco(5)
humano_disparar()  
humano_disparar()
humano_disparar()




