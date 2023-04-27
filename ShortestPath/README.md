# [Shortest Path with Alternating Colors](https://leetcode.com/problems/shortest-path-with-alternating-colors/)

(Traduzido do inglês)

Você recebe um número inteiro n, o número de nós em um grafo direcionado onde os nós são rotulados de 0 a n - 1. Cada aresta é vermelha ou azul neste grafo, e pode haver auto-arestas e arestas paralelas.

Você recebe duas matrizes de arestas redEdges e blueEdges onde:

redEdges[i] = [ai, bi] indica que há uma aresta vermelha direcionada do nó ai para o nó bi no grafo, e
blueEdges[j] = [uj, vj] indica que há uma aresta azul direcionada do nó uj para o nó vj no grafo.
Retorne uma matriz de resposta de comprimento n, onde cada resposta[x] é o comprimento do caminho mais curto do nó 0 ao nó x, de modo que as cores das arestas se alternem ao longo do caminho, ou -1 se tal caminho não existir.

Exemplo 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]

Restrições:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n