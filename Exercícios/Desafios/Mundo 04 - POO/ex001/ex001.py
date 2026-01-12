#Declaração de classes
class gafanhato:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

        # Métodos de instancia
    def aniversario(self):
        self.idade += 1
        
    def mensagem(self):
        print(f'Olá, eu sou {self.nome}, tenho {self.idade} anos e sou do sexo {self.sexo}.')

# Definição de um objeto
gafanhato1 = gafanhato('João', 20, 'M')