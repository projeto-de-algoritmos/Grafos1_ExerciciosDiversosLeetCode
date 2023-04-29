from typing import List

# Essa é uma questão que envolve um grafo direcionado e a busca por nós terminais, isto é, caminhos para nós que não tem arestas de saída

class Solution:
    # Apesar do grafo teoricamente estar representado como matrix, seu input é feito por lista
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        # Cria a lista auxiliar para a marcação dos visitados
        n = len(graph)
        visitado = [0] * n
        
        # Cria a DFS que retorna True se o nó em questão é "seguro"
        def DFS(no):
            visitado[no] = 1
            for vizinho in graph[no]:
                if visitado[vizinho] == 2:
                    continue
                if visitado[vizinho] == 1 or not DFS(vizinho):
                    return False # não seguro
            visitado[no] = 2
            return True
        
        return [i for i in range(n) if visitado[i] != 1 and DFS(i)]
