#
agenda=[]
#contatos={}
#metodo é um verbo
#atributo é um substantivo
class Agenda():
    def __init__(self):
        self.contatos={}
        #self.agenda=[]
    #atributos
    #contatos
    #agenda 
    def adicionar(self):
        #self.contatos={}
        self.contatos["nome"]=input("Digite o nome comleto: ")
        self.contatos["telefone"]=input("Digite o telefone: ")
        self.contatos["email"]=input("Digite o email: ")
        agenda.append(self.contatos)
        print("")

    def exluir(self):
        print("Escolha o contato que você gostaria de apagar:")
        lista=Agenda()
        lista.listar()
        self.id_contato = int(input("Contato para editar: "))
        del agenda[self.id_contato]
        print("")
    
    def listar(self):
        for index, self.contatos in enumerate(agenda):
            print("Contato "+str(index)+":")
            print("Nome completo: "+self.contatos["nome"])
            print("Email: "+self.contatos["email"])
            print("Telefone: "+self.contatos["telefone"])
        print("")
        
    
    def modificar (self):
        #mostrar o método listar  
        lista=Agenda()
        lista.listar()
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

    def encontrar (self):
        self.termo = input("Digite o termo que você gostaria de buscar: ")
        for index, self.contatos in enumerate(agenda):
            if (self.contatos['nome'].find(self.termo) + self.contatos['email'].find(self.termo) + self.contatos['telefone'].find(self.termo))>=-2:
                print("Contato "+str(index)+":")
                print("Nome completo: "+self.contatos["nome"])
                print("Email: "+self.contatos["email"])
                print("Telefone: "+self.contatos["telefone"])
        print("")
    
    #metodos
    #adicionar 
    #excluir 
    #listar
    #modificar 


class Menu():
    def __init__(self,escolha):
        self.escolha=escolha
        pass
    def funcoes(self):
        pass
    #metodos
    #mostar as funções 

    
class Contato():
    def __init__(self,nome,telefone,email):
        self.nome=nome
        self.telefone=telefone
        self.email=email
    
    def informacoes(self):
        print("nome:"+self.nome+"\n telefone:"+ self.telefone+"\n email:"+self.email)
        
    #atributos
    #nome 
    #email
    #telefone
    
    #metodos

#testando funções
contato1=Contato("rodrigo","987645327","rogrigo@ufpa.com")
contato1.informacoes()
contato2=Agenda()
contato2.adicionar()
contato2.modificar()
contato2.listar()
#contato2.exluir()
#contato2.listar()
