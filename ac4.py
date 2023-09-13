# exercicio 1
print("Exercicio 1")

def e_primo(num):
    if num <= 1:
        print("O número não é primo!")
        return

    primo = True
    for div in range(2, num):
        if num % div == 0:
            primo = False
    if primo:
        print("O número é primo!")
    else:
        print("O número não é primo!")

numero = 8
e_primo(numero)
print("--------------------------------------")
print("Exercicio 2")
#exercicio 2

def determina_parcela_juros(num_parcelas):
    if num_parcelas == 1:
        parc_juros = 0
    elif num_parcelas == 3:
        parc_juros = 10
    elif num_parcelas == 6:
        parc_juros = 15
    elif num_parcelas == 9:
        parc_juros = 20
    elif num_parcelas == 12:
        parc_juros = 25
    else:
        print("Número de parcelas está inválido")

    return parc_juros

def exibe_dados(divida, num_parcelas):
    tx_juros = determina_parcela_juros(num_parcelas)
    valor_juros = (tx_juros / 100) * divida
    valor_total = divida + valor_juros
    valor_parcela = valor_total / num_parcelas

    print("Valor dos Juros:", valor_juros)
    print("Valor Total:", valor_total)
    print("Quantidade de Parcelas:", num_parcelas)
    print("Valor da Parcela:", valor_parcela)

divida = float(input("Digite o valor da dívida: "))
num_parcelas = int(input("Digite a quantidade de parcelas (1, 3, 6, 9 ou 12): "))

exibe_dados(divida, num_parcelas)

#exercicio 3
print("--------------------------------------")
print("Exercicio 3")
numero = 1
intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0
while numero > 0:
    numero = int(input("Digite um número: "))
    if numero >= 0 and numero <= 25:
        intervalo_0_25 = intervalo_0_25 + 1
    elif numero >= 26 and numero <= 50:
        intervalo_26_50 = intervalo_26_50 + 1
    elif numero >= 51 and numero <= 75:
        intervalo_51_75 = intervalo_51_75 + 1
    elif numero >= 76 and numero <= 100:
        intervalo_76_100 = intervalo_76_100 + 1
print("A quantidade de números entre 0 e 25 é: ", intervalo_0_25) 
print(", entre votos 26-50 é: ", intervalo_26_50) 
print(", entre votos 51-75 é: ", intervalo_51_75) 
print(", e entre votos 76-100 é: ", intervalo_76_100)