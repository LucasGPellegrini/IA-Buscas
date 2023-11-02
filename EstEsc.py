from Estado import Estado

class EstEsc(Estado):

    # conteudo = Lista de Processadores, com os processos;
    #   ex: [[0, 1, 2, 6], [3, 4, 5, 7]]
    # dados = dicionario de dicionarios com dados de cada processo;
    #   ex: 
    #  1 : {
    #       'tmp_exec' : 8,
    #       'pre_reqt' : 0, (-1 se não há)
    #       'tmp_comn' : 5  ( 0 se não há)
    #       }
    def __init__(self, conteudo: list[object], dados) -> None:
        self.dados = dados
        super().__init__(conteudo)

    def get(self) -> tuple:
        return tuple(tuple(sublist) for sublist in self.conteudo)

    def heuristica(self, meta) -> int:
        h = 0

        for processador in [0,1]:
            for processo in self.conteudo[processador]:
                if processo not in meta.conteudo[processador]: h += 1
            for processo in meta.conteudo[processador]:
                if processo not in self.conteudo[processador]: h += 1

        return h

    def fnCusto(self, estado_ant=None) -> int:
        custoP0 = 0
        custoP1 = 0

        # P0
        for processo in self.conteudo[0]:
            custo = 0
            custo += self.dados[processo]['tmp_exec']

            # verifica comunicação entre processadores
            if self.dados[processo]['pre_reqt'] != [-1]:
                for indice, prereq in enumerate(self.dados[processo]['pre_reqt']):
                    if prereq in self.conteudo[1]:
                        custo += self.dados[processo]['tmp_comn'][indice]

            custoP0 += custo

        # P1
        for processo in self.conteudo[1]:
            custo = 0
            custo += self.dados[processo]['tmp_exec']

            # verifica comunicação entre processadores
            if self.dados[processo]['pre_reqt'] != [-1]:
                for indice, prereq in enumerate(self.dados[processo]['pre_reqt']):
                    if prereq in self.conteudo[0]:
                        custo += self.dados[processo]['tmp_comn'][indice]

            custoP1 += custo

        return max(custoP0, custoP1)


