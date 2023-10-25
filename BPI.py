from Estado   import Estado
from Solucao  import Solucao
from Problema import Problema

class BPI:

    @staticmethod
    def busca(problema: Problema, maxAlt: int) -> bool:
        def __BPL__(problema: Problema, limite: int) -> bool:
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

            profundidade = 0
            for vizinho in problema.acao(estado):
                para_visitar += [(vizinho, 
                                     profundidade, 
                                     (custo_atual + vizinho.fnCusto(estado)))]

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

                # Checa limite de altura
                if profundidade >= limite:
                    return False

                # Continua busca
                for vizinho in problema.acao(estado):
                    if tuple(vizinho.conteudo) not in visitados.keys() or (custo_atual + vizinho.fnCusto(estado)) < visitados[tuple(vizinho.conteudo)]:
                        para_visitar += [(vizinho, profundidade, custo_atual+vizinho.fnCusto(estado))]


        retorno = False
        i = 1
        while (not retorno and i <= maxAlt):
            retorno = __BPL__(problema, i)
            i += 1

        return retorno
