class Carta():

    CARTAS_VALORES = {
        "3": 10,
        "2": 9,
        "1": 8,
        "13": 7,
        "12": 6,
        "11": 5,
        "7": 4,
        "6": 3,
        "5": 2,
        "4": 1
    }

    NAIPES_VALORES = {
        "Paus": 4,
        "Copas": 3,
        "Espadas": 2,
        "Ouros": 1
    }

    def __init__(self, numero, naipe):
        self.numero = numero
        self.naipe = naipe

    def verificarCarta(self, carta_jogador_01, carta_jogador_02):
        if self.CARTAS_VALORES[str(carta_jogador_01.numero)] > self.CARTAS_VALORES[str(carta_jogador_02.numero)]:
            return carta_jogador_01
        elif self.CARTAS_VALORES[str(carta_jogador_01.retornarNumero())] < self.CARTAS_VALORES[
            str(carta_jogador_02.retornarNumero())]:
            return carta_jogador_02
        else:
            return "Empate"

    def verificarManilha(self, carta_jogador_01, carta_jogador_02):
        if self.NAIPES_VALORES[carta_jogador_01.naipe] > self.NAIPES_VALORES[carta_jogador_02.naipe]:
            return carta_jogador_01
        elif self.NAIPES_VALORES[carta_jogador_01.naipe] < self.NAIPES_VALORES[carta_jogador_02.naipe]:
            return carta_jogador_02
        else:
            raise "Erro"

    def retornarNumero(self):
        return self.numero

    def retornarNaipe(self):
        return self.naipe