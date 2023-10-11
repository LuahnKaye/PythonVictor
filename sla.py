letras = ["a","f","x","g","k", "v", "p"]
lista = [1, 2, 3, 4, True, "abc", [1,2,3]]

print(letras[3])
print(letras[-1])

matriz = [
    [10,15],
    [-2, 5],
    [4, 3.5]
]
print(matriz[1][0])
print(matriz[2][1])

print("-"*40)
print(letras[1:4]) # inclui o elemento 1 até o elemento 4, exclusive
print(letras[:4]) # inclui do inicio da lista até o elemento 4, exclusive
print(letras[2:]) # inclui do elemento 2 até o final da lista
print(letras[:]) # exibe a lista inteira
print(letras[2::2]) # inclui do elemento 2 até o final, de 2 em 2 elementos
print(letras[::-1]) # inverte a lista

#operações de pertencimento
print("a" in letras) # true
print("a" not in letras) #false

if "e" in letras:
    print("'e' está em letras.")

#interações
print("-" * 40)
for letra in letras:
    print(letra)
    
for indice, letra in enumerate(letras):
    print(indice, "-", letra)
    
for _, letra in enumerate(letras):
    print(letra)

#operações aritmeticas
print("-" * 40)
print([1,2] + [3,4])
print(8*[0])

#funções metodos
print("-" * 40)
print(len(letras))
letras.append("c")
print(letras)
print(letras.count("a"))
if len(letras) > 0:
    print(letras.pop())
print(letras)
print(letras.pop(4))
print(letras)
if "g" in letras:
    letras.remove("g")
print(letras)

print("-" * 40)
letras_ord = sorted(letras)
print(letras_ord)
print(letras)

print("-" * 40)
print(letras)
letras.sort()
print(letras)
