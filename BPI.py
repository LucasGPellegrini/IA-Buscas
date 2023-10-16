from Estado   import Estado
from Solucao  import Solucao
from Problema import Problema

class BPI:

    @staticmethod
    def busca(problema: Problema, maxAlt: int) -> bool:
        def __BPL__(problema: Problema, limite: int) -> bool:
            # para_visitar -> Lista: (Estado, profundidade, custo)
            para_visitar = []

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
                para_visitar.extend((vizinho, profundidade, custo_atual+vizinho.fnCusto()))

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

                # Checa limite de altura
                if profundidade == limite:
                    return False

                # Continua busca
                profundidade += 1
                for vizinho in problema.acao(estado):
                    if vizinho not in visitados.keys() or (custo_atual + vizinho.fnCusto()) < visitados[vizinho]
                        para_visitar.extend((vizinho, profundidade, custo_atual+vizinho.fnCusto()))


        retorno = False
        altura = 1
        i = 1
        while (not retorno or altura >= maxAlt):
            retorno = __BPL__(problema, i)
            i += 1

        return retorno
