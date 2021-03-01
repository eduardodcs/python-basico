print("Cálculo de salário com comissão (6%)")
salarioFixo = float(input("Digite o salário do vendedor: "))
vendas = float(input("Digite o total vendido no mês: "))
vComissao = vendas * 0.06
salarioMes = salarioFixo + vComissao
print("O vendedor receberá {:.2f} de salário mais {:.2f} de comissão. Total {:.2f}".format(salarioFixo, vComissao, salarioMes))
