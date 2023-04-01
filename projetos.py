
class Projetos:

    def __init__(self, ordem_venda, tipo, documentos, cliente, gerente_projetos, gerente_conta, status):
        self.__ordem_venda = ordem_venda
        self.__tipo = tipo
        self.__documentos = documentos.title()
        self.__cliente = cliente.title()
        self.__gerente_projetos = gerente_projetos.title()
        self.__gerente_conta = gerente_conta.title()
        self.__status = status.title()


    def documentacao(self):

        if(self.__documentos == "Aprovado"):
            print("Documentos aprovados! O projeto pode seguir.")
        else:
            print("Documentos inválidos. Favor reportar o time de vendas.")

    def dicionario(self):
    
        lista = {
            "Ordem de venda": self.__ordem_venda,
            "Tipo de contrato": self.__tipo,
            "Documentação": self.__documentos,
            "Cliente": self.__cliente,
            "Gerente da Conta": self.__gerente_conta,
            "Gerente de projetos": self.__gerente_projetos,
            "Status do Projeto": self.__status}

        return lista

    def exportar_json(self):
        with open("teste.json", "a") as arquivo:
            arquivo.write(str(self.dicionario()) + '\n')


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status




projeto1 = Projetos(1993, "MS", "aprovado", "Jefferson", "Carlos", "Julia", "Concluído")
projeto2 = Projetos(5655, "Software", "reprovado", "Jefferson", "Luan", "Alex", "Concluído")
projeto3 = Projetos(19828, "MS", "reprovado", "Marcos", "Clarisse", "Alex", "On Hold")

projeto1.exportar_json()
projeto3.exportar_json()
projeto2.exportar_json()

