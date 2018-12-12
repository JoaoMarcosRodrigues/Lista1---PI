import matplotlib.pyplot as plt
import cv2
import numpy as np
import copy
import os

########################################
#
# Nome: João Marcos de Oliveira Rodrigues
# Matricula: 201600091952
# E­mail: joaomarcosoliveirarodrigues@hotmail.com
#
# Nome:
# Matricula:
# E­mail:
#
########################################

# Q.02
def imread(arquivo):
    imagem = plt.imread(arquivo,np.ndarray)
    plt.imshow(imagem)
    plt.title('Imagem')
    plt.show()

# Q.03
def nchannels(imagem):
    ler = plt.imread(imagem)
    print("Canais: {}".format(ler.shape[2]))

# Q.04
def size(imagem):
    ler = plt.imread(imagem)
    vetor = [ler.shape[1],ler.shape[0]]
    print('Largura x altura: ',vetor)

# Q.05
def rgb2gray(imagem):
    ler = plt.imread(imagem)
    cinza = np.dot(ler[..., :3], [0.299, 0.587, 0.114])
    plt.imshow(cinza, cmap='gray')
    plt.show()

# Q.06
def imreadgray(arquivo):
    imagem = cv2.imread(arquivo,0)
    plt.imshow(imagem,cmap='gray')
    plt.title='Imagem em preto e branco'
    plt.show()

# Q.07
def imshow(arquivo):
    imagem = plt.imread(arquivo)
    if (imagem.shape[2] == 1):
        plt.imshow(imagem,cmap='gray',interpolation='nearest')
    else:
        plt.imshow(imagem,interpolation='nearest')
    plt.show()

# Q.08
def thresh(arquivo,limiar):
    imagem = plt.imread(arquivo);
    altura = imagem.shape[0];
    largura = imagem.shape[1];
    for i in range(altura):
        for j in range(largura):
            for k in range(3):
                if(imagem[i][j][k] >= limiar):
                    imagem[i][j][k] = 255;
                else:
                    imagem[i][j][k] = 0;
    plt.imshow(imagem);
    plt.show();

# Q.09
def negative(imagem):
    copia = imagem[:]
    for linha in range(len(imagem)):
        for coluna in range(len(imagem[0])):
            copia[linha][coluna] = (imagem[linha][coluna] + 1) % 2
    return copia

# Q.10
def contrast(arquivo,r,m):
    imagem = plt.imread(arquivo)
    constrate = sum(np.dot(r,(sum(imagem[i:j:,k],-m))),m)
    plt.imshow(imagem)
    plt.show()

# Q.11
# Q.12
# Q.13
# Q.14
# Q.15
# Q.16
# Q.17
# Q.18
# Q.19
# Q.20
# Q.21
