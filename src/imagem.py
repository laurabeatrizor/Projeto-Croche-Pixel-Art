from PIL import Image


"""Lê uma imagem utilizando a biblioteca Pillow"""

def ler_imagem(caminho):

    imagem = Image.open(caminho)

    return imagem

"""Converte a imagem em uma matriz contendo o nome da cor de cada pixel."""

def imagem_para_matriz(imagem, linhas, colunas):
    largura_celula = imagem.width / colunas
    altura_celula = imagem.height / linhas
    print("Largura da célula:", largura_celula)
    print("Altura da célula:", altura_celula)

    matriz = []

    for y in range(linhas):

        linha = []

        for x in range(colunas):

            print("Linha:", y, "Coluna:", x)

            #rgb = imagem.getpixel((x, y))

            #cor = identificar_cor(rgb)

            #linha.append(cor)

        matriz.append(linha)

    return matriz

def calcular_distancia(rgb1, rgb2):

    distancia = (
        abs(rgb1[0] - rgb2[0]) +
        abs(rgb1[1] - rgb2[1]) +
        abs(rgb1[2] - rgb2[2])
    )

    return distancia




        




    