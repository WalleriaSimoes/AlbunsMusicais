from tkinter import *

# As seguintes informações são necessárias: nome do álbum, ano de lançamento, nome da banda/artista, álbum lançamento do artista (sim/não);

window = Tk()
window.title("Cadastro de Álbuns")
window.geometry('600x400+350+150')

def salva_valores():
    nomeAlbum = inputNomeAlbum.get()
    dataLancamento = inputDataLancamento.get()
    nomeBanda = inputNomeBanda.get()
    albumLancamento = v0.get()

    with open('Albuns_Cadastrados.txt', 'a') as albunsCadastrados:
        if albumLancamento == 0:
            albunsCadastrados.write(f"{nomeAlbum}|{dataLancamento}|{nomeBanda}|Não\n")
        else:
            albunsCadastrados.write(f"{nomeAlbum}|{dataLancamento}|{nomeBanda}|Sim\n")

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

v0 = IntVar()
r1 = Radiobutton(window, text= 'Sim', variable= v0, value= True)
r1.grid(column= 1, row= 3, sticky= W)
r2 = Radiobutton(window, text= 'Não', variable= v0, value= False)
r2.grid(column= 1, row= 3, sticky= E)

botao = Button(window, text= 'Cadastrar', command= salva_valores)
botao.grid(column= 0, row= 4, columnspan= 2)

window.mainloop()