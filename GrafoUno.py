import networkx as nx
import pylab

grafo = nx.DiGraph()

grafo.add_edges_from([('1', '2'),('5','9'),('3','8'),('4','7'),('7','10')], costo=8)
grafo.add_edges_from([('5','10'),('8','11'),('10','12')], costo=6)
grafo.add_edges_from([('2','5'),('1','4')], costo=9)
grafo.add_edges_from([('3','5'),('3','7')], costo=5)
grafo.add_edges_from([('1','3'),('3','6'),('7','11')], costo=7)
grafo.add_edges_from([('4','8'),('9','12')], costo=14)
grafo.add_edges_from([('2','6')], costo=10)
grafo.add_edges_from([('6','10')], costo=3)
grafo.add_edges_from([('6','9')], costo=4)
grafo.add_edges_from([('8','10')], costo=12)
grafo.add_edges_from([('11','12')], costo=15)

solucion = [('1','3'),('3','6'),('6','10'),('10','12')]

color_aristas = ['black' if not arista in solucion else 'red' for arista in grafo.edges()]

valores = {
    'node_color': 'yellow',
    'node_size': 170,
    'width': 1,
    'arrowsize': 12
}

nx.draw_networkx(grafo, **valores,edge_color = color_aristas)
pylab.show()