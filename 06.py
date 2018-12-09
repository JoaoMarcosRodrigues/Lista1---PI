import cv2
import matplotlib.pyplot as plt

def imreadgray(arquivo):
    imagem = cv2.imread(arquivo,0)
    plt.imshow(imagem,cmap='gray')
    plt.title='Imagem em preto e branco'
    plt.show()

arquivo = input('Arquivo: ')
imreadgray('imagens/'+arquivo)