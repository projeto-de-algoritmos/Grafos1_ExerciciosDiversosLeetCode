# [Frog Position After T Seconds](https://leetcode.com/problems/frog-position-after-t-seconds/description/)

(traduzido do inglês)

Dado uma árvore não-direcionada com n vértices numerados de 1 a n. Uma rã começa pulando do vértice 1. Em um segundo, a rã pula do vértice atual para outro vértice não visitado se estiverem diretamente conectados. A rã não pode pular de volta para um vértice visitado. No caso de a rã poder pular para vários vértices, ela pula aleatoriamente para um deles com a mesma probabilidade. Caso contrário, quando a rã não pode pular para nenhum vértice não visitado, ela pula para sempre no mesmo vértice.

As arestas da árvore não direcionada são dadas no array 'edges', onde 'edges[i] = [ai, bi]' significa que existe uma aresta conectando os vértices ai e bi.

Retorne a probabilidade de que, após t segundos, a rã esteja no vértice de destino. Respostas dentro de 10-5 da resposta real serão aceitas.

Exemplo 1:

Entrada: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
Saída: 0.16666666666666666

Exemplo 2:

Entrada: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
Saída: 0.3333333333333333

Restrições:

1 <= n <= 100
edges.length == n - 1
edges[i].length == 2
1 <= ai, bi <= n
1 <= t <= 50
1 <= target <= n