#Função vai servir para evitar repetição de codigo
def calcula_tx_restituicao(renda):
    if renda <= 1000:
        return 0.3
    if renda <= 2000:
        return 0.2
    return 0.1
#print(calcula_tx_restituicao(1500))
#0.2

def calcula_restituicao():
    renda = float(input("Informe sua renda: "))
    tx = calcula_tx_restituicao(renda)
    print("Destituição: ", tx * renda)
    
calcula_restituicao()
print("Fim")