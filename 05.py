import numpy as np
import matplotlib.pyplot as plt
import os

def rgb2gray(imagem):
    ler = plt.imread(imagem)
    cinza = np.dot(ler[..., :3], [0.299, 0.587, 0.114])
    plt.imshow(cinza, cmap='gray')
    plt.show()

os.chdir('imagens')
os.listdir('.')
imagem = os.listdir('.')
arquivo = input('Imagem de entrada: ')
imagem = arquivo

rgb2gray(imagem)
