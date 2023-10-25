from Estado   import Estado
from Solucao  import Solucao
from Problema import Problema

class SEML:

    @staticmethod
    def busca(problema: Problema) -> bool:
        visitados = []
        passos = []
        custo = 0
        profundidade = 0
        qtd_visitados = 0

        corrente: Estado
        proximo: Estado

        corrente = problema.est_ini
        visitados.append(tuple(corrente.conteudo))

        movLat = []

        while True:
            passos.append(corrente)
            profundidade += 1

            # Checa Solução
            if problema.verificaObjetivo(corrente):
                problema.solucao = Solucao(qtd_visitados, passos,
                                           profundidade, problema.est_meta,
                                           custo)
                return True

            proximo, lista_movLat = problema.sucessor(corrente, visitados)
            
            for candidato in lista_movLat:
                movLat.append(Instancia(candidato, profundidade, custo))

            qtd_visitados += 1

            visitados.append(tuple(corrente.conteudo))

            valor_prox = problema.avaliacao(proximo)
            valor_corr = problema.avaliacao(corrente)

            # Checa otimo local + movimento lateral
            if valor_prox > valor_corr:
                if movLat == []:
                    return False
                
                corrente, profundidade, custo = movLat.pop(0).getInstancia()

            custo += proximo.fnCusto(corrente)
            corrente = proximo


class Instancia():
    def __init__(self, est, prf, cst):
        self.est = est
        self.prf = prf
        self.cst = cst

    def getInstancia(self):
        return (self.est, self.prf, self.cst)
