


nombre1 = input("Como se llama el jugador 1?")
nombre2 = input("Como se llama el jugador 2?")

jugador1 = input(f"Hola {nombre1}!, Que elijes? piedra papel o tijera?")
jugador2 = input(f"Hola {nombre2}!, Que eliges? Piedra, papel o tijera?")

condicion1 = jugador1 == "piedra" and jugador2 =="tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

if jugador1 == jugador2:
    print("Ha sido un empate!")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado: ", nombre1)
else:
    print("Ha ganado:", nombre2)
    
