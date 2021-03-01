from random import randint

n = int(input("Digite N: "))
total = 0
i = 1
while i <= n:
    x = randint(1, 50)
    print("Valor {} gerado = {}".format(i, x))
    total+=x
    i+=1
print("\nSoma dos valores gerados = {}".format(total))