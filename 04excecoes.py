try:
    a = int(input("Digite um valor para A: "))
    b = int(input("Digite um valor para B: "))
    r = a/b
    if a < 0:
        c = cos(a)
    print("resultado: R = %.1f" %r)
except ZeroDivisionError:
    print("B não pode ser zero")
except ValueError:
    print("Digite números inteiros para A e B")
except:
    print("Erro desconhecido. Não é possível calcular a divisão")