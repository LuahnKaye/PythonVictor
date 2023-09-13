"" 
1.
salario= float(input("Digite o salário atual do colaborador: "))

def reajuste(salario):
    if salario <= 280.00:
        percentual_aumento = 20
    elif salario <= 700.00:
        percentual_aumento = 15
    elif salario <= 1500.00:
        percentual_aumento = 10
    else:
        percentual_aumento = 5

    aumento = (percentual_aumento / 100) * salario
    novo_salario = salario + aumento

    return salario, percentual_aumento, aumento, novo_salario

def mostrar_resultado(salario, percentual_aumento, aumento, novo_salario):
    print("Salário antes do reajuste: R$", salario)
    print("Percentual de aumento aplicado:", percentual_aumento, "%")
    print("Valor do aumento: R$", aumento)
    print("Novo salário após o aumento: R$", novo_salario)
    
resultado =reajuste(salario)
mostrar_resultado(*resultado) 


2. 

def dia_da_semana(num):
        if num == 1:
            return "Domingo"
        elif num == 2:
            return "Segunda-feira"
        elif num == 3:
             return "Terça-feira"
        elif num == 4:
             return "Quarta-feira"
        elif num == 5:
             return "Quinta-feira"
        elif num == 6:
             return "Sexta-feira"
        elif num == 7: 
             return "Sábado"
        else: 
             return "Valor inválido"
        
numero = int(input("Digite um número de 1 a 7: "))
resultado = dia_da_semana(numero)
print(resultado)

3. 
import math 

a = float(input("Digite o valor de a: "))
if a == 0:
    print("A equação não é do segundo grau. Encerrando o programa.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b ** 2 - 4 * a * c 
if delta < 0 :

    print (" não há raizes reais que satisfazem a equação ")

else: 
    x1 = (-b + math.sqrt (delta)) / (2 * a)
    x2 = (-b - math.sqrt (delta)) / (2 * a)

    print (f"a raiz x1 = {x1} ")
    print (f"a raiz x2 = {x2} ")
            