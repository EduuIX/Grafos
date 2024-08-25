from grafo import Grafo


class Main(Grafo):
    def __init__(self):
        super().__init__()

        self.arestas = [(0, 1), (0, 2), (1, 2), (2, 3)]
        self.vertices = 4

    def run(self):
        self.matriz = self.para_matriz(self.arestas, self.vertices)
        self.lista = self.para_lista(self.matriz)

        self.print_matriz()
        self.print_lista()


if __name__ == "__main__":
    Main().run()