from Est2NF import Est2NF
from Estado import Estado
from Problema import Problema

class Prob2NF(Problema):

    def __init__(self, est_ini, est_meta) -> None:
        super().__init__(est_ini, est_meta)

    def verificaObjetivo(self, estado: Estado) -> bool:
        if estado.conteudo in [x.conteudo for x in self.est_meta]:
            return True
        
        return False

    def __swap(self, conteudo, pos1, pos2):
        lista = conteudo[:]
        lista[pos1], lista[pos2] = lista[pos2], lista[pos1]
        return lista

    def acao(self, estado: Estado) -> list[Estado]:
        vizinhos = []
        vazio_ind = estado.conteudo.index('')
        N = len(estado.conteudo) // 2

        for ind, ficha in enumerate(estado.conteudo):
            if abs(ind - vazio_ind) <= N and ind != vazio_ind:
                vizinhos.append(Est2NF(self.__swap(estado.conteudo, ind, vazio_ind)))

        return vizinhos

