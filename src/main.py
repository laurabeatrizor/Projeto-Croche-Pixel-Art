import sys
import io

# Força o terminal a usar UTF-8 para exibir os textos corretamente
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from algoritmo import gerar_receita_imagem
from imagem import ler_imagem, imagem_para_matriz

# Lê a imagem
imagem = ler_imagem("imagens/testes/imagem 3x3.png")

# Redimensiona para 3x3 pixels
imagem = imagem.resize((3, 3))

print("Largura:", imagem.width)
print("Altura:", imagem.height)


# Converte a imagem para uma matriz de cores
matriz = imagem_para_matriz(imagem)

# Gera a receita de crochê
gerar_receita_imagem(matriz)



    
    

