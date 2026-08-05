"""
Módulo responsável pela avaliação da similaridade estrutural
entre a imagem original e a imagem processada.
"""

from skimage.metrics import structural_similarity


def calcular_ssim(imagem_original, imagem_processada):
    """
    Calcula o índice de similaridade estrutural entre duas imagens RGB.

    O resultado se aproxima de 1 quando as imagens possuem
    maior similaridade estrutural.
    """

    if imagem_original.shape != imagem_processada.shape:
        raise ValueError(
            "As imagens precisam possuir as mesmas dimensões para calcular o SSIM."
        )

    indice = structural_similarity(
        imagem_original,
        imagem_processada,
        channel_axis=-1,
        data_range=255
    )

    return indice