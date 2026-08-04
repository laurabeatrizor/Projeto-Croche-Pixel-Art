import cv2
import numpy as np
from sklearn.cluster import KMeans


#Módulo responsável pelo processamento da imagem.
PALETA = {
    "branco": np.array([255, 255, 255]),
    "preto": np.array([0, 0, 0]),
    "vermelho": np.array([180, 40, 40]),
    "laranja": np.array([255, 150, 20]),
    "amarelo": np.array([255, 230, 0]),
    "verde": np.array([60, 130, 40]),
    "azul": np.array([30, 80, 220]),
    "marrom": np.array([105, 70, 35])
}

def ler_imagem(caminho):

    #Lê a imagem utilizando OpenCV e converte do padrão BGR para RGB.
    

    imagem = cv2.imread(caminho)
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

    return imagem

def preparar_pixels(imagem):

    #Converte a imagem em uma lista de pixels para utilização no algoritmo K-Means.

    return imagem.reshape((-1,3))

def quantizar_cores(pixels, quantidade_cores):

    #Aplica o algoritmo K-Means para reduzir a quantidade de cores da imagem.

    kmeans = KMeans(
        n_clusters=quantidade_cores,
        random_state=0,
        n_init="auto"
    )

    kmeans.fit(pixels)

    return kmeans

def reconstruir_imagem(kmeans, imagem):

    #Reconstrói a imagem utilizando apenas as cores encontradas pelo K-Means.

    pixels = preparar_pixels(imagem)

    novos_pixels = kmeans.cluster_centers_[kmeans.labels_]

    return novos_pixels.reshape(imagem.shape).astype("uint8")


def gerar_matriz(imagem, linhas, colunas, centros):

    """Divide a imagem em uma grade conforme as
    dimensões informadas pelo usuário e identifica
    a cor predominante de cada célula."""

    altura, largura, _ = imagem.shape

    altura_celula = altura / linhas
    largura_celula = largura / colunas

    matriz = []

    for i in range(linhas):

        linha = []

        for j in range(colunas):

            # Centro da célula
            y = int((i + 0.5) * altura_celula)
            x = int((j + 0.5) * largura_celula)

            pixel = imagem[y, x]

            menor_distancia = float("inf")
            indice = 0

            for k in range(len(centros)):

                distancia = np.linalg.norm(pixel - centros[k])

                if distancia < menor_distancia:
                    menor_distancia = distancia
                    indice = k

            linha.append(indice)

        matriz.append(linha)

    return matriz

def nomear_cores(matriz, centros):

    #Associa cada centro encontrado pelo K-Means a uma cor conhecida da paleta.

    mapa = {}

    for indice, centro in enumerate(centros):

        menor_distancia = float("inf")
        nome_cor = ""

        for nome, rgb in PALETA.items():

            distancia = np.linalg.norm(centro - rgb)

            if distancia < menor_distancia:
                menor_distancia = distancia
                nome_cor = nome

        mapa[indice] = nome_cor

    matriz_nomeada = []

    for linha in matriz:

        nova_linha = []

        for indice in linha:

            nova_linha.append(mapa[indice])

        matriz_nomeada.append(nova_linha)

    return matriz_nomeada