import matplotlib.pyplot as plt
import numpy as np

def imread(arquivo):
    imagem = plt.imread(arquivo,np.ndarray)
    plt.imshow(imagem)
    plt.title('Imagem')
    plt.show()

arquivo = input('Arquivo: ')
imread('imagens/'+arquivo)