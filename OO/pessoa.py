class Pessoa:
    olhos =2
    def __init__(self,*filhos,nome= None,idade=35):
        self.idade = idade

        self.nome=nome
        self.filhos =list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    renzo = Pessoa(nome ='Renzo')
    luciano= Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    luciano.olhos=1
    del luciano.olhos
    del luciano.filhos
    print (luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome ='Ramalho'
    print(renzo.__dict__)
    print(luciano.__dict__)

