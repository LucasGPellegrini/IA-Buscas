from Est2NF import Est2NF
from Problema import Problema

class Prob2NF(Problema):

    def __init__(self, est_ini, est_meta) -> None:
        super().__init__(est_ini, est_meta)

    def verificaObjetivo(self, estado: Estado) -> bool:
        if estado.conteudo in est_meta:
            return True
        
        return False

    def __swap(self, lista, pos1, pos2): 
        list[pos1], list[pos2] = list[pos2], list[pos1]
        return list

    def acao(self, estado: Estado) -> list[Estado]:
        vizinhos = []
        vazio_ind = estado.conteudo.index('')
        N = len(estado.conteudo) // 2

        for ind, ficha in enumerate(estado.conteudo):
            if abs(ind - vazio_ind) <= N:
                vizinhos.append(Estado(__swap(ind, vazio_ind)))

        return vizinhos

