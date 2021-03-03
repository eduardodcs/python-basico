'''
Fazer a leitura de 3 números na mesma linha, separado por espaço, carregar em 3 variáveis
e exibir
'''

s = input("Digite três números inteiros: ")
l = s.split(" ") #carrega a lista separando onde tem o espaço
print(f"Lista L: {l}")
a = int(l[0])
b = int(l[1])
c = int(l[2])

print(f"\nA = {a}, B = {b}, C = {c}")