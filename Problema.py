from Estado import Estado
from Solucao import Solucao

class Problema:

    # est_ini e est_meta não são tipados
    # dependendo do problema existe mais de um (lista ou objeto).
    def __init__(self, est_ini, est_meta) -> None:
        self.est_ini  = est_ini
        self.est_meta = est_meta
        self.solucao: Solucao = None

    def verificaObjetivo(self, estado: Estado) -> bool:
        pass

    def acao(self, estado: Estado) -> list[Estado]:
        pass

    def sucessor(self, estado: Estado, visitados: list[Estado]) -> (Estado, list[Estado]):
        pass

    def avaliacao(estado: Estado) -> int:
        pass

    def __str__(self):
        s:str = ' -> Estado inicial:\n'
        s += str(self.est_ini) + '\n'
        s += '-=-=-=-=-=-=-=-=-=-=-=-='
        s += ' -> Estado meta:\n'
        s += str(self.est_meta)

        return s
