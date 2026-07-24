from PIL import Image

PALETA = {
    "verde": (163, 208, 201),
    "branco": (216, 230, 225)
}

"""Lê uma imagem utilizando a biblioteca Pillow"""

def ler_imagem(caminho):

    imagem = Image.open(caminho)

    return imagem

"""Converte a imagem em uma matriz contendo o nome da cor de cada pixel."""

def imagem_para_matriz(imagem):
    matriz = []
    for y in range(imagem.height):

        linha = []

        for x in range(imagem.width):

            rgb = imagem.getpixel((x, y))

            cor = identificar_cor(rgb)

            linha.append(cor)

        matriz.append(linha)

    return matriz


"""Identifica a cor mais próxima do pixel comparando com a paleta."""
def identificar_cor(rgb):
    menor_distancia = 999999
    cor_escolhida = ""

    for nome, valor in PALETA.items():

        distancia = (
            abs(rgb[0] - valor[0]) +
            abs(rgb[1] - valor[1]) +
            abs(rgb[2] - valor[2])
        )

        if distancia < menor_distancia:
            menor_distancia = distancia
            cor_escolhida = nome

    return cor_escolhida


    