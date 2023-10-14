from Estado     import Estado
from Solucao    import Solucao
from Problema   import Problema

class BMC:

    @staticmethod
    def busca(problema: Problema) -> bool:
        return True

    def Nodo():
        def __init__(self, estado: Estado, custo: int):
            self.estado = estado
            self.custo  = custo

    def FilaPrior():
        def __init__(self):
            self.fila = []

        def insere(self, nodo: Nodo) -> None:
            # fila nao-vazia 
            if self.fila != []:
                # insersao por prioridade
                for idx, elem in enumerate(self.fila):
                    if nodo.custo <= elem.custo:
                        self.fila.insert(idx, nodo)
                        return

            # fila vazia ou elemento de maior custo
            self.fila.append(nodo)
            return

        def pop(self) -> (Estado, int):
            est, cst = self.fila.pop()
            return est, cst

