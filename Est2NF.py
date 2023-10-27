from Estado import Estado

class Est2NF(Estado):

    def __init__(self, conteudo: list[object]) -> None:
        super().__init__(conteudo)

    def heuristica(self, meta) -> int:
        h = 0
        for i, ficha in enumerate(self.conteudo[1:-1]):
            ind = i+1
            if ficha == 'B':
                print(f'ficha = {ficha} no indice {ind} h += {min(ind, (len(self.conteudo)-ind))}\n')
                if self.conteudo[ind-1] == 'P' and self.conteudo[ind+1] == 'P':
                    h += 1
            elif ficha == 'P':
                print(f'ficha = {ficha} no indice {ind} h += {min(ind, (len(self.conteudo)-ind))}\n')
                if self.conteudo[ind-1] == 'B' and self.conteudo[ind+1] == 'B':
                    h += 1
            else:
                print(self.conteudo.__str__())
                print(f'ficha = {ficha} no indice {ind} h += {min(ind, (len(self.conteudo)-ind))}\n')
                h += min(ind, (len(self.conteudo)-ind))

        return h

    def fnCusto(self, estado_ant) -> int:
        pos_vazia = self.conteudo.index('')
        pos_vazia_ant = estado_ant.conteudo.index('')

        return abs(pos_vazia - pos_vazia_ant)
