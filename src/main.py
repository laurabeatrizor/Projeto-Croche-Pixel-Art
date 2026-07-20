import sys
import io

# Força o terminal a usar UTF-8 para exibir os textos corretamente
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from algoritmo import gerar_receita_linha

imagem = [
    ["preta", "preta", "azul"],      # índice 0
    ["preta", "azul", "azul"],       # índice 1
    ["vermelha", "vermelha", "preta"] # índice 2
]

carreira = 1
for i in range(len(imagem) - 1, -1, -1):
    receita = gerar_receita_linha(imagem[i])

    print("Carreira", carreira, ":", receita)

    carreira += 1