from Estado   import Estado
from Solucao  import Solucao
from Problema import Problema

class ASTR:

    @staticmethod
    def busca(problema: Problema) -> bool:
        # para_visitar -> ListaPrior: [Nodo]
        para_visitar = FilaPrior()

        # visitados -> Dicionario[(Estado.conteudo)] = custo
        visitados = {}

        # passos -> Lista: Estado
        passos = []

        qtd_explorada = 0
        custo_atual = 0
        

        # Nó raiz
        estado, profundidade = (problema.est_ini, 0)
        visitados[tuple(estado.conteudo)] = 0
        passos.append(estado)

        profundidade += 1
        for vizinho in problema.acao(estado):
            para_visitar.insere(Nodo(vizinho, profundidade, 
                                     custo_atual+vizinho.fnCusto(estado), 
                                     vizinho.heuristica(problema.est_meta)))

        # Algoritmo Geral:
        while para_visitar:

            estado, profundidade, custo_atual = para_visitar.pop()
            visitados[tuple(estado.conteudo)] = custo_atual
            qtd_explorada += 1

            # tratamento do caminho
            while len(passos) > profundidade:
                passos.pop()
            passos.append(estado)
 
            # Checa solução
            if problema.verificaObjetivo(estado):
                problema.solucao = Solucao(qtd_explorada, passos, 
                                           profundidade, problema.est_meta, custo_atual)
                return True

            # Continua busca
            profundidade += 1
            for vizinho in problema.acao(estado):
                if tuple(vizinho.conteudo) not in visitados.keys() or (custo_atual + vizinho.fnCusto(estado)) < visitados[tuple(vizinho.conteudo)]:
                    para_visitar.insere(Nodo(vizinho, profundidade, custo_atual+vizinho.fnCusto(estado), vizinho.heuristica(problema.est_meta)))

        return False

    
class Nodo():

    def __init__(self, estado: Estado, profundidade: int, custo: int, heuri: int):
        self.estado = estado
        self.profundidade = profundidade
        self.custo  = custo
        self.heuri = heuri

    def get(self):
        return (self.estado, self.profundidade, self.custo)


class FilaPrior():

    def __init__(self):
        self.fila = []

    def insere(self, nodo: Nodo) -> None:
        # fila nao-vazia 
        if self.fila != []:
            # insersao por prioridade
            for idx, elem in enumerate(self.fila):
                if (nodo.custo + nodo.heuri) <= (elem.custo + elem.heuri): 
                    self.fila.insert(idx, nodo)
                    return

        # fila vazia ou elemento de maior custo
        self.fila.append(nodo)
        return

    def pop(self) -> (Estado, int, int):
        nodo = self.fila.pop()
        est, prof, cst = nodo.get()
        return est, prof, cst
