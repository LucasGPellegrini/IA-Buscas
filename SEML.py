from Estado   import Estado
from Solucao  import Solucao
from Problema import Problema

class SEML:

    @staticmethod
    def busca(problema: Problema) -> bool:
        # para_visitar -> Lista: (Estado, profundidade, custo)
        para_visitar = []

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
            para_visitar += [(vizinho, 
                                 profundidade, 
                                 (custo_atual + vizinho.fnCusto(estado)))]


        # Movimentos Laterais
        mov_lat = []

        # Algoritmo Geral:
        while para_visitar:
            
            candidatos_ord = sorted(para_visitar, key=lambda tup: tup[2])
            
            qtd = 1, i = 1
            while i <= len(candidatos_ord):
                if candidatos_ord[i][2] == candidatos_ord[i-1][2]:
                    qtd += 1
                i += 1

            menores = candidatos_ord[:qtd]

            para_visitar = menores.pop()

            while menores:
                est, prf, cst = menores.pop()
                inst = Instancia(visitados, qtd_explorada, passos,
                                 est, prf, cst)

                mov_lat.append(inst)
            
            custo_anterior = custo_atual
            
            estado, profundidade, custo_atual = para_visitar.pop()
            visitados[tuple(estado.conteudo)] = custo_atual
            qtd_explorada += 1
            
            #print(f'Explorei o estado: {estado.__str__()}\n')
            #print(f'Qtd de nós explorados: {qtd_explorada}\n')
            #print(f'Profundidade: {profundidade}, Custo: {custo_atual}\n\n')

            # Checa solução
            if problema.verificaObjetivo(estado):
                problema.solucao = Solucao(qtd_explorada, passos, 
                                           profundidade, problema.est_meta, custo_atual)
                return True
            # Checa Min local
            else:
                if custo_anterior < custo_atual:
                    #lateral = True
                    inst = mov_lat.pop()
                    visitados, qtd_explorada, passos, estado, profundidade, custo_atual = inst.getInstancia()

            # Continua busca
            profundidade += 1
            for vizinho in problema.acao(estado):
                if tuple(vizinho.conteudo) not in visitados.keys() or (custo_atual + vizinho.fnCusto(estado)) < visitados[tuple(vizinho.conteudo)]:
                    para_visitar += [(vizinho, profundidade, custo_atual+vizinho.fnCusto(estado))]


class Instancia():
    def __init__(self, vtd, qtd, pss, est, prf, cst):
        this.vtd = vtd
        this.qtd = qtd
        this.pss = pss
        this.est = est
        this.prf = prf
        this.cst = cst

    def getInstancia():
        return (this.vtd, this.qtd, this.pss,
                this.est, this.prf, this.cst)
