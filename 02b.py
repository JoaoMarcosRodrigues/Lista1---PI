import cv2
import matplotlib.pyplot as plt

def imread(arquivo):
    imagem = cv2.imread(arquivo,0)
    plt.imshow(imagem,cmap='gray')
    plt.title('Imagem preta e branca')
    plt.show()

arquivo = input('Arquivo: ')
imread('imagens/'+arquivo)