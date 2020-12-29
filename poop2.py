class Programas:
    def __init__(self,nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes}'

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
        self._nome = nome.title()


class Filme(Programas):
    def __init__(self,nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} Min - {self.likes} Likes'


class Serie(Programas):
    def __init__(self,nome, ano, temporada):
        super().__init__(nome,ano)
        self.temporada = temporada

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporada} Temporadas - {self.likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


vingadores = Filme("vingadores: guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("Todo mundo em panico", 1999, 100)
demolidor = Serie("Demolidor", 2018, 4)

vingadores.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()


lista_de_programas = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist("Filmes do fim de semana", lista_de_programas)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)





