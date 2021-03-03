'''
Receber quantidade de linhas e colunas depois gerar números aleatórios para criar uma matriz
'''

from random import randint

Lin = int(input("Quantidade de linhas: "))
Col = int(input("Quantidade de colunas: "))

M = []
i = 0
while i < Lin:
    M.append([])
    j = 0
    while j < Col:
        M[i].append(randint(0, 20))
        j+=1
    i+=1
print("\nEsta é a lista M gerada: ")
print(f"M = {M}")
print("\nExibindo como Matriz: ")
i = 0
while i < Lin:
    j = 0
    print("|", end=" ")
    while j < Col:
        print(f"{M[i][j]:4}", end=" ")
        j+=1
    print("|")
    i+=1
    