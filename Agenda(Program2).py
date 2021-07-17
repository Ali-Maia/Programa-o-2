#PROGRAMAÇÃO 2 
#Professor: Fabrício Almeida
#Alunas: Alícia Maia(202017740004) e Sarah Cabral(202017740005)
#Turma: Engenharia da Computação/2020.04

agenda=[]

class Agenda():
    def __init__(self):
        self.contatos={}

    def adicionar(self):
        self.contatos["nome"]=input("Digite o nome comleto: ")
        self.contatos["telefone"]=input("Digite o telefone: ")
        self.contatos["email"]=input("Digite o email: ")
        agenda.append(self.contatos)
        print("")
        
        #Código que retorna para o menu
        retorno = Menu()
        retorno.exibir_opcoes()
        x=input("Digite a opção: ")
        retorno.setEscolha(x)
        retorno.destino()

    def excluir(self):
        print("Escolha o contato que você gostaria de apagar:")
        lista=Agenda()
        lista.listar_excluir_modificar()
        self.id_contato = int(input("Contato para editar: "))
        del agenda[self.id_contato]
        print("")
        
        #Código que retorna para o menu
        retorno = Menu()
        retorno.exibir_opcoes()
        x=input("Digite a opção: ")
        retorno.setEscolha(x)
        retorno.destino()

    def listar(self):
        for index, self.contatos in enumerate(agenda):
            print("Contato "+str(index)+":")
            print("Nome completo: "+self.contatos["nome"])
            print("Email: "+self.contatos["email"])
            print("Telefone: "+self.contatos["telefone"])
        print("")
        
        #Código que retorna para o menu
        retorno = Menu()
        retorno.exibir_opcoes()
        x=input("Digite a opção: ")
        retorno.setEscolha(x)
        retorno.destino()
    
    def listar_excluir_modificar(self):
        for index, self.contatos in enumerate(agenda):
            print("Contato "+str(index)+":")
            print("Nome completo: "+self.contatos["nome"])
            print("Email: "+self.contatos["email"])
            print("Telefone: "+self.contatos["telefone"])
        print("")
        
    def modificar(self):
        #mostrar o método listar  
        lista=Agenda()
        lista.listar_excluir_modificar()
        print("Escolha o contato que você gostaria de editar:")
        self.id_contato = int(input("Contato para editar: "))
        if self.id_contato !="":
            self.novoNome = input("Novo valor para o Nome "+agenda[self.id_contato]["nome"]+": ")
            if self.novoNome != "":
                agenda[self.id_contato]["nome"] = self.novoNome
    
            self.novoEmail = input("Novo valor para o Email "+agenda[self.id_contato]["email"]+": ")
            if self.novoEmail != "":
                agenda[self.id_contato]["email"] = self.novoEmail

            self.novoTelefone = input("Novo valor para o Telefone "+agenda[self.id_contato]["telefone"]+": ")
            if self.novoTelefone != "":
                agenda[self.id_contato]["telefone"] = self.novoTelefone
        print("")
        
        #Código que retorna para o menu
        retorno = Menu()
        retorno.exibir_opcoes()
        x=input("Digite a opção: ")
        retorno.setEscolha(x)
        retorno.destino()

    def encontrar (self):
        self.termo = input("Digite o termo que você gostaria de buscar: ")
        for index, self.contatos in enumerate(agenda):
            if (self.contatos['nome'].find(self.termo) + self.contatos['email'].find(self.termo) + self.contatos['telefone'].find(self.termo))>=-2:
                print("Contato "+str(index)+":")
                print("Nome completo: "+self.contatos["nome"])
                print("Email: "+self.contatos["email"])
                print("Telefone: "+self.contatos["telefone"])
        print("")
        
        #Código que retorna para o menu
        retorno = Menu()
        retorno.exibir_opcoes()
        x=input("Digite a opção: ")
        retorno.setEscolha(x)
        retorno.destino()
        
class Menu():
    #Definindo a opção escolhida
    def getEscolha(self):
        return self.escolha

    def setEscolha(self, opcao):
        self.escolha = opcao
    
    def exibir_opcoes(self):
        print("Escolha uma das opções abaixo:")
        print("1 - Incluir contato")
        print("2 - Buscar contato")
        print("3 - Editar contato")
        print("4 - Excluir contato")
        print("5 - Listar contatos")
        print("6 - Sair")
            
    def destino(self):
        #Encaminha de acordo com a escolha do usuário
        produto = Agenda()
        if self.escolha == "1":
           produto.adicionar()
        elif self.escolha == "2":
            produto.encontrar()
        elif self.escolha == "3":
            produto.modificar()
        elif self.escolha == "4":
            produto.excluir()
        elif self.escolha == "5":
            produto.listar()
        elif self.escolha == "6":
            print("Bye bye :)")
        else:
            #Código que retorna para o menu
            print("Opção inválida, tente novamente!")
            p1.exibir_opcoes()
            x=input("Digite a opção: ")
            p1.setEscolha(x)
            p1.destino()
            
#Exibição
p1 = Menu() 
p1.exibir_opcoes()
x=input("Digite a opção: ")
p1.setEscolha(x)
p1.destino()




