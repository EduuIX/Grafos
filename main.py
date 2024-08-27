from grafo import Grafo

class Main(Grafo):

    def __init__(self):
        super().__init__()

        self.arestas = [(0, 2), (1, 2),]
        self.vertices = 3

    def run(self):
        self.matriz = self.para_matriz(self.arestas, self.vertices)
        self.lista = self.para_lista(self.matriz)

        self.PRINT()
        
        #Gerando G2 para realizar o produto cartesiano
        G2 = Grafo()
        G2.arestas = [(0, 1)]
        G2.vertices = 2
        matriz_G2 = G2.para_matriz(G2.arestas, G2.vertices)

        resultado_produto = self.produto_cartesiano(self.matriz, self.vertices, matriz_G2, G2.vertices)
        self.print_matriz_cartesiano(resultado_produto, self.vertices * G2.vertices)

if __name__ == "__main__":
    Main().run()
