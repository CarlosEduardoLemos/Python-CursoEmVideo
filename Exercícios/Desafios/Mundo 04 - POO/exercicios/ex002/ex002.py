#Declaração de classes
class Gafanhato:
    """
    Classe que representa um Gafanhato com nome, idade e sexo.
    Para criar uma nova pessoa, use variavel = Gafanhato('Nome', Idade, 'Sexo')
    """
    def __init__(self, nome = "", idade = 0, sexo = ""):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

        # Métodos de instancia
    def aniversario(self):
        self.idade += 1
        
    #def mensagem(self):
    #    print(f'Olá, eu sou {self.nome}, tenho {self.idade} anos e sou do sexo {self.sexo}.')

    def __str__(self): #Dunder Method str
        return f'Gafanhato: {self.nome}, {self.idade} anos, Sexo: {self.sexo}'
    
    
    def __getstate__(self): #Dunder Method getstate
        return f"Estado: Nome: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}"

# Declaração de um objeto
gafanhato1 = Gafanhato('Carlos', 27, 'M')
gafanhato1.aniversario()
print(gafanhato1)
print(gafanhato1.__dict__) #Attribute Dunder dict mostra os atributos do objeto em forma de dicionário
print(gafanhato1.__getstate__()) # Method Dunder getstate mostra o estado do objeto em forma de dicionário
#print(gafanhato1.mensagem())

# print(Gafanhato.__doc__) #Dunder Attribute doc mostra a documentação da classe

gafanhato2 = Gafanhato('Ana', 52, 'F')
print(gafanhato2)
#print(gafanhato2.mensagem())

gafanhato3 = Gafanhato()
print(gafanhato3)
#print(gafanhato3.mensagem())