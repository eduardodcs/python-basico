n = 0
while n < 2:
    try:
        n = int(input("Digite a qtde de números a serem exibidos: "))
        if n > 1:
            print(f"Serão exibidos {n} números.")
    except:
        print("O número precisar ser um inteiro.")

a = 0
b = 1
print("0, 1", end="")

i = 0
while i < n-2:
    c = a + b
    print(", {}".format(c), end="")
    a = b
    b = c
    i += 1
print("\nFim do programa.")