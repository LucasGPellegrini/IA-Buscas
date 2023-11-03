from Estado   import Estado
from Solucao  import Solucao
from Problema import Problema

class ASTR:

    @staticmethod
    def busca(problema: Problema) -> bool:
        # para_visitar -> ListaPrior: [Nodo]
        para_visitar = FilaPrior()

        # visitados -> Dicionario[(Estado.conteudo)] = custo+heuristica
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
                                     custo_atual+vizinho.fnCusto(estado), 
                                     vizinho.heuristica(problema.est_meta),
                                     passos[:]))

        # Algoritmo Geral:
        while para_visitar:

            estado, profundidade, custo_atual, passos = para_visitar.pop()
            visitados[estado.get()] = custo_atual
            qtd_explorada += 1
            passos.append(estado)
            profundidade += 1

            # Checa solução
            if problema.verificaObjetivo(estado):
                problema.solucao = Solucao(qtd_explorada, passos, 
                                           profundidade, problema.est_meta, custo_atual)
                return True

            # Continua busca
            for vizinho in problema.acao(estado):
                if (vizinho.get() not in visitados.keys() 
                    or (custo_atual + vizinho.fnCusto(estado) + vizinho.heuristica(problema.est_meta)) 
                    < visitados[vizinho.get()]):
                    if vizinho.get() not in [x.get()[0].get() for x in para_visitar.fila]:
                        para_visitar.insere(Nodo(vizinho, profundidade, custo_atual+vizinho.fnCusto(estado),
                                                 vizinho.heuristica(problema.est_meta), passos[:]))
                    else:
                        para_visitar.replace(Nodo(vizinho, profundidade, custo_atual+vizinho.fnCusto(estado),
                                                 vizinho.heuristica(problema.est_meta), passos[:]))


        return False

    
class Nodo():

    def __init__(self, estado: Estado, profundidade: int,
                 custo: int, heuri: int, passos: list[Estado]):
        self.estado = estado
        self.profundidade = profundidade
        self.custo  = custo
        self.heuri = heuri
        self.passos = passos

    def get(self):
        return (self.estado, self.profundidade, 
                (self.custo+self.heuri), self.passos)


class FilaPrior():

    def __init__(self):
        self.fila = []

    def insere(self, nodo: Nodo) -> None:
        # fila nao-vazia 
        if self.fila != []:
            # insersao por prioridade
            for idx, elem in enumerate(self.fila):
                if (nodo.custo + nodo.heuri) < (elem.custo + elem.heuri): 
                    self.fila.insert(idx, nodo)
                    return

        # fila vazia ou elemento de maior custo
        self.fila.append(nodo)
        return
    
    def replace(self, nodo: Nodo) -> None:
        # busca pelo elemento em comum:
        for indice, instancia in enumerate(self.fila):
            if instancia.get()[0].get() == nodo.get()[0].get():
                if (nodo.custo + nodo.heuri) < (instancia.custo + instancia.heuri): 
                    self.fila.pop(indice)
                    self.insere(nodo)

    def pop(self) -> (Estado, int, int, list[Estado]):
        nodo = self.fila.pop(0)
        return nodo.get()
