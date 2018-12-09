import cv2
import matplotlib.pyplot as plt
import os

def thresh(imagem):
    ler = cv2.imread(imagem)
    imagem_shape = ler.shape
    altura = imagem_shape[0]
    largura = imagem_shape[1]

    for linha in range(largura):
        for coluna in range(altura):
            (b, g, r) = ler[coluna,linha]
    if (b == g and b == r):
        ler = cv2.imread(imagem,0)
        plt.imshow(ler,cmap='gray',interpolation='nearest')
    ler = plt.imread(imagem)
    plt.imshow(ler,interpolation='nearest')
    plt.show()

os.chdir('imagens')
os.listdir('.')
imagem = os.listdir('.')
arquivo = input('Imagem de entrada: ')
imagem = arquivo

thresh(imagem)
