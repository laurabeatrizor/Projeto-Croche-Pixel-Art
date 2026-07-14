import sys
import io

# Força o terminal a usar UTF-8 para exibir os textos corretamente
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

imagem = [
    ["preta", "preta", "azul"],
    ["preta", "azul", "azul"],
    ["vermelha", "vermelha", "preta"]
]

linha = ["preta", "preta", "azul", "azul", "azul", "preta"]


cor_atual = linha[0]
contador = 1

for i in range(1,len(linha)):
    print(i)

if linha[1] == cor_atual:
    contador+=1

def soma(a, b):
    return a + b


resultado = soma(3, 4)
print(resultado) 