class Estado:

    def __init__(self, conteudo: list[object]) -> None:
        self.conteudo = conteudo

    def get(self):
        pass

    def heuristica(self, meta) -> int:
        pass

    def fnCusto(self, estado_ant) -> int:
        pass

    def __str__(self) -> str:
        return str(self.conteudo)
