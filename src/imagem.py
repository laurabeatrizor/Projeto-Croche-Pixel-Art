from PIL import Image

PALETA = {
    "verde": (163, 208, 201),
    "branco": (255,255,255)
}



def ler_imagem(caminho):

    imagem = Image.open(caminho)

    return imagem

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



def identificar_cor(rgb):
    menor_distancia = 999999
    cor_escolhida = ""

    for nome, valor in PALETA.items():
        print(nome, valor)

        if distancia < menor_distancia:
            menor_distancia = distancia

            cor_escolhida = nome

            return cor_escolhida


    if rgb == PALETA["verde"]:
        return "verde"

    else:
        return "branco"

    