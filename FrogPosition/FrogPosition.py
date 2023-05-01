from collections import defaultdict

# Essa questão dá um grafo, mais especificaente uma árvore não direcinada com n vértices, em que uma rã deve alcançar um nó alvo dado um tempo especifico e deve ser determinado a possibilidade disso acontecer

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # Cria a lista de adjacência que cria o grafo/ávore
        adj_list = defaultdict(list)
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        # Inicia a lista com o nó 1 visitado e para manter posteriores marcados
        visitado = [False] * (n+1)
        visitado[1] = True
        
        # Inicia a uma fila para auxuliar a BFS a atravessa-la
        queue = [(1, 1.0)]
        
        # BFS transversal
        while queue and t > 0:
            size = len(queue)
            for i in range(size):
                atual, prob = queue.pop(0)
                visinhos = [n for n in adj_list[atual] if not visitado[n]]
                num_visinhos = len(visinhos)
                if num_visinhos > 0:
                    p = 1.0 / num_visinhos
                    for neighbor in visinhos:
                        visitado[neighbor] = True
                        queue.append((neighbor, prob * p))
                else:
                    queue.append((atual, prob))
            t -= 1
        
        # Encontra a probabilidade de chegar ao nó de destino
        for node, prob in queue:
            if node == target:
                return prob
        
        return 0.0
