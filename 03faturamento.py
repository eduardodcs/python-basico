produtos = ["Boneco Malandrinho", "Spinner Pequeno", "Cubo Mágico"]
quantidades = [17, 36, 7]
precos = [18.5, 12, 5.9]
fatProduto = []
i=0
fatTotal=0

for x in range(3):
    fatProduto.append(quantidades[i]*precos[i])
    fatTotal+=fatProduto[i]
    print("{} : {:.2f}".format(produtos[i], fatProduto[i]))
    i+=1
print("Faturamento Total: {:.2f}".format(fatTotal))

