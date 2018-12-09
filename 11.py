import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def hist(imagem):
    ler = cv2.imread(imagem)
    cv2.imshow('Imagem',ler)
    hist = cv2.calcHist([ler],[0],None,[256],[0,256])
    plt.hist(ler.ravel(),256,[0,256])
    plt.title('Histograma da imagem')
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

os.chdir('imagens')
imagem = os.listdir('.')
arquivo = input('Imagem de entrada: ')
imagem = arquivo

hist(imagem)