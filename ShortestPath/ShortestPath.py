from typing import List


# Essa questão avalia , em um grafo com duas cores mas não bipartido, a menor distância entre dados nós, com alteracçao de cores, sendo que podem existir mais de uma aresta entre dois mesmos nós 
# ou arestas que inccidem sobre o própio nó.

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        #  Criar lista de ajacência para os nós vermelhos e azuis
        red_adj = {i: [] for i in range(n)}
        blue_adj = {i: [] for i in range(n)}
        for i, j in redEdges:
            red_adj[i].append(j)
        for i, j in blueEdges:
            blue_adj[i].append(j)
        
        # Criar arrays que "medem" a distância com nós vermelhos e azuis
        red_dist = [-1] * n
        blue_dist = [-1] * n
        
        # Cria fila e inicializa o nó
        queue = [(0, 'red'), (0, 'blue')]
        red_dist[0] = blue_dist[0] = 0
        
        # BFS para encontrar o menor caminho que alterna entre as cores
        while queue:
            node, color = queue.pop(0)
            if color == 'red':
                for neighbor in red_adj[node]:
                    if red_dist[neighbor] == -1:
                        red_dist[neighbor] = blue_dist[node] + 1
                        queue.append((neighbor, 'blue'))
            else:
                for neighbor in blue_adj[node]:
                    if blue_dist[neighbor] == -1:
                        blue_dist[neighbor] = red_dist[node] + 1
                        queue.append((neighbor, 'red'))
        
        # Criar array resultante
        result = []
        for i in range(n):
            if red_dist[i] == -1 and blue_dist[i] == -1:
                result.append(-1)#não tem caminho
            else:
                result.append(min(dist for dist in (red_dist[i], blue_dist[i]) if dist != -1))#há caminho
        
        return result
