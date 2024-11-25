"""
Jogo da velha projetado para treinar a lógica de programação e treinar a mente para resolver problemas!!!!
"""
import os
import time
cerquilha_original:list[str]=["%s|%s|%s"% ('1','2','3'),"%s|%s|%s"% ('4','5','6'),"%s|%s|%s"% ('7','8','9')]
cerquilha:list[str]=cerquilha_original.copy()
jogadores=['X','O']

#função responsável por mostrar a cerquilha aos jogadores
def mostrar_cerquilha():
  os.system('cls')
  for linha in cerquilha:
    print(linha)

#função que responsável por inserir o jogador na tabela
def inserir_valor_cerquilha(valor:str,jogador:str)->bool:
  if not valor.isdigit():
    print('O número digitado não é um número inteiro.\n')
    return False

  valor_int=int(valor)

  if valor_int>=1 and valor_int<=9:
    global cerquilha
    
    if valor in ''.join(cerquilha):
      cerquilha=[i.replace(valor,jogador) if valor in i else i for i in cerquilha ]
      return True
    else:
        print(f'{valor} já foi inserido,coloque um que está mostrando na cerquilha.')
        return False
  else:
    print('Esse valor não existe na cerquilha.\n')
    return False

def checar_empate():
  global cerquilha
  #checando se houve empate, se houver empate aí irá retornar True, senão False
  for i in cerquilha:
    for k in i:
      if k.isdigit():
        return False
    
    if i == cerquilha[-1]:
      #aqui deu empate
      return True
def checar_vitoria(jogador:str):

  # X|X|X
  # 4|5|6
  # 7|8|9
  if cerquilha[0]==f'{jogador}|{jogador}|{jogador}':
    return True
  # 1|2|3
  # X|X|X
  # 7|8|9
  elif cerquilha[1]==f'{jogador}|{jogador}|{jogador}':
    return True
  # 1|2|3
  # 4|5|6
  # X|X|X
  elif cerquilha[2]==f'{jogador}|{jogador}|{jogador}':
    return True
  # X|2|3
  # X|5|6
  # X|8|9
  elif cerquilha[0][0]==jogador and cerquilha[1][0]==jogador and cerquilha[2][0]==jogador:
    return True
  # 1|X|3
  # 4|X|6
  # 7|X|9
  elif cerquilha[0][2]==jogador and cerquilha[1][2]==jogador and cerquilha[2][2]==jogador:
    return True
  # 1|2|X
  # 4|5|X
  # 7|8|X
  elif cerquilha[0][4]==jogador and cerquilha[1][4]==jogador and cerquilha[2][4]==jogador:
    return True
  # X|2|3
  # 4|X|6
  # 7|8|X
  elif cerquilha[0][0]==jogador and cerquilha[1][2]==jogador and cerquilha[2][4]==jogador:
    return True
  # 1|2|X
  # 4|X|6
  # X|8|9
  elif cerquilha[0][4]==jogador and cerquilha[1][2]==jogador and cerquilha[2][0]==jogador:
    return True
  return False

print("Você acaba de entrar no jogo da velha, feita por Erick.")

print("Nesse jogo insira somente números. Lembrando que só podera inserir os que estão vagos.")
input('Pressione qualquer tecla para começar\n')

jogador=jogadores[0]
while True:

  mostrar_cerquilha()
  escolha=input("Jogador '{}' é a sua vez: \n".format(jogador))
  inserido=inserir_valor_cerquilha(escolha,jogador)

  if not inserido:
    time.sleep(4)
    continue

  if checar_empate():
    if escolha_continuar.lower().strip()=='s':
      cerquilha=cerquilha_original.copy()
      continue
    print('Deu empate')
    break
  
  if checar_vitoria(jogador):
    print(f'Jogador "{jogador}" ganhou essa partida.\n')
    print(f'Parabéns jogador {jogador}!!!!!!!!!')
    escolha_continuar=input('Deseja jogar mais uma vez? S/N\n')
    if escolha_continuar.lower().strip()=='s':
      cerquilha=cerquilha_original.copy()
      continue
    break

  #aqui estou trocando de jogador antes da próxima iteração
  if jogador==jogadores[0]:
    jogador=jogadores[1]
  else:
    jogador=jogadores[0]