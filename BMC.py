from Estado     import Estado
from Solucao    import Solucao
from Problema   import Problema

class BMC:

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

        profundidade = 0
        for vizinho in problema.acao(estado):
            para_visitar.insere(Nodo(vizinho, profundidade, custo_atual+vizinho.fnCusto(estado)))

        # Algoritmo Geral:
        while para_visitar:

            estado, profundidade, custo_atual = para_visitar.pop()
            visitados[tuple(estado.conteudo)] = custo_atual 
            qtd_explorada += 1

            #print(f'Explorei o estado: {estado.__str__()}\n')
            #print(f'Qtd de nós explorados: {qtd_explorada}\n')
            #print(f'Profundidade: {profundidade}, Custo: {custo_atual}\n\n')


            # tratamento do caminho
            while len(passos) > profundidade and len(passos) > 1:
                passos.pop()
            passos.append(estado)

            profundidade += 1

            # Checa solução
            if problema.verificaObjetivo(estado):
                problema.solucao = Solucao(qtd_explorada, passos, 
                                           profundidade, problema.est_meta, custo_atual)
                return True

            # Continua busca
            for vizinho in problema.acao(estado):
                if tuple(vizinho.conteudo) not in visitados.keys() or (custo_atual + vizinho.fnCusto(estado)) < visitados[tuple(vizinho.conteudo)]:
                    para_visitar.insere(Nodo(vizinho, profundidade, custo_atual+vizinho.fnCusto(estado)))

        return False


class Nodo():
    def __init__(self, estado: Estado, profundidade: int, custo: int):
        self.estado = estado
        self.profundidade = profundidade
        self.custo  = custo

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
                if nodo.custo < elem.custo: 
                    self.fila.insert(idx, nodo)
                    return

        # fila vazia ou elemento de maior custo
        self.fila.append(nodo)
        return

    def pop(self) -> (Estado, int, int):
        nodo = self.fila.pop(0)
        est, prof, cst = nodo.get()
        return est, prof, cst


