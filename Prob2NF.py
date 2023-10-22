from Est2NF import Est2NF
from Estado import Estado
from Problema import Problema
import random

class Prob2NF(Problema):

    def __init__(self, est_ini=None, est_meta=None, N=2) -> None:
        if N == 2:
            if est_ini == None:
                est_ini = [Est2NF(['B','B','','P','P']), Est2NF(['P','P','','B','B'])]
            if est_meta == None:
                est_meta = [Est2NF(['B','P','P','B','']),
                            Est2NF(['P','B','B','P','']),
                            Est2NF(['','P','B','B','P']),
                            Est2NF(['','B','P','P','B'])]
        if N == 3:
            if est_ini == None:
                est_ini = [Est2NF(['B','B','B','','P','P','P']), Est2NF(['P','P','P','','B','B','B'])]
            if est_meta == None:
                est_meta = [Est2NF(['B','B','P','P','P','B','']),
                            Est2NF(['P','P','B','B','B','P','']),
                            Est2NF(['','P','P','B','B','B','P']),
                            Est2NF(['','B','B','P','P','P','B'])]
        else: # N == 4
            if est_ini == None:
                est_ini = [Est2NF(['B','B','B','B','','P','P','P','P']), Est2NF(['P','P','P','P','','B','B','B','B'])]
            if est_meta == None:
                est_meta = [Est2NF(['B','B','P','P','P','P','B','B','']),
                            Est2NF(['P','P','B','B','B','B','P','P','']),
                            Est2NF(['','P','P','B','B','B','B','P','P']),
                            Est2NF(['','B','B','P','P','P','P','B','B'])]

        if isinstance(est_ini, list): est_ini = random.choice(est_ini)
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

