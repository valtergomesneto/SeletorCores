from tkinter import *
import tkinter.messagebox

# cores

cor0 = "#080808" #cor preta
cor1 = "#faf7f7" #cor branca
cor2 = "#004338" #verde forte

# criando a janela

janela = Tk()
janela.geometry("530x205")
janela.configure(bg=cor1)
janela.title("Seletor de cores")

# criando frame janela

tela = Label(janela, bg=cor0, width=40, height=10, bd=1)
tela.grid(row=0, column=0)

frameDireita = Frame(janela, bg=cor1)
frameDireita.grid(row=0, column=1, padx=5)

frameBaixo = Frame(janela, bg=cor1)
frameBaixo.grid(row=1, column=0, columnspan=2, pady=15)

# função scale

def escala(valor):
    #obtem os dados do scale
    r=s_red.get()
    g=s_green.get()
    b=s_blue.get()

    #atribui os dados coletados a variavel rgb em formato estabelecido
    rgb = f'{r}, {g}, {b}'

    #converte para hexadecimal
    global hexadecimal
    hexadecimal = "#%02x%02x%02x" % (r, g, b)

    #atribui a cor do background da tela conforme o hexadecimal gerado
    tela['bg'] = hexadecimal

    #alterando a entry
    e_cor.delete(0, END)
    e_cor.insert(0, hexadecimal)

# função clicar
def onClick():
    #Informar que foi copiado MessageBox
    tkinter.messagebox.showinfo('Cor ', "A cor " + hexadecimal +" foi copiada!")

    #Serve para criar o botão copiar
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(e_cor.get())
    clip.destroy()

# configurando o frame direito

#vermelho
l_red = Label(frameDireita, text='Red', bg=cor1, width=7, fg='red', anchor='nw', font=("Times New Roman", 12, "bold"))
l_red.grid(row=0, column=0)
s_red = Scale(frameDireita, command=escala, from_=0, to=255, length=150, bg=cor1, fg='red',orient=HORIZONTAL)
s_red.grid(row=0, column=1)

#verde
l_green = Label(frameDireita, text='Green', bg=cor1, width=7, fg='green', anchor='nw', font=("Times New Roman", 12, "bold"))
l_green.grid(row=1, column=0)
s_green = Scale(frameDireita, command=escala,from_=0, to=255, length=150, bg=cor1, fg='green',orient=HORIZONTAL)
s_green.grid(row=1, column=1)

#azul
l_blue = Label(frameDireita, text='Blue', bg=cor1, width=7, fg='blue', anchor='nw', font=("Times New Roman", 12, "bold"))
l_blue.grid(row=2, column=0)
s_blue = Scale(frameDireita, command=escala,from_=0, to=255, length=150, bg=cor1, fg='blue',orient=HORIZONTAL)
s_blue.grid(row=2, column=1)

# configurando o frame de baixo

#label Entry
l_rgb = Label(frameBaixo, text='CÓDIGO HEX: ', bg=cor1, font=("Ivy", 10, "bold"))
l_rgb.grid(row=0, column=0, padx=5)

#entry
e_cor = Entry(frameBaixo, width=12, font=("Ivy", 10, "bold"), justify=CENTER)
e_cor.grid(row=0, column=1, padx=5)

#botao copiar
btn_copy = Button(frameBaixo, command=onClick, text='Copiar cor', bg=cor1, font=("Ivy", 8, "bold"), relief=RAISED, overrelief=RIDGE)
btn_copy.grid(row=0, column=2, padx=5)


#app nome
l_app_nome = Label(frameBaixo, text='SELETOR DE CORES', bg=cor1, font=("Ivy", 13, "bold"))
l_app_nome.grid(row=0, column=3, padx=40)


janela.mainloop()