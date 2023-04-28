# [Evaluate Division](https://leetcode.com/problems/evaluate-division/)

(Traduzido do inglês)

Você recebe uma matriz de pares de variáveis ​​equations e uma matriz de números reais values, onde equations [i] = [Ai, Bi] e values [i] representam a equação Ai / Bi = values [i]. Cada Ai ou Bi é uma string que representa uma única variável.

Você também recebe algumas queries, onde queries [j] = [Cj, Dj] representa a j-ésima consulta onde você deve encontrar a resposta para Cj / Dj =?.

Retorne as respostas para todas as consultas. Se uma única resposta não puder ser determinada, retorne -1.0.


Exemplo 1:

Entrada: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Saída: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explicação:
Dado: a / b = 2.0, b / c = 3.0
As consultas são: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
Retorna: [6.0, 0.5, -1.0, 1.0, -1.0]

Exemplo 2:

Entrada: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Saída: [3.75000,0.40000,5.00000,0.20000]

Exemplo 3:

Entrada: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Saída: [0.50000,2.00000,-1.00000,-1.00000]

Restrições:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consistem em letras minúsculas do alfabeto inglês e dígitos.

