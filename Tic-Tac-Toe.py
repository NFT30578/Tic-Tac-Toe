import string, random

tablero = [ [" ", " ", " "],
			[" ", " ", " "],
			[" ", " ", " "]]

def imprimir(tablero):	# imprime el tablero
	horizontal = "+---" *3 + "+"  # lineas horizontales ej: +--+--+--+
	vertical = string.ascii_uppercase[:0] + "\n"
	print(vertical, end="")	# end="" da una cadena de texto vacia
	for fila in tablero:
		print(horizontal)
		print("|", end =" ")
		for cell in fila:
			print(f"{cell} |", end=" ")
		print()
	print(horizontal)

def vaciar_tablero():	# quita los valores dejando el tablero vacio
	for fila in range(len(tablero)):
				for columna in range(len(tablero[fila])):
					tablero[fila][columna] = " "    

def opciones():	# guia para que el jugador sepa cual elegir
	print('1.-Superior_izquierda', '2.-Superior','3.-Super_derecha')
	print('4.-Centro_izquierda' + "   " + '5.-Centro' + "   " + '6.-Centro_derecha')
	print('7.-Inferior_izquierda', '8.-Inferior', '9.-Inferior_derecha')
	print('0.-Salir\n')

def error():	# imprime error cada vez que una jugada sea invalida
	print("---------------------")
	print("ERROR: Campo ocupado")
	print("---------------------")

def maquina(tablero):	# funcion para que se marque un "O" en una ubicacion vacia
	posiciones_vacias = [(fila, columna) for fila in range(3) for columna in  range(3) if tablero[fila][columna] == " "]
	if posiciones_vacias:
		fila, columna = random.choice(posiciones_vacias)
		tablero[fila][columna] = "O"

def hay_ganador(tablero):	# funcion para verificar si hay un ganador
    for fila in tablero:	# Verificar filas
        if fila[0] == fila[1] == fila[2] and fila[0] != " ":
            return fila[0]
    for columna in range(3):	# Verificar columnas
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] and tablero[0][columna] != " ":
            return tablero[0][columna]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":	# Verificar diagonales
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return tablero[0][2]
    return None	# Si no hay ganador

def iniciar(tablero):	# inicio del juego
	imprimir(tablero)
	opciones()
	print("Turno jugador:")
	jugador1 = input("Ingresa un numero:\n")
	posiciones = {  # Mapeo de la entrada del jugador a una posición en el tablero
		"1": (0, 0),
		"2": (0, 1),
		"3": (0, 2),
		"4": (1, 0),
		"5": (1, 1),
		"6": (1, 2),
		"7": (2, 0),
		"8": (2, 1),
		"9": (2, 2)
	}
	if jugador1 in posiciones:	# verifica en el tablero si la eleccion del jugador es una ubicacion vacia
		fila, columna = posiciones[jugador1]
		if tablero[fila][columna] == " ":
			tablero[fila][columna] = "X"
			maquina(tablero)
		else:
			error()	# en caso contrario arroja error
		ganador = hay_ganador(tablero)
		if ganador is not None:	# condicion para verificar si hay ganador
			imprimir(tablero)
			print(f"¡{ganador} ha ganado!\n")
			print("¿Volver a jugar?\n")
			respuesta = input()
			if respuesta == "si":	# una vez que hay ganador pregunta si quiere iniciar otro juego
				vaciar_tablero()
				iniciar(tablero)
			else:
				vaciar_tablero()
				return
		else:
			print("Empate")
			print(("¿Volver a jugar?\n"))
	elif jugador1 == "0":	# la eleccion 0 es finaliza el juego y vacia el tablero
		vaciar_tablero()
		return
	iniciar(tablero)