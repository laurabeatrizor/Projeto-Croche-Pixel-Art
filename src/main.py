import sys
import io
import cv2
import numpy
import sklearn

# Força o terminal a usar UTF-8 para exibir os textos corretamente
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from algoritmo import gerar_receita_imagem
from imagem import ler_imagem, imagem_para_matriz

# Lê a imagem
imagem = ler_imagem("../imagens/testes/11x11.png")

# Redimensiona para pixels
linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))


# Converte a imagem para uma matriz de cores
matriz = imagem_para_matriz(imagem, linhas, colunas)

# Gera a receita de crochê
gerar_receita_imagem(matriz)



    
    

