from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Janela de Acesso
window = Tk()
window.title("DS Systems - Acess Panel")
window.geometry("600x300")
window.configure(background="white")
window.resizable(width=False, height=False) # Pra não ser possível alterar o tamanho da janela
window.attributes("-alpha", 0.9)


# Carregar Logotipo

logo = PhotoImage(file="icons/esfera.png") # PhotoImage serve para pegar a imagem do tKinter e exibir ela primeiro


# Widgets da Janela
LeftFrame = Frame(window, width=200, height=300, bg="Black", relief="raise")  # Frame da esquerda
LeftFrame.pack(side=LEFT)


RightFrame = Frame(window, width=390, height=300, bg="DarkOrange", relief="raise")  # Frame da direita
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="Black")
LogoLabel.place(x=60, y=100)

UserLabel = Label(RightFrame, text="Usuário:", font=("Century Gothic", 20), bg="DarkOrange", fg="White")
UserLabel.place (x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=112)

PassLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg="DarkOrange", fg="White")
PassLabel.place (x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30)
PassEntry.place(x=150, y=162)

# Botões de Acesso

LoginButton = ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x=100, y=225)

RegisterButton = ttk.Button(RightFrame, text="Cadastre-se", width=20)
RegisterButton.place(x=130, y=260)

window.mainloop()
