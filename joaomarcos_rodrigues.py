import matplotlib.pyplot as plt
import cv2
import numpy as np
import math
import copy
import os

########################################
#
# Nome: João Marcos de Oliveira Rodrigues
# Matricula: 201600091952
# E-mail: jmorodrigues@dcomp.ufs.br
#
# Nome: Rivanildo Júnior dos Santos Andrade
# Matricula: 201600092477
# E-mail: rivanildo.andrade@dcomp.ufs.br
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
    copia = ler.copy()
    cinza = np.dot(copia[..., :3], [0.299, 0.587, 0.114])
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
    copia = imagem.copy()
    altura = imagem.shape[0];
    largura = imagem.shape[1];
    for i in range(altura):
        for j in range(largura):
            for k in range(3):
                if(imagem[i][j][k] >= limiar):
                    copia[i][j][k] = 255;
                else:
                    copia[i][j][k] = 0;
    plt.imshow(copia);
    plt.show();

# Q.09
def negative(imagem):
    copia = imagem[:]
    for linha in range(len(imagem)):
        for coluna in range(len(imagem[0])):
            copia[linha][coluna] = (imagem[linha][coluna] + 1) % 2
    return copia

# Q.10
def contrast(imagem, r, m):
    novaImagem = imagem.copy()
    tamImagem = size(imagem)
    if (nchannels(imagem) == 1):
        for x in range(0, tamImagem[0]):
            for y in range(0, tamImagem[1]):
                result = truncate( r * (imagem[x][y] - m) + m)
                novaImagem[x][y] = result
    else:
        for x in range(0, tamImagem[0]):
            for y in range(0, tamImagem[1]):
                for k in range(0, 3):
                    result = truncate( r * (imagem[x][y][k] - m) + m)
                    novaImagem[x][y][k] = result
    return novaImagem

# Q.11
def hist(imagem, result):
    tamImagem = size(imagem)
    if (nchannels(imagem) == 1):
        result = [0] * 256
        for x in range(0, tamImagem[0]):
            for y in range(0, tamImagem[1]):
                result[imagem[x][y]] += 1
        return result
    else:
        result[[0] * 256, [0] * 256, [0] * 256]
        for x in range(0, tamImagem[0]):
            for y in range(0, tamImagem[1]):
                for k in range(0, 3):
                    result[k][imagem[x][y][k]] += 1
        return result

# Q.12
def showhist(resultHist):
    if(len(resultHist) == 1):
        plt.hist(resultHist, 50, density=True, facecolor='g', alpha=0.75)
    else:
        plt.hist(resultHist[0], 50, density=True, facecolor='g', alpha=0.75)
        plt.hist(resultHist[1], 50, density=True, facecolor='g', alpha=0.75)
        plt.hist(resultHist[2], 50, density=True, facecolor='g', alpha=0.75)
    plt.show()

#Q.15
def convolve(imagem,mask):
    ler = plt.imread(imagem)
    convolucao = np.convolve(ler,mask,mode='full')
    plt.imshow(ler)
    plt.show()

# Q.16
def maskBlur():
    return (1/16) * np.asarray([[1,0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])

# Q.17
def (imagem):
    return convolve(imagem, maskBlur())

# Q.18
def seSquare3():
    return np.asarray([[1, 1, 1],[1, 1, 1],[1, 1, 1]]).astype(np.uint8)

# Q.19
def seCross():
    return np.asarray([[0, 1, 0], [1, 1, 1]]).astype(np.uint8)

