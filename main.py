import Barcos
from Barcos import JugadorHumano , JugadorMaquina , JugadorHumanoRandom

jugador1 = JugadorHumano( "nombre_jugador") # creamos objeto jugador1 , es un jugador Humano
jugador2= JugadorMaquina( "nombre_jugador2")  # creamos objeto jugador2
 
 #1 barco de 5
 #1 barco de 4
 #2 barcos de 3
 #1 barco de 2

mi_tablero=Barcos.Tablero("rosa") #dentro de paréNtesis VAN SOLAMENTE INPUTS
su_tablero=Barcos.Tablero("amarillo")

mi_barco1=jugador1.colocarBarcos(mi_tablero , 5)  # la funcion "colocarBarcos" retorna un objeto barco aquí
mi_barco2=jugador1.colocarBarcos(mi_tablero , 4)
mi_barco3=jugador1.colocarBarcos(mi_tablero , 3)
mi_barco4=jugador1.colocarBarcos(mi_tablero , 3)
mi_barco5=jugador1.colocarBarcos(mi_tablero , 2)

su_barco1=jugador2.colocarBarcos(su_tablero , 5)  # la funcion "colocarBarcos" retorna un objeto barco aquí
su_barco2=jugador2.colocarBarcos(su_tablero , 4)
su_barco3=jugador2.colocarBarcos(su_tablero , 3)
su_barco4=jugador2.colocarBarcos(su_tablero , 3)
su_barco5=jugador2.colocarBarcos(su_tablero , 2)


juego =Barcos.Juego (mi_tablero , su_tablero , jugador1 , jugador2  ,numero_cells=17)
juego.iniciarPartida()
while juego.vencedor() == 0:
    juego.turno += 1
    sum1 = sum([sum([1 if item in ["!", "~"] else 0 for item in lista]) for lista in su_tablero.tablero_lista])
    sum2 = sum([sum([1 if item in ["!", "~"] else 0 for item in lista]) for lista in mi_tablero.tablero_lista])
    print("Turno: ", juego.turno)
    print("Score Jugador 1: ", sum1)
    print("Score Jugador Maquina: ", sum2)


    su_tablero=jugador1.jugar(su_tablero)
    mi_tablero=jugador2.jugar(mi_tablero)
    
if juego.vencedor() == 1 :
    print("Eres el vencedor!!!")
else :
    print("Jugador máquina ha ganado!")

    














#tengo que hacer dos tableros o cuatro tableros??????????????