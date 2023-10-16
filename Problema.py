from Estado import Estado
from Solucao import Solucao

class Problema:

    def __init__:(self, est_ini: Estado, est_meta: Estado) -> None:
        self.est_ini  = est_ini
        self.est_meta = est_meta
        self.solucao: Solucao = None

    def verificaObjetivo(self, estado: Estado) -> bool:
        pass

    def acao(self, estado: Estado) -> list[Estado]:
        pass

    # def relacao(self, e1: Estado, e2: Estado) -> int:
        # pass

    def __str__(self):
        s:str = ' -> Estado inicial:\n'
        s += str(self.est_ini) + '\n'
        s += '-=-=-=-=-=-=-=-=-=-=-=-='
        s += ' -> Estado meta:\n'
        s += str(self.est_meta)

        return s