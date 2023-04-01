from tkinter import *

import proj


def save_info():
    ordem_de_venda_info = ordem_de_venda.get()
    tipo_info = tipo.get()
    documentos_info = documentos.get()
    cliente_info = cliente.get()
    gerente_projetos_info = gerente_projetos.get()
    gerente_conta_info = gerente_conta.get()
    status_info = status.get()

    print(ordem_de_venda_info, tipo_info, documentos_info, cliente_info, 
    gerente_projetos_info, gerente_conta_info, status_info)

    lista = {
    "Ordem de Venda": ordem_de_venda_info,
    "Tipo de contrato": tipo_info.title(),
    "Documentos": documentos_info.title(),
    "Cliente": cliente_info.title(),
    "Gerente de Projetos": gerente_projetos_info.title(),
    "Gerente da Conta": gerente_conta_info.title(),
    "Status": status_info.title()}

    with open("teste.json", "a") as arquivo:
        arquivo.write(str(lista) + '\n')

    print("Projeto cadastrado com sucesso.")

    ordem_de_venda_entry.delete(0, END)
    tipo_entry.delete(0, END)
    documentos_entry.delete(0, END)
    cliente_entry.delete(0, END)
    gerente_projetos_entry.delete(0, END)
    gerente_conta_entry.delete(0, END)
    status_entry.delete(0, END)
    #ordem_de_venda.focus()

janela = Tk()
janela.geometry("500x600+500+100")
janela.title("Desafio Python")
heading = Label(text="Cadastro de Projetos", bg="black", fg="white", width="200", height="10")
heading.pack()

ordem_de_venda = Label(text = "Ordem de Venda: ",)
tipo = Label(text = "Tipo de projeto: ",)
documentos = Label(text = "Documentos: ",)
cliente = Label(text = "Cliente: ",)
gerente_projetos = Label(text = "Gerente de Projetos: ",)
gerente_conta = Label(text = "Gerente de conta: ",)
status = Label(text = "Status: ",)

ordem_de_venda.place(x= 15, y = 170)
tipo.place(x= 15, y = 220)
documentos.place(x= 15, y = 270)
cliente.place(x= 15, y = 320)
gerente_projetos.place(x= 15, y = 370)
gerente_conta.place(x = 15, y = 420)
status.place(x= 15, y = 470)

ordem_de_venda = StringVar()
tipo = StringVar()
documentos = StringVar()
cliente = StringVar()
gerente_projetos = StringVar()
gerente_conta = StringVar()
status = StringVar()

ordem_de_venda_entry = Entry(textvariable = ordem_de_venda)
tipo_entry = Entry(textvariable = tipo)
documentos_entry = Entry(textvariable = documentos)
cliente_entry = Entry(textvariable = cliente)
gerente_projetos_entry = Entry(textvariable = gerente_projetos)
gerente_conta_entry = Entry(textvariable = gerente_conta)
status_entry = Entry(textvariable = status)

ordem_de_venda_entry.place(x= 150, y = 170)
tipo_entry.place(x= 150, y = 220)
documentos_entry.place(x= 150, y = 270)
cliente_entry.place(x= 150, y = 320)
gerente_projetos_entry.place(x= 150, y = 370)
gerente_conta_entry.place(x = 150, y = 420)
status_entry.place(x= 150, y = 470)

botao = Button(text = "Salvar", width = "25", height = "2", command = save_info)
botao.place(x = 160, y = 520)


janela.mainloop()