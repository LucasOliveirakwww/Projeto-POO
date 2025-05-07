#Introdução a POO
'''
1-Classe pascalcase class ClassePessoa
2-Método camelcase classePessoa
'''
class Pessoa():
    def __init__(self,nome, idade, peso):
        self.nome=nome
        self.peso=peso
        self.idade=idade
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}! Eu tenho {self.idade} anos e peso {self.peso} kg.")
    def comer(self):
        print(f"{self.nome} está comendo.")
    def dormir(self):
        print(f"{self.nome} está dormindo.")
    def falar(self):
        print(f"{self.nome} está falando.")