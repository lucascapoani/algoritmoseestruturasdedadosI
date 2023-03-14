class Pessoa():

    def __init__(self, nome, idadePessoa ):
        print("Objeto Instanciado")
        self.nome = nome
        self.idade = idadePessoa
        self.fone = input("Digite o telefone: ")

    def imprimir(self):
        print("Nome: ", self.nome)
        print("Idade: ",self.idade)
        print("Telefone: ",self.fone)