class Grafo():


    def __init__(self):
        self.matriz = []
        self.lista = {}
    

    def para_matriz(self, arestas, num_vertices):
        """
            Gera a matriz de adjacência de um grafo não direcionado a partir de uma lista de arestas.

            Esta função cria uma matriz de adjacência representando um grafo não direcionado. A matriz de adjacência é uma forma de representar um grafo onde as linhas e colunas correspondem aos vértices, e os valores da matriz indicam a presença ou ausência de arestas entre os vértices.

            Parâmetros:
            ----------
            arestas : list of tuples
                Uma lista de tuplas, onde cada tupla (u, v) representa uma aresta entre os vértices u e v no grafo.
            
            num_vertices : int
                O número de vértices no grafo. A matriz de adjacência gerada terá dimensões num_vertices x num_vertices.

            Retorna:
            --------
            list of list of int
                A matriz de adjacência do grafo. Uma lista de listas, onde cada sublista representa uma linha da matriz. Um valor 1 na posição [i][j] indica a presença de uma aresta entre os vértices i e j, e 0 indica ausência de aresta.

            Exemplo:
            --------
            >>> arestas = [(0, 1), (0, 2), (1, 2), (2, 3)]
            >>> num_vertices = 4
            >>> grafo = Grafo()
            >>> matriz_adj = grafo.matriz(arestas, num_vertices)
            >>> print(matriz_adj)
            [[0, 1, 1, 0],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [0, 0, 1, 0]]
        """

        matriz = [[0] * num_vertices for _ in range(num_vertices)]
        for u, v in arestas:
            matriz[u][v] = 1
            matriz[v][u] = 1 

        return matriz


    def para_lista(self, matriz):
        """
            Converte uma matriz de adjacência em uma lista de adjacência.

            Esta função transforma uma matriz de adjacência, que representa um grafo, em uma lista de adjacência. A lista de adjacência é uma estrutura de dados que armazena, para cada vértice, uma lista de vértices adjacentes, ou seja, os vértices com os quais está conectado.

            Parâmetros:
            ----------
            matriz : list of list of int
                Uma matriz de adjacência onde cada elemento matriz[i][j] é 1 se existe uma aresta entre os vértices i e j, e 0 caso contrário.

            Retorna:
            --------
            dict
                Um dicionário representando a lista de adjacência do grafo. As chaves são os vértices do grafo, e os valores são listas dos vértices adjacentes a cada chave.

            Exemplo:
            --------
            >>> matriz = [
            ...     [0, 1, 1, 0],
            ...     [1, 0, 1, 0],
            ...     [1, 1, 0, 1],
            ...     [0, 0, 1, 0]
            ... ]
            >>> grafo = Grafo()
            >>> lista_adj = grafo.lista(matriz)
            >>> print(lista_adj)
            {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
        """
        lista_adjacencia = {}
        num_vertices = len(matriz)
        for i in range(num_vertices):
            lista_adjacencia[i] = []
            for j in range(num_vertices):
                if matriz[i][j] == 1:
                    lista_adjacencia[i].append(j)

        return lista_adjacencia


    def print_matriz(self):
        print("Matriz de Adjacência:")
        for row in self.matriz:
            print(row)


    def print_lista(self):
        print("Lista de Adjacência:", self.lista)
