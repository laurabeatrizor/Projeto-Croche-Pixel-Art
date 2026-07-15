import sys
import io

# Força o terminal a usar UTF-8 para exibir os textos corretamente
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#from algoritmo import gerar_receita_linha



linha = ["preta", "preta", "azul", "azul", "azul", "preta"]


cor_atual = linha[0]
contador = 1

for i in range(1,len(linha)):
    if linha[i]== cor_atual:
        contador+=1

    else: 
        print(str(contador) +"x "+ cor_atual)
        cor_atual = linha[i]
        contador = 1
        
print(str(contador) + "x " + cor_atual)

#técnica run-length Encoding-RLE

