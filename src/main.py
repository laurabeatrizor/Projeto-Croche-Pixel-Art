import sys
import io

# Força o terminal a usar UTF-8 para exibir os textos corretamente
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from algoritmo import gerar_receita_linha



linha = ["preta", "preta", "azul", "azul", "azul", "preta"]


resultado = gerar_receita_linha(linha)

print(resultado)