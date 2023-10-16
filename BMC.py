from Estado     import Estado
from Solucao    import Solucao
from Problema   import Problema

class BMC:

    @staticmethod
    def busca(problema: Problema) -> bool:
        # para_visitar -> ListaPrior: [Nodo]
        para_visitar = ListaPrior()

        # visitados -> Dicionario[Estado] = custo
        visitados = {}

        # passos -> Lista: Estado
        passos = []

        qtd_explorada = 0
        custo_atual = 0
        

        # Nó raiz
        estado, profundidade = (problema.est_ini, 0)
        visitados[estado] = 0
        passos.append(estado)

        profundidade += 1
        for vizinho in problema.acao(estado):
            para_visitar.insere(Nodo(vizinho, profundidade, custo_atual+vizinho.fnCusto()))

        # Algoritmo Geral:
        while para_visitar:

            estado, profundidade, custo_atual = para_visitar.pop()
            visitados[estado] = custo_atual

            # tratamento do caminho
            while len(passos) > profundidade:
                passos.pop()
            passos.append(estado)

            qtd_explorada += 1
            
            # Checa solução
            if problema.verificaObjetivo(estado):
                problema.solucao = Solucao(qtd_explorada, passos, 
                                           profundidade, problema.est_meta, custo_atual)
                return True

            # Continua busca
            profundidade += 1
            for vizinho in problema.acao(estado):
                if vizinho not in visitados.keys() or (custo_atual + vizinho.fnCusto()) < visitados[vizinho]
                    para_visitar.insert(Nodo(vizinho, profundidade, custo_atual+vizinho.fnCusto()))

        return False



    def Nodo():
        def __init__(self, estado: Estado, profundidade: int, custo: int):
            self.estado = estado
            self.profundidade = profundidade
            self.custo  = custo

        def __get(self):
            return (self.estado, self.profundidade, self.custo)
                # tratamento rollback
                while len(passos) > profundidade:
                    passos.pop()

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

        def pop(self) -> (Estado, int, int):
            est, prof, cst = (self.fila.pop()).__get()
            return est, prof, cst

