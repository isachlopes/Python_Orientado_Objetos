from datetime import date


class Pessoa:
    from datetime import date
    atual = date.today().year
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
        
    def ano_nascimento(self):
        print(self.atual - self.idade)
        
    @classmethod
    def por_ano_nasc(cls, nome, nasc):
        idade = cls.atual - nasc
        return cls(nome, idade)
#p1 = Pessoa.por_ano_nasc('Ana', 1999)
p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.idade, p1.nome)
p1.ano_nascimento()
        
        