from decimal import Decimal
preco = Decimal(input(" Digite o preço do produto: "))
valor_pago = Decimal(input(" Digite o valor pago pelo cliente: "))
troco = valor_pago - preco

if(valor_pago < preco):
    print(" O valor não é suficiente para a compra do produto.")
elif(valor_pago == preco):
    print(" Troco ao cliente é de R$ 0,00.")
else:
    print(f'Troco ao cliente é de R$ {troco}')

    notas = [100, 50, 10, 5, 1]
    vlr = int(troco)
    i = 0

    while vlr != 0:
        c = int(vlr / notas[i])
        if c != 0:
            if c > 1 and notas[i] > 1:
                print(str(c) + ' notas de R$' + str(notas[i]) + ' reais')
                vlr = vlr % notas[i]
            elif c == 1 and notas[i] > 1:
                print(str(c) + ' nota de R$' + str(notas[i]) + ' reais')
                vlr = vlr % notas[i]
            elif c > 1 and notas[i] == 1:
                print(str(c) + ' notas de R$' + str(notas[i]) + ' real')
                vlr = vlr % notas[i]
            else:
                print(str(c) + ' moeda de R$' + str(notas[i]) + ' real')
                vlr = vlr % notas[i]
        i += 1


    centavos = [50, 10, 5, 1]
    vlr = int(round((troco - int(troco)) * 100, 2))
    i = 0
    while vlr != 0:
        c = int(vlr / centavos[i])
        if c != 0:
            if c > 1 and centavos[i] > 1:
                print(str(c) + ' moedas de ' + str(centavos[i]) + ' centavos')
                vlr = vlr % centavos[i]
            elif c == 1 and centavos[i] > 1:
                print(str(c) + ' moeda de ' + str(centavos[i]) + ' centavos')
                vlr = vlr % centavos[i]
            elif c > 1 and centavos[i] == 1:
                print(str(c) + ' moedas de ' + str(centavos[i]) + ' centavo')
                vlr = vlr % centavos[i]
            else:
                print(str(c) + ' moeda de ' + str(centavos[i]) + ' centavo')
                vlr = vlr % centavos[i]
        i += 1