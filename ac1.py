import math

ano = int(input("Digite um ano: "))
bissexto = (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)
print(f"{ano} é bissexto: {bissexto}")

a = float(input("Digite um numero: "))
b = float(input("Digite um numero: "))
c = float(input("Digite um numero: "))

r = b ** 2 - 4 * a * c

x1 = (-b + math.sqrt(r)) / (2 * a)
x2 = (-b - math.sqrt(r)) / (2 * a)

print ("As raizes são: ", x1, "e", x2)