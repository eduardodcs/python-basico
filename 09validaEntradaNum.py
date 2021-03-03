'''
Validando a entrada de dados numéricos
Escreva um programa em python que leia um string que deve conter obrigatoriamente,
um número inteiro e, caso isso não aconteça, emita uma mensagem de erro.
'''

s = input("Digite um número inteiro: ")
if s.isnumeric():
    n = int(s)
    print(f"O número digitado foi {n}.")
else:
    print(f"Digite apenas números.")