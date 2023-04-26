# [Course Schedule](https://leetcode.com/problems/course-schedule/description/)

(Traduzido do inglês)

Existem um total de numCourses cursos que você precisa fazer, numerados de 0 a numCourses - 1. É fornecido um array de pré-requisitos chamado prerequisites, onde prerequisites[i] = [ai, bi] indica que você precisa fazer o curso bi primeiro se quiser fazer o curso ai.

Por exemplo, o par [0, 1] indica que para fazer o curso 0 você precisa primeiro fazer o curso 1.
Retorne verdadeiro se você puder concluir todos os cursos. Caso contrário, retorne falso.


Exemplo 1:

Entrada: numCourses = 2, prerequisites = [[1,0]]
Saída: verdadeiro
Explicação: Existem um total de 2 cursos para fazer.
Para fazer o curso 1, você deve ter terminado o curso 0. Portanto, é possível.

Exemplo 2:

Entrada: numCourses = 2, prerequisites = [[1,0],[0,1]]
Saída: falso
Explicação: Existem um total de 2 cursos para fazer.
Para fazer o curso 1, você deve ter terminado o curso 0 e para fazer o curso 0 você também deve ter terminado o curso 1. Portanto, é impossível.

Restrições:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
Todos os pares prerequisites[i] são únicos.

