#Tres en Raya
from random import randrange

def TablerodeJuego(cuadro):
	print("+-------" * 3,"+",sep="")
	for fila in range(3):
		print("|       " * 3,"|",sep="")
		for columna in range(3):
			print("|   " + str(cuadro[fila][columna]) + "   ",end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def MovInicial(cuadro):
	inic = False	
	while not inic:
		mov = input("Ingresa tu movimiento: ") 
		inic = len(mov) == 1 and mov >= '1' and mov <= '9' 
		if not inic:
			print("Movimiento erróneo, intentalo nuevamente") 
			continue
		mov = int(mov) - 1 	
		fila = mov // 3 	
		columna = mov % 3		
		signo = cuadro[fila][columna]	
		inic = signo not in ['O','X'] 
		if not inic:	
			print("¡Campo ocupado, intentalo nuevamente!")
			continue
	cuadro[fila][columna] ='O' 	

def ListaCuadVacios(cuadro):
	vacio = []	
	for fila in range(3): 
		for columna in range(3): 
			if cuadro[fila][columna] not in ['O','X']: 
				vacio.append((fila,columna)) 
	return vacio


def VictoriaGame(cuadro,sign):
	if sign =="X":	
		quien ='yo'	
	elif sign =="O": 
		quien ='tu'	
	else:
		quien = None	
	diagon1 = diagon2 = True  
	for comp in range(3):
		if cuadro[comp][0] == sign and cuadro[comp][1] == sign and cuadro[comp][2] == sign:	
			return quien
		if cuadro[0][comp] == sign and cuadro[1][comp] == sign and cuadro[2][comp] == sign: 
			return quien
		if cuadro[comp][comp] != sign: 
			diagon1 = False
		if cuadro[2 - comp][2 - comp] != sign: 
			diagon2 = False
	if diagon1 or diagon2:
		return quien
	return None

def PriMov(cuadro):
	vacio = ListaCuadVacios(cuadro) 
	cont = len(vacio)
	if cont > 0:	 
		coloc = randrange(cont)
		fila, columna = vacio[coloc]
		cuadro[fila][columna] = 'X'

cuadro = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
cuadro[1][1]='X' 
vacio = ListaCuadVacios(cuadro)
turnoplayer = True 
while len(vacio):
	TablerodeJuego(cuadro)
	if turnoplayer:
		MovInicial(cuadro)
		victoriaDef = VictoriaGame(cuadro,'O')
	else:	
		PriMov(cuadro)
		victoriaDef = VictoriaGame(cuadro,'X')
	if victoriaDef != None:
		break
	turnoplayer = not turnoplayer		
	vacio = ListaCuadVacios(cuadro)

TablerodeJuego(cuadro)
if victoriaDef =='tu':
	print("¡Has ganado!")
elif victoriaDef =='yo':
	print("¡Has perdido!")
else:
	print("¡Empate!")
