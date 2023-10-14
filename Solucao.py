from Estado import Estado

class Solucao:

    def __init__(self, qtd_visitados: int, 
                 passos: list[Estado],
                 profundidade: int,
                 est_meta: Estado, 
                 custo: int) -> None:
        self.qtd_visitados = qtd_visitados
        self.passos = passos
        self.profundidade = profundidade
        self.est_meta = est_meta
        self.custo = custo

    def __str__(self) -> str:
        s:str = 'Quantidade de estados visitados = '
        s += str(self.qtd_visitados)
        s += '; \nProfundidade = '
        s += str(self.profundidade)
        s += '; \nCusto = '
        s += str(self.custo)
        s += ';\n----------------------------\n\n'


        if self.passos:
            for indice, est in enumerate(self.passos):
                s += '-=-=-=-=-=-=-=-=-=-=-=-=-PASSOS-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
                s += f"{indice+1}-ésimo estado (com H = {str(est.heuristica(self.est_meta))})\n\n"
                s += est.__str__()

        return s

