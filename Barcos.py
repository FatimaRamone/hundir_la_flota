import random


class Barco:
    def __init__(self , longitud , fila , columna , orientacion , lista_celulas):
        self.longitud = longitud
        self.fila = fila
        self.columna= columna
        self.orientacion=orientacion
        self.lista_celulas=lista_celulas

    def impactos(self , disparos):
        self.disparos= disparos         #esto no hace nada

    def hundido(self , tablero):    # le pasamos el objeto tablero como un input de la función , así tengo acceso a todos los atributos del objeto tablero
         lista=[]
         for i in self.lista_celulas:                 #cojo toda la lista de células del barco
              if tablero.tablero_lista[i[0]][i[1]]=="!":  #las comparo con el tablero para saber si la célula fue disparada
                   lista.append(True)                    # si la cécula está dañada (!) , la añado a la lista
              else:
                   lista.append(False)
         if all(lista):                                  # todas(all) las células del barco están hundidas
          for i in self.lista_celulas:                   #para cada célula del barco
              tablero.tablero_lista[i[0]][i[1]]="~"      # cambiamos el caracter ! por ~ para indicar que el barco está hundido
         return all (lista) , tablero                    #retorna : 1- si el barco está hundido o no (boolean) ; 2- el tablero actualizado
      
                   
        #versión mas compacta de una parte de la función:     
        #return all ([True if tablero.tablero_lista[item[0]][item[1]]=="!" else False for item in self.lista_celulas ])
    
      

    def dibujar(self , tablero):
        pass                             #esto no hace nada
    
class Tablero():             
    def __init__(self , color = "blanco"):     # pongo dentro de () los atributos que quiero personalizar
        self.diccionario_colores={"amarillo": 93 , "blanco" : 97 , "rosa" : 95}  # diccionario , desde aqui voy a llamar a los colores
        self.posicionBarcos= [] #atributo 2 , creo una lista vacía para almacenar la posición de los barcos 
        self.disparos=[]        #atributo 3 , creo una lista vacía para almacenar los disparos 
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


        self.tablero_lista = [O ,A , B, C ,D ,E, F , G , H , I , J]  # una lista de listas 
        self.color=color
        self.cells_hundidos=0 # empezamos con default 0
        self.lista_fila = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.lista_columna = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.lista_posicion = ["H", "V"]
    def posicionarBarco(self , Barco):
       self.Barco= Barco #esto no hace nada
       
    
    def recibirDisparo(self, fila , columna):
         self.fila = fila
         self.columna=columna
         #esto no hace nada , recibimos disparos en otra función
    def hundidos (self):
         contador=0
         for lista in self.tablero_lista: #recorre cada elemento de la lista llamada self.tablero_lista
              for item in lista:          #recorre cada elemento de las listas de tablero_lista 
                   if item =="!":
                        contador += 1
         return contador
                        
    def dibujar(self):           # esto no está siendo llamado 
        for lista in self.tablero_lista:  
                    for item in lista:
                        if "$" in item:
                            # ANSI escape code for green color
                            print("\033[92m" + item + "\033[0m", end=' ')
                        else:
                            print("\033["  +str(self.diccionario_colores[self.color])+"m" + item + "\033[0m", end=' ')
                    print("\n")
     
class Juego():
    def __init__(self,tablero_1 , tablero_2 , jugador_1 , jugador_2 , numero_cells):
        self.tablero_1=tablero_1       # todos los atributos son personalizables , excepto "turno"
        self.tablero_2= tablero_2
        self.jugador_1= jugador_1
        self.jugador_2= jugador_2
        self.numero_cells=numero_cells
    def iniciarPartida(self):
         self.turno = 0       # reinicia los turnos cada vez que inicie una nueva partida
    
    def disparar (self, fila , columna):
         self.fila= fila
         self.columna= columna        # no hace nada

    def QuedanBarcos(self):
         pass#tampoco hace nada
    def vencedor(self):
         if self.tablero_1.hundidos() == self.numero_cells: # si el numero de "!" de mi_tablero es igual a número de cells , pierdes
            return 2
         # 0 : no hay vencedores ; 1 : jugador_1 ; 2: jugador_2
         elif self.tablero_2.hundidos() == self.numero_cells:  # si el numero de "!" de su_tablero  es igual a número de cells , ganas
              return 1
         else:
              return 0
         

class Jugador():                                 # esto lo puedo borrar y no pasa nada
     def __init__(self ,nombre , partida = 0 ):
          self.nombre= nombre
          self.partida= partida

     def colocarBarcos(self , tablero):
          pass

     def jugar(self):
      pass

     
class JugadorHumano ():
     def __init__(self ,nombre , partida = 0 ):  
          self.nombre= nombre
          self.partida= partida


     def colocarBarcos(self ,tablero , n):
        flag=True      # un buleano que me dice si el input es válido ,por defecto es True
        while flag:
         fila = input("Escoje una fila: ")   
         fila = fila.upper()
         flag = fila not in tablero.lista_fila # flag = True significa que el input NO es válido , False significa que el input SÍ ES válido
         if flag :print("Ese input no es válido")
        flag=True      # un buleano que me dice si el input es válido ,por defecto es True
        while flag:
         columna =(input("Escoje una columna: "))
         flag = columna not in tablero.lista_columna # flag = True significa que el input NO es válido , False significa que el input SÍ ES válido
         if flag :print("Ese input no es válido")
        
        fila_index = ord(fila) - 64   # busca un index usando código ascii
        flag=True      # un buleano que me dice si el input es válido ,por defecto es True
        while flag:
         direccion=input("Quieres posicionar el barco en Horizontal o Vertical? Introduce H ò V : ").upper()
         flag = direccion not in tablero.lista_posicion # flag = True significa que el input NO es válido , False significa que el input SÍ ES válido
         if flag :print("Ese input no es válido")
        columna=int(columna)
        
        if direccion == "H":         
            if columna > 11 - n :    # para que los barcos no salgan del tablero 
                print("Eso no está permitido")
                return self.colocarBarcos(tablero ,n) #función recursiva
            else:  # el input es válido , entonces creamos una lista para almacenar las células del barco
                lista_celulas=[]
                for i in range(0 , n ):
                    if tablero.tablero_lista[fila_index ][columna + i] == "x": # si la célula en el tablero está libre
                        tablero.tablero_lista[fila_index ][columna + i] = "$"  # puedes ocuparlo ($)
                        lista_celulas.append((fila_index,columna + i))         # almacena las $ en la lista
                    else:
                        print( "Esa posición no está disponible , Vuelve a posicionar tu barco")
                        return self.colocarBarcos(tablero ,n)
        if direccion == "V":
            
            if fila_index > 11 - n :
                print("Eso no está permitido")
                return self.colocarBarcos(tablero ,n)
            print("1")    
            lista_celulas=[]
            for i in range(0 , n ):
                if tablero.tablero_lista[fila_index + i][columna] == "x":
                    tablero.tablero_lista[fila_index + i][columna] = "$"
                    lista_celulas.append((fila_index + i,columna))
                else:
                    print( "Esa posición no está disponible , Vuelve a posicionar tu barco")
                    return self.colocarBarcos(tablero ,n)
        
        for lista in tablero.tablero_lista:         # para imprimir la nueva posición del barco
                        for item in lista:
                            if "$" in item:
                                # ANSI escape code for green color
                                print("\033[92m" + item + "\033[0m", end=' ')
                            
                            else:
                                
                                print("\033["  +str(tablero.diccionario_colores[tablero.color])+"m" + item + "\033[0m", end=' ') #cambia el color de tablero e imprime el tablero
                        print("\n")
        barco=Barco( n , fila_index , columna , direccion , lista_celulas)  #creamos un objeto barco          
        tablero.posicionBarcos.append(barco)  # tablero.posicionBarcos = es una lista de objetos barco y posicionBarcos es un atributo de tablero          
        return barco
     def jugar(self , tablero): # esto funciona igual que la anterior función pero para disparar
        flag=True      # un buleano que me dice si el input es válido ,por defecto es True
        while flag:
         fila = input("Escoje una fila: ")   
         fila = fila.upper()
         flag = fila not in tablero.lista_fila # flag = True significa que el input NO es válido , False significa que el input SÍ ES válido
         if flag :print("Ese input no es válido")
        flag=True      # un buleano que me dice si el input es válido ,por defecto es True
        while flag:
         columna =(input("Escoje una columna: "))
         flag = columna not in tablero.lista_columna # flag = True significa que el input NO es válido , False significa que el input SÍ ES válido
         if flag :print("Ese input no es válido")
        
        fila_index = ord(fila) - 64
        
        columna=int(columna)

        
        
        
        if tablero.tablero_lista[fila_index][columna] == "x": # si la célula no disparada y sin barco
            tablero.tablero_lista[fila_index][columna] = "W"  # ahora muestra "agua"
        elif tablero.tablero_lista[fila_index][columna] == "$": # si la célula tiene barco y no está disparada
            tablero.tablero_lista[fila_index][columna] = "!"     #ahora muestra el disparo
        
        tablero.disparos.append((fila_index,columna))   # actualiza la lista de disparos del tablero 
        for objeto in tablero.posicionBarcos:           # todo este código es para detectar si un barco está hundido , si está hundido , cambia el caracter
             hundido, tablero=Barco.hundido(objeto , tablero)
             if hundido:
                  print("Un barco del Jugador Máquina ha sido tocado y hundido!!!")  #notifica el hundimiento
        for lista in tablero.tablero_lista: # imprime el tablero actualizado
                        for item in lista:
                            if "$" in item:
                                # ANSI escape code for green color
                                #print("\033[92m" + item + "\033[0m", end=' ') #escondo barcos enemigos
                                  print("\033["  +str(tablero.diccionario_colores[tablero.color])+"m" + "x" + "\033[0m", end=' ')
                            elif "W" in item:
                                # ANSI escape code for BLUE color
                            
                                print("\033[94m" + item + "\033[0m", end=' ')
                            elif item in ["!", "~"] :
                                print("\033[91m" + item + "\033[0m", end=' ')

                            else:
                                print("\033["  +str(tablero.diccionario_colores[tablero.color])+"m" + item + "\033[0m", end=' ')
                        print("\n")       
        return tablero

class JugadorMaquina():         
     def __init__(self ,nombre , partida = 0 ):
          self.nombre= nombre
          self.partida= partida


     def colocarBarcos(self , tablero , n):
        lista_fila = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]  
        fila = random.choice(lista_fila)                      # tiene un input random 
        lista_columna = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        columna = int(random.choice(lista_columna)) # tiene un input random 
        fila_index = lista_fila.index(fila)
        lista_posicion = ["H", "V"]
        direccion = random.choice(lista_posicion)  # tiene un input random 
# es el mismo código que la anterior clase 
        if direccion == "H":
            if columna > 11 - n:
                return self.colocarBarcos(tablero ,n)
                
            if all(tablero.tablero_lista[fila_index][columna+i] == "x" for i in range(n)):
                lista_celulas=[]
                for i in range(n):
                    tablero.tablero_lista[fila_index][columna+i] = "$"
                    lista_celulas.append((fila_index , columna + i))
            else:
                return self.colocarBarcos(tablero ,n)
                
        elif direccion == "V":
            if fila_index > 11 - n:
                return self.colocarBarcos(tablero ,n)
                
            if all(tablero.tablero_lista[fila_index+i][columna] == "x" for i in range(n)):
                lista_celulas=[]

                for i in range(n):
                    tablero.tablero_lista[fila_index+i][columna] = "$"
                    lista_celulas.append((fila_index + i , columna))
            else:
                return self.colocarBarcos(tablero ,n)
                
        for lista in tablero.tablero_lista:
            for item in lista:
                if "$" in item:
                    # ANSI escape code for green color
                    #print("\033[92m" + item + "\033[0m", end=' ')  , no quiero ver los barcos enemigos
                    print("\033["  +str(tablero.diccionario_colores[tablero.color])+"m" + "x" + "\033[0m", end=' ')
                else:
                    print("\033["  +str(tablero.diccionario_colores[tablero.color])+"m" + item + "\033[0m", end=' ')
            print("\n")
        barco=Barco( n , fila_index , columna , direccion , lista_celulas )                
        tablero.posicionBarcos.append(barco)                
        return barco
     def jugar(self , tablero):
            lista_fila = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
            fila = random.choice(lista_fila)
            lista_columna = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
            columna = int(random.choice(lista_columna))
            fila_index = lista_fila.index(fila)
            
            if tablero.tablero_lista[fila_index][columna] == "x":
                tablero.tablero_lista[fila_index][columna] = "W"
            elif tablero.tablero_lista[fila_index][columna] == "$":
                tablero.tablero_lista[fila_index][columna] = "!"
            
            tablero.disparos.append((fila_index,columna))
            for objeto in tablero.posicionBarcos:
                 hundido, tablero=Barco.hundido(objeto , tablero)
                 if hundido:
                  print("Un barco del Jugador Humano ha sido tocado y hundido!!!")
            for lista in tablero.tablero_lista:
                            for item in lista:
                                if "$" in item:
                                    # ANSI escape code for green color
                                    print("\033[92m" + item + "\033[0m", end=' ')
                                elif "W" in item:
                                    # ANSI escape code for BLUE color
                                
                                    print("\033[94m" + item + "\033[0m", end=' ')
                                elif item in ["!", "~"] :
                                    print("\033[91m" + item + "\033[0m", end=' ')

                                else:
                                    print("\033["  +str(tablero.diccionario_colores[tablero.color])+"m" + item + "\033[0m", end=' ')
                            print("\n")             
            return tablero
     

    
class JugadorHumanoRandom(JugadorHumano , JugadorMaquina): # es una alternativa para en main.py , si quisiéramos llamar por jugadorHumano y JugadorMáquina
    def __init__(self , tipo_de_jugador ,nombre):
        self.tipo_de_jugador= tipo_de_jugador
        if tipo_de_jugador == "humano":
            JugadorHumano.__init__(self ,nombre)
        else:
            JugadorMaquina.__init__(self ,nombre)
    
    def colocarBarcos(self, tablero, n ):
        if self.tipo_de_jugador == "humano":
            return JugadorHumano.colocarBarcos(self, tablero, n)
        else:
            return JugadorMaquina.colocarBarcos(self , tablero, n)
    def jugar(self , tablero):
            if self.tipo_de_jugador == "humano":
             return JugadorHumano.jugar(self ,tablero)
            else:
             return JugadorMaquina .jugar(self ,tablero)



