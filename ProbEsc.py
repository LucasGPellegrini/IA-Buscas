from EstEsc import EstEsc
from Estado import Estado
from Problema import Problema
import random

class ProbEsc(Problema):

    def __init__(self, est_ini=None, est_meta=None, tipo='Simples') -> None:
        if tipo == 'Simples':
            if est_ini == None:
                self.dados = {
                        0 : {'tmp_exec':1, 'pre_reqt':[-1], 'tmp_comn':[0]},
                        1 : {'tmp_exec':2, 'pre_reqt': [0], 'tmp_comn':[1]},
                        2 : {'tmp_exec':4, 'pre_reqt': [0], 'tmp_comn':[1]},
                        3 : {'tmp_exec':2, 'pre_reqt': [1], 'tmp_comn':[1]}
                }
                
                est_ini = EstEsc([(),()], {})

            if est_meta == None:
                est_meta = EstEsc([[0,2],[1,3]], self.dados)

        if tipo == '11-1':
            pass

        if tipo == '11-2':
            pass
        if tipo == 'Gauss-18':
            if est_ini == None:
                self.dados = {
                        0 : {'tmp_exec':8, 'pre_reqt':[-1], 'tmp_comn':[0]},
                        1 : {'tmp_exec':4, 'pre_reqt': [0], 'tmp_comn':[12]},
                        2 : {'tmp_exec':4, 'pre_reqt': [0], 'tmp_comn':[12]},
                        3 : {'tmp_exec':4, 'pre_reqt': [0], 'tmp_comn':[12]},
                        4 : {'tmp_exec':4, 'pre_reqt': [0], 'tmp_comn':[12]},
                        5 : {'tmp_exec':4, 'pre_reqt': [0], 'tmp_comn':[12]},
                        6 : {'tmp_exec':6, 'pre_reqt': [0,2], 'tmp_comn':[12,8]},
                        7 : {'tmp_exec':3, 'pre_reqt': [2,6], 'tmp_comn':[8,12]},
                        8 : {'tmp_exec':3, 'pre_reqt': [3,6], 'tmp_comn':[8,12]},
                        9 : {'tmp_exec':3, 'pre_reqt': [4,6], 'tmp_comn':[8,12]},
                        10: {'tmp_exec':3, 'pre_reqt': [5,6], 'tmp_comn':[8,12]},
                        11: {'tmp_exec':4, 'pre_reqt': [6,8], 'tmp_comn':[12,8]},
                        12: {'tmp_exec':2, 'pre_reqt': [8,11], 'tmp_comn':[8,12]},
                        13: {'tmp_exec':2, 'pre_reqt': [9,11], 'tmp_comn':[8,12]},
                        14: {'tmp_exec':2, 'pre_reqt': [10,11], 'tmp_comn':[8,12]},
                        15: {'tmp_exec':2, 'pre_reqt': [11,13], 'tmp_comn':[12,8]},
                        16: {'tmp_exec':1, 'pre_reqt': [13,15], 'tmp_comn':[8,12]},
                        17: {'tmp_exec':1, 'pre_reqt': [14,15], 'tmp_comn':[8,12]}
                }
                
                est_ini = EstEsc([(),()], {})

            if est_meta == None:
                est_meta = EstEsc([[5,1,10,7,12],[0,2,6,3,8,11,4,9,13,15,16,14,17]], self.dados)

        super().__init__(est_ini, est_meta)


    def verificaObjetivo(self, estado: Estado) -> bool:
        if tuple(estado.conteudo) == tuple(self.est_meta.conteudo):
            return True
        
        return False

    def acao(self, estado: Estado) -> list[Estado]:
        vizinhos = []

        # Caso inicial
        if not estado.dados:
            vizinhos.append(EstEsc([[0],[]], {0:self.dados[0]}))
            vizinhos.append(EstEsc([[],[0]], {0:self.dados[0]}))
            return vizinhos

        # Caso geral
        proc_disponiveis = []
        for proc, pdic in self.dados.items():

            vdict = {}
            pode_alocar = True
            # processo nao alocado, com pre-requisitos alocados: alocado em um dos processadores;
            if proc not in estado.conteudo[0] and proc not in estado.conteudo[1]:
                for prereq in pdic['pre_reqt']:
                    if prereq not in estado.conteudo[0] and prereq not in estado.conteudo[1]:
                        pode_alocar = False

                    if pode_alocar:
                        vdict = estado.dados.copy()
                        vdict[proc] = pdic

                        processosp0 = estado.conteudo[0][:]
                        processosp1 = estado.conteudo[1][:] 
                        processosp0.append(proc)
                        processosp1.append(proc)

                        vizinhos.append(EstEsc([processosp0, estado.conteudo[1]], vdict))
                        vizinhos.append(EstEsc([estado.conteudo[0], processosp1], vdict))


        return vizinhos
