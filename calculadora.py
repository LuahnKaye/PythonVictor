numero1 = int(input("Digite o valor do primeiro número:"))

while True:
    numero2 = int(input("Digite o valor do segundo número:"))
    
    print("""[1] soma
[2] subtração
[3] multiplicação
[4] divisão
[ENTER] fechar programa""")
    
    escolha = input("Digite o número que você quer para fazer o cálculo:")

    if escolha == "1":
        numero_total = numero1 + numero2
        numero1 = numero_total
        print("O resultado da sua conta é", numero_total)
        continua = input("Deseja continuar com o resultado(c), limpar resultado(X) ou fechar programa(ENTER)?")
        if continua == "x" or continua == "X":
            numero1 = int(input("Digite o valor do primeiro número:"))

        elif continua == "":
            print("Encerrando programa!")
            break

    elif escolha == "2":
        numero_total = numero1 - numero2
        numero1 = numero_total
        print("O resultado da sua conta é", numero_total)
        continua = input("Deseja continuar com o resultado(c), limpar resultado(X) ou fechar programa(ENTER)?")
        if continua == "x" or continua == "X":
            numero1 = int(input("Digite o valor do primeiro número:"))

        elif continua == "":
            print("Encerrando programa!")
            break

    elif escolha == "3":
        numero_total = numero1 * numero2
        numero1 = numero_total
        print("O resultado da sua conta é", numero_total)
        continua = input("Deseja continuar com o resultado(c), limpar resultado(X) ou fechar programa(ENTER)?")
        if continua == "x" or continua == "X":
            numero1 = int(input("Digite o valor do primeiro número:"))

        elif continua == "":
            print("Encerrando programa!")
            break

    elif escolha == "4":
        numero_total = numero1 / numero2
        numero1 = numero_total
        print("O resultado da sua conta é", numero_total)
        continua = input("Deseja continuar com o resultado(c), limpar resultado(X) ou fechar programa(ENTER)?")
        if continua == "x" or continua == "X":
            numero1 = int(input("Digite o valor do primeiro número:"))

        elif continua == "":
            print("Encerrando programa!")
            break

    elif escolha == "":
        print("Encerrando programa!")
        break

    else:
        print("Tente denovo!")
        break