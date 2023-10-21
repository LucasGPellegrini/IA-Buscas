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

    def __str__(self, h=False) -> str:
        s:str = 'Quantidade de nos visitados = '
        s += str(self.qtd_visitados)
        s += '; \nProfundidade = '
        s += str(self.profundidade)
        s += '; \nCusto = '
        s += str(self.custo)
        s += ';\n--------------------------------\n'


        if self.passos:
            s += '\n--------------------PASSOS--------------------\n'
            for indice, est in enumerate(self.passos):
                s += f"{indice+1}º estado:\n"
                s += est.__str__()
                if h:
                    s += f"\nH = {str(est.heuristica(self.est_meta))}"
                s += f"\n\n"

        return s

