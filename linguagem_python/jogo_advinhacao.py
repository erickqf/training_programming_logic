# Exercício: Jogo de Adivinhação em Python
# Objetivo: Criar um jogo onde o usuário deve adivinhar um número gerado aleatoriamente pelo programa dentro de um intervalo pré-definido.

# Instruções:

# O programa deve gerar um número aleatório entre 1 e 100. Use a função random.randint() para isso.
# O usuário terá 5 tentativas para adivinhar o número correto.
# Após cada palpite, o programa deve fornecer um feedback, dizendo se o palpite foi:
# Muito alto
# Muito baixo
# Correto
# Se o usuário acertar o número, o programa deve exibir uma mensagem de parabéns e encerrar o jogo.
# Se o usuário esgotar todas as tentativas e não acertar, o programa deve revelar o número correto.
# Opcional: Adicione um sistema de pontuação, onde o usuário ganha mais pontos se acertar com menos tentativas.
# Requisitos:

# Use a função random.randint() para gerar o número secreto.
# Use input() para capturar o palpite do usuário.
# Utilize um loop while para controlar as tentativas.
# Utilize condicionais if/else para comparar o palpite com o número gerado.
# Dicas:

# Lembre-se de diminuir o número de tentativas a cada palpite.
# No final, exiba uma mensagem dizendo se o usuário venceu ou perdeu.
# Desafio Extra:
# Adapte o jogo para permitir que o usuário escolha a faixa de números (por exemplo, entre 1 e 50, ou 1 e 1000).
from secrets import SystemRandom

random=SystemRandom()
#número escolhido
chosen_number=random.randint(1,100)
#tentativas que o jogador terá
attempts=5

def verify_guess(player_number:str)->bool:
    def check_if_it_is_int(number_str:str)->int:
        if not number_str.isdigit():
            raise ValueError('Insira somente números inteiros EX: 10')
        
        number_int=int(number_str)
        return number_int
    player_number_int=check_if_it_is_int(player_number)
    if player_number_int ==chosen_number:
        print('Parabéns, você acertou!')
        return True
    elif player_number_int< chosen_number:
        print('O número digitado é menor que o número escolhido.')
        return False
    else:
        print('O número digitado é maior que o número escolhido.')
        return False

print(f'Olá, você tem {attempts} tentativas nesse jogo de advinhação.')
print(f'Escolha um número de 1 até 100. Insira somente números.')
print(chosen_number)
print()

while attempts>0:
    print()
    guess=input('Insira seu palpite: ')

    check_victory=verify_guess(guess)
    if check_victory:
        break
    #quando o jogador fazer seu palpite aí ele irá subtrair 1 tentativa
    attempts-=1
    print(f'Você tem mais {attempts} tentativas')
    if attempts==0:
        print(f'O número escolhido era {chosen_number}')