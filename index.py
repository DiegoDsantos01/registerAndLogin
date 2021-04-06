from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

# Janela de Acesso
window = Tk()
window.title("DBZ Systems - Acess Panel")
window.geometry("600x300")
window.configure(background="white")
window.resizable(width=False, height=False) # Pra não ser possível alterar o tamanho da janela
window.attributes("-alpha", 0.9)
window.iconbitmap(default="icons/iconEsfera.ico")


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

UserEntry = ttk.Entry(RightFrame, width=38)
UserEntry.place(x=112, y=112)

PassLabel = Label(RightFrame, text="Senha:", font=("Century Gothic", 20), bg="DarkOrange", fg="White")
PassLabel.place (x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=40, show="•")
PassEntry.place(x=100, y=162)


# Função Para Logar 

def Login():
    UserLogin = UserEntry.get()
    PassLogin = PassEntry.get()
    
    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """,(UserLogin, PassLogin))

    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (UserLogin in VerifyLogin and PassLogin in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado, Bem Vindo Guerreiro(a) Z.")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique se você não é um vilão.")

# Botões de Acesso

LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    #Removendo os widgets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    #Inserindo os widgets de Cadastro
    NameLabel = Label(RightFrame, text="Nome:", font=("Century Gothic", 20), bg="DarkOrange", fg="White")
    NameLabel.place(x=5, y=5)

    NameEntry = ttk.Entry(RightFrame, width=40)
    NameEntry.place(x=100, y=18)

    EmailLabel = Label(RightFrame, text="E-mail:",  font=("Century Gothic", 20), bg="DarkOrange", fg="White")
    EmailLabel.place(x=5, y=55)

    EmailEntry = ttk.Entry(RightFrame, width=40)
    EmailEntry.place(x=100, y=68)

# Conectando ao Banco de Dados

    def RegisterToDataBase():
        Name = NameEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name == "" or Email == "" or User == "" or Pass == ""):
            messagebox.showerror(title="Register Error", message="Preencha Todos os Campos.")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """,(Name, Email, User, Pass))
            DataBaser.connection.commit()
            messagebox.showinfo(title="Register Info", message="Cadastro Realizado! Bem Vindo aos Guerreiros(a) Z")

    Register = ttk.Button(RightFrame, text="Cadastrar", width=30, command=RegisterToDataBase)
    Register.place(x=100, y=225)

    def BackToLogin():
        #Remover os Widgets de Cadastro
        NameLabel.place(x=5000)
        NameEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        
        #Trazendo os widgets de Login
        LoginButton.place(x=100)
        RegisterButton.place(x=125)

    Back = ttk.Button(RightFrame, text="Voltar", width=20, command=BackToLogin)
    Back.place(x=125, y=260)


RegisterButton = ttk.Button(RightFrame, text="Cadastre-se", width=20, command=Register)
RegisterButton.place(x=130, y=260)

window.mainloop()
