import matplotlib.pyplot as plt
import os

def size(imagem):
    ler = plt.imread(imagem)
    vetor = [ler.shape[1],ler.shape[0]]
    print('Largura x altura: ',vetor)

os.chdir('imagens')
os.listdir('.')
imagem = os.listdir('.')
arquivo = input('Imagem de entrada: ')
imagem = arquivo

size(imagem)