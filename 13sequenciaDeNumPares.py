'''
Programa que lê um número N e gera uma lista com números pares de 2 até N.
Depois inicar um laço que deve permanecer em execução enquanto x for diferente de zero.
Para cada valor de x informar se está ou não na lista.
'''
print("Pesquisa Sequencial\n")
N = int(input("Digite N: "))
L = list(range(2, N+1, 2))
print(f"Lista Gerada: {L}")

x = int(input("Digite x: "))
while x != 0:
    if x in L:
        print(f"{x} está na lista.")
    else:
        print(f"{x} não está na lista.")
    x = int(input("Digite x: "))

print("Fim do Programa!")