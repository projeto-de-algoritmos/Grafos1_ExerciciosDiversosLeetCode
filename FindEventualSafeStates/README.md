# [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/)

(Traduzido do inglês)

Há um grafo direcionado com n nós, cada nó rotulado de 0 a n - 1. O grafo é representado por uma matriz de inteiros 2D indexada em 0, chamada 'graph', onde graph[i] é uma matriz de inteiros que representa os nós adjacentes ao nó i, ou seja, há uma aresta do nó i para cada nó em graph[i].

Um nó é um nó terminal se não há arestas de saída dele. Um nó é um nó seguro se todo caminho possível a partir desse nó leva a um nó terminal (ou a outro nó seguro).

Retorne uma matriz contendo todos os nós seguros do grafo. A resposta deve estar ordenada em ordem crescente.

Exemplo 1:

Ilustração do grafo
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: O grafo dado é mostrado acima.
Os nós 5 e 6 são nós terminais, pois não há arestas de saída de nenhum deles.
Todos os caminhos começando nos nós 2, 4, 5 e 6 levam ao nó 5 ou 6.
Exemplo 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Apenas o nó 4 é um nó terminal, e todo caminho começando no nó 4 leva ao próprio nó 4.

Restrições:

n == graph.length
1 <= n <= 104
0 <= graph[i].length <= n
0 <= graph[i][j] <= n - 1
graph[i] está ordenado em ordem estritamente crescente.
O grafo pode conter laços de auto-relação.
O número de arestas no gráfico estará no intervalo [1, 4 * 104].