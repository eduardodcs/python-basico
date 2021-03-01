n = int(input("Digite um número inteiro: "))

isPar = (n % 2 == 0)
isPositivo = (n > 0)

if n == 0:
    print("Zero vale né cara !!!")
elif isPar and isPositivo:
    print("O número é PAR e POSITIVO")
elif not isPar and isPositivo:
    print("O número é ÍMPAR e POSITIVO")
elif isPar and not isPositivo:
    print("O número é PAR e NEGATIVO")
else:
    print("O número é ÍMPAR e NEGATIVO")

