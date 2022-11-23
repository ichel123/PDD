from numpy import inf
import networkx as nx
import pylab


#grafo = {'1':{'2':8,'3':7,'4':9},'2':{'5':9,'6':10},'3':{'5':5,'6':7,'7':5,'8':8},'4':{'7':8,'8':14},'5':{'9':8,'10':6},'6':{'9':4,'10':3},'7':{'9':11,'10':8,'11':7},'8':{'10':12,'11':6},'9':{'12':14},'10':{'12':6},'11':{'12':15},'12':{'12':0}}
#grafo = {'1':{'2':2,'3':4,'4':3},'2':{'5':7,'6':4,'7':6},'3':{'5':3,'6':2,'7':4},'4':{'5':4,'6':1,'7':5},'5':{'8':1,'9':4},'6':{'8':6,'9':3},'7':{'8':3,'9':3},'8':{'10':3},'9':{'10':4},'10':{'10':0}}
grafo = {'A':{'B':8,'C':3,'D':6},'B':{'E':4,'F':7},'C':{'E':5},'D':{'E':9,'F':7},'E':{'G':7},'F':{'G':6},'G':{'G':0}}

def calcular_camino(grafo,i,f):
    min_camino = {}
    anterior = {}
    nodos = grafo
    camino = []
    for nodo in nodos:
        min_camino[nodo] = inf
    min_camino[i] = 0
 
    while nodos:
        nodoMin = None
        for nodo in nodos:
            if nodoMin is None:
                nodoMin = nodo
            elif min_camino[nodo] < min_camino[nodoMin]:
                nodoMin = nodo
 
        for nodoHijo, costo in grafo[nodoMin].items():
            if costo + min_camino[nodoMin] < min_camino[nodoHijo]:
                min_camino[nodoHijo] = costo + min_camino[nodoMin]
                anterior[nodoHijo] = nodoMin
        nodos.pop(nodoMin)
 
    nodoActual = f
    while nodoActual != i:
        try:
            camino.insert(0,nodoActual)
            nodoActual = anterior[nodoActual]
        except KeyError:
            print('No existe un camino')
            break
    camino.insert(0,i)
    if min_camino[f] != inf:
        print('El costo mínimo es ' + str(min_camino[f]))
        print('Y el camino es ' + str(camino))
 
calcular_camino(grafo, 'A', 'G')

grafo = nx.DiGraph()

############## EJERCICIO 1 ############## 
# grafo.add_edges_from([('1', '2'),('5','9'),('3','8'),('4','7'),('7','10')], costo=8)
# grafo.add_edges_from([('5','10'),('8','11'),('10','12')], costo=6)
# grafo.add_edges_from([('2','5'),('1','4')], costo=9)
# grafo.add_edges_from([('3','5'),('3','7')], costo=5)
# grafo.add_edges_from([('1','3'),('3','6'),('7','11')], costo=7)
# grafo.add_edges_from([('4','8'),('9','12')], costo=14)
# grafo.add_edges_from([('2','6')], costo=10)
# grafo.add_edges_from([('6','10')], costo=3)
# grafo.add_edges_from([('6','9')], costo=4)
# grafo.add_edges_from([('8','10')], costo=12)
# grafo.add_edges_from([('11','12')], costo=15)

# solucion = [('1','3'),('3','6'),('6','10'),('10','12')]

############## EJERCICIO 2 ############## 
# grafo.add_edges_from([('1', '3'),('3','7'),('2','6'),('4','5'),('5','9'),('9','10')], costo=4)
# grafo.add_edges_from([('1', '4'),('3','5'),('6','9'),('7','8'),('7','9'),('8','10')], costo=3)
# grafo.add_edges_from([('1','2'),('3','6')], costo=2)
# grafo.add_edges_from([('5','8'),('4','6')], costo=1)
# grafo.add_edges_from([('2','7'),('6','8')], costo=6)
# grafo.add_edges_from([('4','7')], costo=5)
# grafo.add_edges_from([('2','5')], costo=7)

# solucion = [('1','4'),('4','6'),('6','9'),('9','10')]

############## EJERCICIO 3 ##############
grafo.add_edges_from([('B', 'F'),('E','G'),('D','F')], costo=7)
grafo.add_edges_from([('A','D'),('F','G')], costo=6)
grafo.add_edges_from([('A','B')], costo=8)
grafo.add_edges_from([('A','C')], costo=3)
grafo.add_edges_from([('B','E')], costo=4)
grafo.add_edges_from([('D','E')], costo=9)
grafo.add_edges_from([('C','E')], costo=5)

solucion = [('A','C'),('C','E'),('E','G')]
 
color_aristas = ['black' if not arista in solucion else 'red' for arista in grafo.edges()]

valores = {
    'node_color': 'yellow',
    'node_size': 170,
    'width': 1,
    'arrowsize': 12
}

nx.draw_networkx(grafo, **valores,edge_color = color_aristas)
pylab.show()
