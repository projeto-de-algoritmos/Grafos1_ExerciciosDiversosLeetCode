from typing import List


#Essa é uma questão que avalia consultas requisitadas para dadas equações de disião entre números reais


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # Cria o grafo e o popula com as equações e valores, adicionado os nós de origem(src) e destino(dst)
        graph = {}
        
        for i in range(len(equations)):
            src, dst = equations[i]
            value = values[i]
            if src not in graph:
                graph[src] = {}
            if dst not in graph:
                graph[dst] = {}
        # As linhas abaixo se dao pela adição de valores reciprocos, ja que é um grafo direcionado        
            graph[src][dst] = value
            graph[dst][src] = 1 / value

        # Cria uma DFS para as consultas
        def DFS(src, dst, visitado):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visitado.add(src)
            for vizinho in graph[src]:
                if vizinho not in visitado:
                    resultado = DFS(vizinho, dst, visitado)
                    if resultado != -1.0:
                        return graph[src][vizinho] * resultado
            return -1.0

        #  Processa cada consulta usando a DFS e armazenando os resultadoados na lista de respostas
        resposta = []
        for query in queries:
            src, dst = query
            visitado = set()
            resposta.append(DFS(src, dst, visitado))

        return resposta