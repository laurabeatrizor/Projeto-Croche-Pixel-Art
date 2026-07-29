import cv2
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter

PALETA = {
    "branco": np.array([255, 255, 255]),
    "preto": np.array([0, 0, 0]),
    "vermelho": np.array([255, 0, 0]),
    "azul": np.array([0, 0, 255]),
    "amarelo": np.array([255, 255, 0])
}


def ler_imagem(caminho):

    imagem = cv2.imread(caminho)
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

    return imagem

def preparar_pixels(imagem):

    return imagem.reshape((-1,3))

def quantizar_cores(pixels, quantidade_cores):

    kmeans = KMeans(
        n_clusters=quantidade_cores,
        random_state=0,
        n_init="auto"
    )

    kmeans.fit(pixels)

    return kmeans

def reconstruir_imagem(kmeans, imagem):

    pixels = preparar_pixels(imagem)

    novos_pixels = kmeans.cluster_centers_[kmeans.labels_]

    return novos_pixels.reshape(imagem.shape).astype("uint8")


def gerar_matriz(imagem, linhas, colunas, centros):

    altura, largura, _ = imagem.shape

    altura_celula = altura // linhas
    largura_celula = largura // colunas

    matriz = []

    for i in range(linhas):

        linha = []

        for j in range(colunas):

            y1 = i * altura_celula
            y2 = (i + 1) * altura_celula

            x1 = j * largura_celula
            x2 = (j + 1) * largura_celula

            celula = imagem[y1:y2, x1:x2]

            # Ignora aproximadamente 20% da borda
            margem_y = celula.shape[0] // 5
            margem_x = celula.shape[1] // 5

            centro = celula[
                margem_y:celula.shape[0]-margem_y,
                margem_x:celula.shape[1]-margem_x
            ]

            votos = []

            for linha_centro in centro:
                for pixel in linha_centro:

                    distancias = []

                    for c in centros:
                        distancias.append(np.linalg.norm(pixel-c))

                    indice = np.argmin(distancias)

                    votos.append(indice)

            indice_vencedor = Counter(votos).most_common(1)[0][0]

            linha.append(indice_vencedor)

        matriz.append(linha)

    return matriz

def nomear_cores(matriz, centros):

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