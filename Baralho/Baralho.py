import random
from Carta import Carta

class Baralho():
    def __init__(self):
        self.cartas = []
        self.manilha = []
        self.vira = []
        self.criarBaralho()

    def criarBaralho(self):
        for i in ["Paus","Copas","Espadas","Ouros"]:
            for a in range(1,14):
                if a < 8 or a >10:
                    self.cartas.append(Carta(a,i))

    def definirManilha(self):
        for v in self.vira:
            if v.retornarNumero() == 7:
                return 11
            elif v.retornarNumero() == 13:
                return 1
            else:
                return v.numero + 1

    def definirManilhas(self, manilha):
        for m in self.cartas:
            x = m.retornarNumero()
            if x == manilha:
                self.manilhas.append(m)


    def embaralhar(self):
        random.shuffle(self.cartas)

    def definirVira(self,baralho):
        self.vira.append(baralho.retirarCarta())

    def retirarCarta(self):
        return self.cartas.pop()


    def resetarBaralho(self):
        self.vira = []
        self.manilhas = []
        self.cartas = []