from tkinter import *

# As seguintes informações são necessárias: nome do álbum, ano de lançamento, nome da banda/artista, álbum lançamento do artista (sim/não);

window = Tk()
window.title("Cadastro de Álbuns")
window.geometry('600x400')

labelNomeAlbum = Label(window, text= 'Nome do Álbum: ')
labelNomeAlbum.grid(column= 0, row= 0, sticky= W)

inputNomeAlbum = Entry(window)
inputNomeAlbum.grid(column= 1, row= 0, sticky= E)

labelDataLancamento = Label(window, text= 'Ano de Lançamento: ')
labelDataLancamento.grid(column= 0, row= 1, sticky= W)

inputDataLancamento = Entry(window)
inputDataLancamento.grid(column= 1, row= 1, sticky= E)

labelNomeBanda = Label(window, text= 'Nome da Banda/Artista: ')
labelNomeBanda.grid(column= 0, row= 2, sticky= W)

inputNomeBanda = Entry(window)
inputNomeBanda.grid(column= 1, row= 2, sticky= E)

labelAlbunLancamento = Label(window, text= 'Álbum lançamento: ')
labelAlbunLancamento.grid(column= 0, row= 3, sticky= W)

window.mainloop()