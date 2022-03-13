class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0 #esse underline não torna esse atributo privaod,
                        # mas é um aviso de que não deve ser mexido,
                        #de que deve ser tratado como se fosse um atributo privado.
    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0



vingadores = Filme("vingadores - guerra infinita", 2018, 160)
print(vingadores.nome)

atlanta = Serie('atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')
