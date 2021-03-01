n = 0
while n < 100 or n > 500:
    try:
        s = input("Digite N no intervalo [100,500]: ")
        n = int(s)
    except:
        print("'{}' não é um número.".format(s))
        n = 0
    else:
        if n < 100 or n > 500:
            print("O valor lido '{}' está fora do intervalo".format(n))
        else:
            print("O valor lido '{}' está OK".format(n))
    finally:
        print("\n\n")
