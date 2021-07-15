#
agenda=[]
contatos={}
#metodo é um verbo
#atributo é um substantivo
class Agenda():
    #def __init__(self,contatos,agenda):
        #self.contatos=contatos
       #self.agenda=agenda
        #self.agenda=[]
    #atributos
    #contatos
    #agenda 
    def adicionar(self):
        self.contatos={}
        self.contatos["nome"]=input("Digite o nome comleto: ")
        self.contatos["telefone"]=input("Digite o telefone: ")
        self.contatos["email"]=input("Digite o email: ")
        agenda.append(self.contatos)

    def exluir(self):
        pass
    def listar(self):
        for index, self.contatos in enumerate(agenda):
            print("Contato "+str(index)+":")
            print("Nome completo: "+self.contatos["nome"])
            print("Email: "+self.contatos["email"])
            print("Telefone: "+self.contatos["telefone"])
    
    def modificar (self):
        pass

    def encontrar (self):
        pass
    
    #metodos
    #adicionar 
    #excluir 
    #listar
    #modificar 


class Menu():
    def __init__(self,inicio,escolha):
        self.inicio=inicio
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

contato1=Contato("rodrigo","987645327","rogrigo@ufpa.com")
contato1.informacoes()
contato2=Agenda()
contato2.adicionar()
contato2.listar()