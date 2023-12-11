from tkinter import *

window = Tk()
window.title("Álbuns Cadastrados")
window.geometry('600x400')


with open('Albuns_Cadastrados.txt', 'r') as cadastros:
    respostas = cadastros.read()
    lista_respostas = respostas.split('\n')
    lista_dados = []

    if respostas.strip() != "":
        for n in range(0, len(lista_respostas) - 1):
            lista_dados.append(lista_respostas[n].split('|'))

    for x in range(0, len(lista_dados)):

        Label(window, text= f"Nome do Álbum: {lista_dados[x][0]}, Ano de Lançamento: {lista_dados[x][1]}, Nome da Banda/Artista: {lista_dados[x][2]}, Álbum lançamento: {lista_dados[x][3]}").pack()

window.mainloop()