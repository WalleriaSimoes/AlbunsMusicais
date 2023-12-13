from tkinter import *

# As seguintes informações são necessárias: nome do álbum, ano de lançamento, nome da banda/artista, álbum lançamento do artista (sim/não);

window = Tk()
window.title("Cadastro de Álbuns")
window.geometry('600x400+350+150')

def separa_dados():

    with open('Albuns_Cadastrados.txt', 'r') as cadastros:
        respostas = cadastros.read()
        lista_respostas = respostas.split('\n')
        lista_dados = []

        if respostas.strip() != "":
            for n in range(0, len(lista_respostas)):
                lista_dados.append(lista_respostas[n].split('|'))

            return lista_dados

def mostra_albuns():
    window = Tk()
    window.title("Álbuns Cadastrados")
    window.geometry('600x400')

    lista_dados = separa_dados()

    for x in range(0, len(lista_dados)):

        Label(window, text= f"Nome do Álbum: {lista_dados[x][0]}, Ano de Lançamento: {lista_dados[x][1]}, Nome da Banda/Artista: {lista_dados[x][2]}, Álbum lançamento: {lista_dados[x][3]}").pack()

def cadastra_valores():
    nomeAlbum = inputNomeAlbum.get()
    dataLancamento = inputDataLancamento.get()
    nomeBanda = inputNomeBanda.get()
    albumLancamento = v0.get()

    with open('Albuns_Cadastrados.txt', 'a') as albunsCadastrados:
        if albumLancamento == 0:
            albunsCadastrados.write(f"{nomeAlbum}|{dataLancamento}|{nomeBanda}|Não\n")
        else:
            albunsCadastrados.write(f"{nomeAlbum}|{dataLancamento}|{nomeBanda}|Sim\n")

def busca_album():
    window_busca = Tk()
    window_busca.title('Buscar Álbum')
    window_busca.geometry('600x400')
    frame_busca = Frame(window_busca)

    def buscar_informacoes():
        lista_dados = separa_dados()
        albuns_buscados = []
        escolha = str(v1.get())
        print(escolha)
        if escolha == '1':
            buscaNome = inputBusca.get()

            for n in range(0, len(lista_dados)):
                if buscaNome.upper() in lista_dados[n][0].upper():
                    albuns_buscados.append(lista_dados[n])

        for n in range(0, len(albuns_buscados)):
            Label(frame_busca, text= f"Nome do Álbum: {albuns_buscados[n][0]}, Ano de Lançamento: {albuns_buscados[n][1]}, Nome da Banda/Artista: {albuns_buscados[n][2]}, Álbum lançamento: {albuns_buscados[n][3]}").grid(row= 4)

    v1 = StringVar()
    v1.set(1)
    r3 = Radiobutton(frame_busca, text= 'Buscar pelo Nome', variable= v1, value='1')
    r3.grid(column= 0, row= 0, sticky= W)
    r4 = Radiobutton(frame_busca, text= 'Buscar pelo Ano', variable= v1, value='2')
    r4.grid(column= 0, row= 1, sticky= W)

    inputBusca = Entry(frame_busca)
    inputBusca.grid(column= 1, row= 0, rowspan= 2)

    botao_exibir_busca = Button(frame_busca, text= 'Buscar', command= buscar_informacoes)
    botao_exibir_busca.grid(column= 0, row= 2)

    frame_busca.pack(expand= True)

    window_busca.mainloop()


main_frame = Frame(window)

labelNomeAlbum = Label(main_frame, text= 'Nome do Álbum: ')
labelNomeAlbum.grid(column= 0, row= 0, sticky= W)

inputNomeAlbum = Entry(main_frame)
inputNomeAlbum.grid(column= 1, row= 0, sticky= E)

labelDataLancamento = Label(main_frame, text= 'Ano de Lançamento: ')
labelDataLancamento.grid(column= 0, row= 1, sticky= W)

inputDataLancamento = Entry(main_frame)
inputDataLancamento.grid(column= 1, row= 1, sticky= E)

labelNomeBanda = Label(main_frame, text= 'Nome da Banda/Artista: ')
labelNomeBanda.grid(column= 0, row= 2, sticky= W)

inputNomeBanda = Entry(main_frame)
inputNomeBanda.grid(column= 1, row= 2, sticky= E)

labelAlbunLancamento = Label(main_frame, text= 'Álbum lançamento: ')
labelAlbunLancamento.grid(column= 0, row= 3, sticky= W)

v0 = IntVar()
r1 = Radiobutton(main_frame, text= 'Sim', variable= v0, value= True)
r1.grid(column= 1, row= 3, sticky= W)
r2 = Radiobutton(main_frame, text= 'Não', variable= v0, value= False)
r2.grid(column= 1, row= 3, sticky= E)

botao_cadastro = Button(main_frame, text= 'Cadastrar', command= cadastra_valores)
botao_cadastro.grid(column= 0, row= 4)

botao_mostrar_cadastros = Button(main_frame, text= 'Mostrar Albuns', command= mostra_albuns)
botao_mostrar_cadastros.grid(column= 1, row = 4)

botao_buscar = Button(main_frame, text= 'Buscar Álbum', command= busca_album)
botao_buscar.grid(column= 3, row= 4)

main_frame.pack(expand= True)

window.mainloop()