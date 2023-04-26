from typing import List #tornar o codigo mais legivel
from collections import defaultdict #facilita para o uso de dados alternativos


#Esse é um problema no que diz respeito a matrpicula em um novo curso e os prerequisitos necessários para cursa-lo, bbuscando por formas de evitar um loop ou cilcos infinitos de pre reqwuisitos

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # criar uma lista de adjacencia para representar o grafo,como exigido do problema
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        # cria uma lista que vcai servir como marcação dos nós já visitados
        visitado = [0] * numCourses

        # funcao recursiva para encontrar ciclos no grafo, isto é, uma DFS
        def cicloExiste_DFS(no):
            if visitado[no] == -1:  # está sendo visitado, portanto há ciclos
                return True
            if visitado[no] == 1:  # já foi visitado, então não há ciclos
                return False
            visitado[no] = -1  # marca o nó como em processo de visita
            for neighbor in graph[no]:
                if cicloExiste_DFS(neighbor):
                    return True
            visitado[no] = 1  #marca o nó como visitado
            return False

        # procura por ciclos
        for i in range(numCourses):
            if cicloExiste_DFS(i):
                return False

        return True
