"""Recebe uma linha da matriz de cores e gera a receita utilizando
    a técnica Run-Length Encoding (RLE)"""

def gerar_receita_linha(linha):
    receita = []
    cor_atual = linha[0]
    contador = 1
    
    for i in range(1, len(linha)):
        
        if linha[i]== cor_atual:
            contador+=1

        else: 
            receita.append(str(contador) +"x "+ cor_atual)
            cor_atual = linha[i]
            contador = 1
        
    receita.append(str(contador) +"x "+ cor_atual)
    #técnica run-length Encoding-RLE
    return ", ".join(receita)


"""Percorre todas as linhas da imagem de baixo para cima e gera
    a receita completa."""

def gerar_receita_imagem(matriz):

    carreira = 1

    for i in range(len(matriz) -1, -1, -1):
        receita = gerar_receita_linha(matriz[i])

        print("Carreira", carreira, ":", receita)

        carreira +=1