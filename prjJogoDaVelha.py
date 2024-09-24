#+------------------------------------------------+
#| Projeto Jogo da Velha                          |
#| autor: Bruno Gontijo                           |
#| descrição: jogo da velha para aprender phyton. |
#| data inicio: 15/03/24                          | 
#| data fim: 05/06/24                             |
#+------------------------------------------------+-------------

from velhaFuncUtil import *
from velhaDAO import * 
from velhaMSG import *
from velhaDAO import *
#|+-------------------------------------+
#|+-Inicialização de Variaveis Globais--|
#|+-------------------------------------+
board = ['_'] * 9
nome_do_jogador=''
caractere=''
modo_de_jogo=''
pontuacao_vitoria = 500
pontuacao_empate = 250
pontos_X = 0
pontos_O = 0

# Inicia as variáveis de controle dos jogadores
player_atual = ""


#Informações iniciais para o jogador

print(bem_vindo_msg)
print(mapa_board_msg)
opcao=int(input(escolha_Solo_Mult_msg))

#-------------------------------------------
# Loop Solo do jogo ("Contra a maquina")
#----------------------------------------
if opcao ==1:
  modo_de_jogo='S'
  caractere='X'
  nome_do_jogador=input('Como você gostaria de ser chamado ? ')
 
  #Escolha do Usuario
  while True:
    escolha=int(input('\n'+nome_do_jogador + ' Qual é sua escolha ? '))
    while board[escolha-1] != '_':
      print('Essa casa já foi escolhida antes!')
      imprime_board(board)
      escolha=int(input('\n'+nome_do_jogador + ' Qual é sua escolha ? '))
    
    board[escolha-1]='X'
    
    ganhador = verifica_vencedor(board)
    if( ganhador != ''):
      print(nome_do_jogador+' Venceu jogando com o X, ganhou '+ str(pontuacao_vitoria)+" pontos, no modo:"+ modo_de_jogo)
      pontos_X = pontos_X + pontuacao_vitoria
      imprime_board (board)
      print('\nFim de jogo!')
      
    
      con=int(input('Digite 0 para continuar ou digite 1 para cancelar '))
      if con ==0:
        board = ['_'] * 9
        print(pontos_X, pontos_O)
        continue
      
      if con==1:
        if pontos_X > pontos_O:
            pontuacao=pontos_X
        else:
          pontuacao=pontos_O
        script_insert(nome_do_jogador,pontuacao,caractere,modo_de_jogo)
        break
    
    #Escolha do Computador

    escolha_comput=random.randint(1,9)
    #print(escolha_comput)
    ct_fim = 0
    while board[escolha_comput-1] != '_':
      escolha_comput=random.randint(1,9)
      #Verificação de empate 
      empatou=empate(board)
      if empatou:

        imprime_board(board)

        con=int(input('\nNinguém venceu!Digite 0 para continuar ou digite 1 para cancelar '))     
        if con ==0:
          
          board = ['_'] * 9
          print(pontos_X, pontos_O)
          continue
        #Insert 
        if con==1:
          if pontos_X > pontos_O:
            pontuacao=pontos_X
          else:
            pontuacao=pontos_O
          script_insert(nome_do_jogador,pontuacao,caractere,modo_de_jogo)
          break
    
     
    board[escolha_comput-1]='O'

    
    #
    #Etapa de verificação e somatorio da pontuação
    #
    
    #Verificador de Vitoria
    ganhador = verifica_vencedor(board)
    if( ganhador != ''):
      print(nome_do_jogador+' Venceu jogando com o O ganhou '+ str(pontuacao_vitoria)+" pontos, no modo:"+ modo_de_jogo)
      pontos_O = pontos_O + pontuacao_vitoria
      imprime_board (board)
      print('\nFim de jogo!')
        
      con=int(input('Digite 0 para continuar ou digite 1 para cancelar '))
      if con ==0:
        board = ['_'] * 9
        print(pontos_X, pontos_O)
        continue
      
      if con==1:
        if pontos_X > pontos_O:
          pontuacao=pontos_X
        else:
          pontuacao=pontos_O
        script_insert(nome_do_jogador,pontuacao,caractere,modo_de_jogo)
        break
  
    imprime_board(board) 

#-------------------------+
# Etapa de multiplayer    |
#-------------------------+-----------
elif opcao == 2:
  modo_de_jogo='M'
  player_inicial =''
      
  # Seta jogador atual sendo X ou O
  print('Digite 0 para X ou 1 para O')
  player=int(input())
  if player == 0:
    player_atual = "X"
  else:
    player_atual = "O"
  player_inicial = player_atual
  
  # Loop multiplayer - rotina principal 
  while True:
    print('\nJogada do', player_atual , ', qual a sua escolha ?')
    escolha = int(input())
    while board[escolha-1]!='_':
      print('Essa casa já foi escolhida antes!')
      imprime_board(board)
      escolha=int(input('\nEscolha novamente? '))
    board[escolha-1] = player_atual

    #+------------------+
    #+ Troca o jogador  |
    #+------------------+
    if player_atual=='X':
      player_atual = 'O'
    else: 
      player_atual = 'X'
      
    #+------------------------------------------+      
    #+Verifica vencedor do modolo multiplayer   |
    #+------------------------------------------+     
    ganhador = verifica_vencedor(board)
    if( ganhador != ''):
      if ganhador =='X':
        pontos_X = pontos_X + pontuacao_vitoria
      else:
        pontos_O = pontos_O + pontuacao_vitoria

      print(nome_do_jogador+' Venceu jogando com o '+ganhador+ ' ganhou '+ str(pontuacao_vitoria)+" pontos, no modo:"+ modo_de_jogo) 
      imprime_board (board)
      print('\nFim de jogo!')

      con=int(input('Digite 0 para continuar ou digite 1 para cancelar '))
      if con ==0:
        board = ['_'] * 9
        player_atual = player_inicial
        print(pontos_X, pontos_O)
        continue
      if con==1:
        nome_do_jogador=input('Ganhador, escreva como quer ser chamado')
        if pontos_X > pontos_O:
          pontuacao=pontos_X
          caractere='X'
        else:
          pontuacao=pontos_O
          caractere='O'
        script_insert(nome_do_jogador,pontuacao,caractere,modo_de_jogo)
        break

    #Verifica empate do modolo multiplayer   |   
    empatou=empate(board)
    if empatou:
      pontos_X = pontos_X + pontuacao_empate
      pontos_O = pontos_O + pontuacao_empate
      con=int(input('\nNinguém venceu!Digite 0 para continuar ou digite 1 para cancelar '))     
      if con ==0:
        board = ['_'] * 9
        player_atual = player_inicial
        print(pontos_X, pontos_O)
        continue
      if con==1:
        nome_do_jogador=input('Ganhador, escreva como quer ser chamado')
        if pontos_X > pontos_O:
          pontuacao=pontos_X
          caractere='X'
        else:
          pontuacao=pontos_O
          caractere='O'
        script_insert(nome_do_jogador,pontuacao,caractere,modo_de_jogo)
        break

    imprime_board(board)

elif opcao ==3:
  placar=retorna_placar()
  print("Jogadores    Pontuação     Tipo    Modo")
  for jogador in placar:
    nome_do_jogador = jogador[0]
    pontuacao = jogador[1]
    caractere = jogador[2]
    modo_de_jogo = jogador[3]
    print(nome_do_jogador +'  '+ str(pontuacao) +'          '+ caractere +'       '+ modo_de_jogo)
  