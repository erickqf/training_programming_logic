"""
Exercício: Calculadora de Números Primos
Objetivo: Criar um programa em Python que analise se um número é primo e, se solicitado pelo usuário, exiba todos os números primos dentro de um intervalo fornecido.
"""
def check_if_is_prime(num:int):
    for i in range(2,num):
        sobra=num%i
        if sobra==0:# não é numero primo
            return False
    return True #é número primo

print("Calculadora de Números Primos")
prime_number=int(input("Enter an integer: "))

prime=check_if_is_prime(prime_number)

if prime:
    print(f'The number {prime_number} is prime!')
else:
    print(f'The number {prime_number} is not prime.')

choice=input("Want to see all prime numbers in a range? (Y/N):")

if choice.lower().strip()=='y':
    start=int(input('Enter the start of the range:'))
    stop=int(input('Enter the end of the range:'))
    numbers_prime=[]
    for i in range(start,stop+1):
        prime=check_if_is_prime(i)
        if prime:
            numbers_prime.append(i)

    print(f"The prime numbers between {start} and {stop} are: {' '.join(map(str,numbers_prime))}")
