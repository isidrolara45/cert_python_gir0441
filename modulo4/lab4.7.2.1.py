'''
Descripcion: PROYECTO: TIC-TAC-TOE
Autor: Isidro Lara López
Fecha: 4 octubre 2022
'''
from random import randrange

def DisplayBoard(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print("+-------" * 3,"+",sep="")
for row in range(3):
		print("|       " * 3,"|",sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ",end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def EnterMove(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    ok = False	# fake assumption - we need it to enter the loop
while not ok:
		move = input("Enter your move: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' 
		if not ok:
			print("Bad move - repeat your input!") 
			continue
		move = int(move) - 1
		row = move // 3 	
		col = move % 3	
		sign = board[row][col]	
		ok = sign not in ['O','X'] 
		if not ok:	
			print("Field already occupied - repeat your input!")
			continue
	board[row][col] = 'O' 	

def MakeListOfFreeFields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
 free = []	
for row in range(3): 
		for col in range(3): 
			if board[row][col] not in ['O','X']: 
				free.append((row,col)) 
    return free


def VictoryFor(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
if sign == "X":	# are we looking for X?
	who = 'me'	# yes - it's computer's side
    elif sgn == "O": # ... or for O?
		who = 'you'	# yes - it's our side
	else:
		who = None	# we should not fall here!
	cross1 = cross2 = True  # for diagonals
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
			return who
		if board[rc][rc] != sgn: # check 1st diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # check 2nd diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None


def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    free = MakeListOfFreeFields(board) # make a list of free fields
	cnt = len(free)
	if cnt > 0:	# if the list is not empty, choose a place for 'X' and set it
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
board[1][1] = 
free = MakeListOfFreeFields(board)
humanturn = True 
while len(free):
	DisplayBoard(board)
	if humanturn:
		EnterMove(board)
		victor = VictoryFor(board,'O')
	else:	
		DrawMove(board)
		victor = VictoryFor(board,'X')
	if victor != None:
		break
	humanturn = not humanturn		
	free = MakeListOfFreeFields(board)

DisplayBoard(board)
if victor == 'you':
	print("You won!")
elif victor == 'me':
	print("I won")
else:
	print("Tie!")
