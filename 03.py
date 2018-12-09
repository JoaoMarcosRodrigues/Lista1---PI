import matplotlib.pyplot as plt
import os

def nchannels(imagem):
    ler = plt.imread(imagem)
    print("Canais: {}".format(ler.shape[2]))

os.chdir('imagens')
os.listdir('.')
imagem = os.listdir('.')
arquivo = input('Imagem de entrada: ')
imagem = arquivo

nchannels(imagem)