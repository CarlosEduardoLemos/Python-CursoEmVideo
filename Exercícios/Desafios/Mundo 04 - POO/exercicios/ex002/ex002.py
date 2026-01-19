#Declaração de classes
class Gafanhato:
    def __init__(self, nome = "", idade = 0, sexo = ""):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

        # Métodos de instancia
    def aniversario(self):
        self.idade += 1
        
    def mensagem(self):
        print(f'Olá, eu sou {self.nome}, tenho {self.idade} anos e sou do sexo {self.sexo}.')

# Declaração de um objeto
gafanhato1 = Gafanhato('Carlos', 27, 'M')
gafanhato1.aniversario()
print(gafanhato1.mensagem())

gafanhato2 = Gafanhato('Ana', 52, 'F')
print(gafanhato2.mensagem())

gafanhato3 = Gafanhato()
print(gafanhato3.mensagem())