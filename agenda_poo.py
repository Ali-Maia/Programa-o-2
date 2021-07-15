#
agenda=[]
contatos={}
#metodo é um verbo
#atributo é um substantivo
class Agenda():
    def __init__(self,contatos,agenda):
        self.contatos=contatos
        self.agenda=agenda
    #atributos
    #contatos
    #agenda 
    def adicionar(self):
        pass
    def exluir(self):
        pass
    def listar(self):
        pass
    def modificar (self):
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