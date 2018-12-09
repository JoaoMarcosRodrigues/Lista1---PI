import copy
import matplotlib.pyplot as plt
import os

def negative(imagem):
    ler = plt.imread(imagem)
    altura = ler.shape[1]
    largura = ler.shape[0]
    copia = ler[:]
    for linha in range(largura):
        for coluna in range(altura):
            copia[linha,coluna] = (ler[linha,coluna]+1)%2
    plt.imshow(copia)
    plt.show()

os.chdir('imagens')
imagem = os.listdir('.')
arquivo = input('Imagem de entrada: ')
imagem = arquivo

negative(imagem)