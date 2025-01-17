"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:
1) Motor
2) Direção
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incremetar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades
A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:
1) Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
2) Método girar_a_esquerda
  N
O   L
  S
    Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'NORTE'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'LESTE'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'OESTE'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'NORTE'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'OESTE'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'LESTE'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'NORTE'
    >>> carro = Carro(motor,direcao)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'NORTE'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'LESTE'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'NORTE'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'OESTE'
"""

NORTE = 'NORTE'
LESTE = 'LESTE'
SUL ='Sul'
OESTE = 'OESTE' or 'Oeste'
class Carro:
    def __init__(self, motor, direcao):
        self.direcao = direcao
        self.motor = motor
    def calcular_velocidade (self):
       return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()
    def frear(self):
        return self.motor.frear()
    def calcular_direcao(self):
        return self.direcao.valor
    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()
    def girar_a_direita(self):
        return self.direcao.girar_a_direita()


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


class Direcao:
    rotacao_a_direita_dct = {NORTE: LESTE, OESTE: NORTE, LESTE: SUL, SUL: OESTE
                             }
    rotacao_a_esquerda_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL
                              }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor
        ]



