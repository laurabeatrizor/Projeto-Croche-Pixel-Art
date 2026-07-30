# Conversão de Pixel Art para Receitas de Crochê

Projeto desenvolvido como Trabalho de Conclusão de Curso do curso de Análise e Desenvolvimento de Sistemas.

## Objetivo

Desenvolver um algoritmo capaz de converter imagens em Pixel Art em receitas textuais para confecção manual em crochê.

O algoritmo realiza a leitura da imagem, reduz a quantidade de cores utilizando quantização cromática e converte a imagem em uma matriz de pontos, gerando automaticamente instruções por carreiras para a execução do trabalho em crochê.

## Funcionalidades

- Leitura de imagens em Pixel Art.
- Quantização cromática utilizando o algoritmo K-Means.
- Conversão da imagem em uma matriz de pontos.
- Identificação automática das cores predominantes.
- Geração da receita em carreiras utilizando a técnica Run-Length Encoding (RLE).

## Tecnologias Utilizadas

- Python 3
- OpenCV
- NumPy
- Scikit-Learn

## Estrutura do Projeto

```
Projeto Final 2/
│
├── imagens/
│   └── testes/
│
├── src/
│   ├── algoritmo.py
│   ├── processamento.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

## Como executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Execute o programa:

```bash
python src/main.py
```

3. Informe:
   - quantidade de linhas;
   - quantidade de colunas.

O algoritmo irá gerar automaticamente a receita de crochê correspondente à imagem.

## Bibliotecas

- **OpenCV:** leitura e manipulação da imagem.
- **NumPy:** manipulação de matrizes.
- **Scikit-Learn:** aplicação do algoritmo K-Means para quantização das cores.

## Autora

Laura Rosa

Trabalho de Conclusão de Curso – Análise e Desenvolvimento de Sistemas.