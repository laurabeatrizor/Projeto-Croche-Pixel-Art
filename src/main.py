import sys
import io
import numpy as np
from avaliacao import calcular_ssim
from algoritmo import gerar_receita_imagem

# Força o terminal a usar UTF-8 para exibir os textos corretamente
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


from processamento import (
    ler_imagem,
    preparar_pixels,
    quantizar_cores,
    reconstruir_imagem,
    gerar_matriz,
    nomear_cores
)

# Lê a imagem
imagem = ler_imagem("imagens/testes/15x15.png")

# Usuário escolhe o tamanho da receita
linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

#Processamento

pixels = preparar_pixels(imagem)

cores_unicas = np.unique(pixels, axis=0)

quantidade_cores = min(5, len(cores_unicas))

kmeans = quantizar_cores(
    pixels,
    quantidade_cores
)

imagem_quantizada = reconstruir_imagem(kmeans, imagem)

indice_ssim = calcular_ssim(imagem,imagem_quantizada)

matriz = gerar_matriz(
    imagem_quantizada,
    linhas,
    colunas,
    kmeans.cluster_centers_
)

matriz = nomear_cores(matriz, kmeans.cluster_centers_)

"""print("Centros encontrados:")
for centro in kmeans.cluster_centers_:
    print(centro)"""

# Gera a receita
gerar_receita_imagem(matriz)

print()
print(f"Índice SSIM: {indice_ssim:.4f}")










    
    

