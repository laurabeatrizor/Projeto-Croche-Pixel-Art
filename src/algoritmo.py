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

