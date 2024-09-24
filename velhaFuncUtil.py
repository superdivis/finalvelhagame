import random

#+------------------------------------+
#| Imprime o board do jogo no console |
#+------------------------------------+
def imprime_board(board):
  for indice in range(len(board)):
    print(board[indice], end=' ')
    if indice ==2 or indice ==5 or indice ==9:
      print('')

#+--------------------------+
#| Verifica se tem vencedor |
#+--------------------------+
def verifica_vencedor(board):
  retorno = ''
  linha1 = board[0:3]
  linha2 = board[3:6]
  linha3 = board[6:9]
  coluna1 = [board[0],board[3],board[6]]
  coluna2 = [board[1],board[4],board[7]]
  coluna3 = [board[2],board[5],board[8]]
  diagonal1 = [board[0],board[4],board[8]]
  diagonal2 = [board[2],board[4],board[6]]
  linhaX = ['X','X','X'] 
  linhaO = ['O','O','O']
  if linha1 == linhaX or linha2 == linhaX or linha3 == linhaX:
    retorno = 'X'
  if coluna1 == linhaX or coluna2 == linhaX or coluna3 == linhaX:
    retorno = 'X'
  if diagonal1 == linhaX or diagonal2 == linhaX:
    retorno = 'X'
  if linha1 == linhaO or linha2 == linhaO or linha3 == linhaO:
    retorno = 'O'  
  if coluna1 == linhaO or coluna2 == linhaO or coluna3 == linhaO:
    retorno = 'O'
  if diagonal1 == linhaO or diagonal2 == linhaO:
    retorno = 'O'
  return retorno

#+------------------------+
#| Verifica se tem empate |
#+------------------------+
def empate(board):
    ret=True
    for empate in (board):
        if empate == '_':
            ret=False 
    return ret