class Grafo:

    def __init__(self):

        self.matriz = []
        self.lista = {}
        self.arestas = []
        self.vertices = None

    def para_matriz(self, arestas, num_vertices):
        """
        Converte uma lista de arestas em uma matriz de adjacência.

        Args:
            arestas (list of tuples): Lista de arestas, onde cada aresta é representada por um tupla (u, v).
            num_vertices (int): Número de vértices no grafo.

        Returns:
            list: Matriz de adjacência resultante.
        """
        matriz = [[0] * num_vertices for _ in range(num_vertices)]
        for u, v in arestas:
            matriz[u][v] = 1
            matriz[v][u] = 1
        return matriz

    def para_lista(self, matriz):
        """
        Converte uma matriz de adjacência em uma lista de adjacência.

        Args:
            matriz (list of lists): Matriz de adjacência do grafo.

        Returns:
            dict: Lista de adjacência resultante.
        """
        lista_adjacencia = {}
        num_vertices = len(matriz)
        for i in range(num_vertices):
            lista_adjacencia[i] = []
            for j in range(num_vertices):
                if matriz[i][j] == 1:
                    lista_adjacencia[i].append(j)
        return lista_adjacencia

    def produto_cartesiano(self, matriz1, vertices1, matriz2, vertices2):
        """
        Calcula o produto cartesiano de dois grafos dados suas matrizes de adjacência.

        Args:
            matriz1 (list of lists): Matriz de adjacência do primeiro grafo.
            vertices1 (int): Número de vértices no primeiro grafo.
            matriz2 (list of lists): Matriz de adjacência do segundo grafo.
            vertices2 (int): Número de vértices no segundo grafo.

        Returns:
            list: Matriz de adjacência do grafo resultante do produto cartesiano.
        """
        num_vertices_produto = vertices1 * vertices2
        matriz_produto = [[0] * num_vertices_produto for _ in range(num_vertices_produto)]

        for i1 in range(vertices1):
            for j1 in range(vertices1):
                for i2 in range(vertices2):
                    for j2 in range(vertices2):
                        v1 = i1 * vertices2 + i2
                        v2 = j1 * vertices2 + j2
                        if (i1 == j1 and matriz2[i2][j2] == 1) or (i2 == j2 and matriz1[i1][j1] == 1):
                            matriz_produto[v1][v2] = 1
        
        return matriz_produto

    def print_matriz(self):
        """
        Exibe a matriz de adjacência atual do grafo.
        """
        print('\n\t=================================================================')
        print("\t\t\t\tMatriz de Adjacência (G1):")
        print('\t=================================================================\n')
        labels = [x for x in range(self.vertices)]
        print(f'\t\t\t\t   {[x for x in labels]}'.replace('[', '').replace(']', '').replace(',', ' '))
        for i, row in zip(labels, self.matriz):
            print(f'\t\t\t\t{labels[i]} {row}')
        print('\n\t=================================================================')

    def print_matriz_cartesiano(self, matriz, num_vertices):
        """
        Exibe a matriz de adjacência do grafo resultante do produto cartesiano.

        Args:
            matriz (list of lists): Matriz de adjacência do grafo produto cartesiano.
            num_vertices (int): Número de vértices no grafo produto cartesiano.
        """
        print('\n\t=================================================================')
        print("\t\tMatriz de Adjacência do Produto Cartesiano (G1 X G2):")
        print('\t=================================================================\n')
        labels = [x for x in range(num_vertices)]
        print(f'\t\t\t\t   {[x for x in labels]}'.replace('[', '').replace(']', '').replace(',', ' '))
        for i, row in zip(labels, matriz):
            print(f'\t\t\t\t{labels[i]} {row}')
        print('\n\t=================================================================')

    def print_lista(self):
        """
        Exibe a lista de adjacência atual do grafo.
        """
        print('\n\n\t=================================================================')
        print("\t\t\t\tLista de Adjacência (G1):")
        print('\t=================================================================\n')
        print(f'\t\t{self.lista}')
        print('\n\t=================================================================')

    def PRINT(self):
        """
        Exibe tanto a matriz de adjacência quanto a lista de adjacência atuais do grafo.
        """
        self.print_matriz()
        self.print_lista()
