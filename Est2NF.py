from Estado import Estado

class Est2NF(Estado):

    def __init__(self, conteudo: list[object]) -> None:
        super().__init__(conteudo)

    def heuristica(self, meta) -> int:
        h = 0
        for ind, ficha in enumerate(self.conteudo[1:-1]):
            if ficha == 'B':
                if self.conteudo[ind-1] == 'P' and self.conteudo[ind+1] == 'P':
                    h += 1
            elif ficha == 'P':
                if self.conteudo[ind-1] == 'B' and self.conteudo[ind+1] == 'B':
                    h += 1
            else:
                h += min(ind, (len(self.conteudo)-ind))

        return h

    def fnCusto(self, estado_ant) -> int:
        pos_vazia = self.conteudo.index('')
        pos_vazia_ant = estado_ant.conteudo.index('')

        return abs(pos_vazia - pos_vazia_ant)
