import sys
import io

# Força o terminal a usar UTF-8 para exibir os textos corretamente
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from algoritmo import gerar_receita_linha
from imagem import ler_imagem, imagem_para_matriz


imagem = ler_imagem("imagens/testes/imagem 3x3.png")

print(imagem)

imagem = imagem.resize((3, 3))

print("Largura:", imagem.width)
print("Altura:", imagem.height)



matriz = imagem_para_matriz(imagem)

print(matriz)


"""imagem = [
    ["preta", "preta", "azul"],      # índice 0
    ["preta", "azul", "azul"],       # índice 1
    ["vermelha", "vermelha", "preta"] # índice 2
]

carreira = 1
for i in range(len(imagem) - 1, -1, -1):
    receita = gerar_receita_linha(imagem[i])

    print("Carreira", carreira, ":", receita)

    carreira += 1"""
    
    

