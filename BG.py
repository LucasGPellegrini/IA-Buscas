
from Estado     import Estado
from Solucao    import Solucao
from Problema   import Problema

class BG:

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
        visitados[estado.get()] = 0
        passos.append(estado)

        profundidade = 1
        for vizinho in problema.acao(estado):
            para_visitar.insere(Nodo(vizinho, profundidade,
                                     custo_atual+vizinho.heuristica(problema.est_meta),
                                     passos[:]))

        # Algoritmo Geral:
        while para_visitar:

            estado, profundidade, custo_atual, passos = para_visitar.pop()
            visitados[estado.get()] = custo_atual 
            qtd_explorada += 1
            passos.append(estado)
            profundidade += 1

            #print(f'Explorei o estado: {estado.__str__()}\n')
            #print(f'Qtd de nós explorados: {qtd_explorada}\n')
            #print(f'Profundidade: {profundidade}, Custo: {custo_atual}\n\n')

            # Checa solução
            if problema.verificaObjetivo(estado):
                problema.solucao = Solucao(qtd_explorada, passos, 
                                           profundidade, problema.est_meta, custo_atual)
                return True

            # Continua busca
            for vizinho in problema.acao(estado):
                if vizinho.get() not in visitados.keys() or (custo_atual + vizinho.heuristica(problema.est_meta)) < visitados[vizinho.get()]:
                    para_visitar.insere(Nodo(vizinho, profundidade, 
                                             custo_atual+vizinho.heuristica(problema.est_meta),
                                             passos[:]))

        return False


class Nodo():
    def __init__(self, estado: Estado, profundidade: int, 
                 custo: int, passos: list[Estado]):
        self.estado = estado
        self.profundidade = profundidade
        self.custo  = custo
        self.passos = passos

    def get(self):
        return (self.estado, self.profundidade,
                self.custo, self.passos)


class FilaPrior():

    def __init__(self):
        self.fila = []

    def insere(self, nodo: Nodo) -> None:
        # fila nao-vazia 
        if self.fila != []:
            # insersao por prioridade
            for idx, elem in enumerate(self.fila):
                if nodo.custo < elem.custo: 
                    self.fila.insert(idx, nodo)
                    return

        # fila vazia ou elemento de maior custo
        self.fila.append(nodo)
        return

    def pop(self) -> (Estado, int, int, list[Estado]):
        nodo = self.fila.pop(0)
        return nodo.get()


