import networkx as nx
import pylab

grafo = nx.DiGraph()

grafo.add_edges_from([('1', '3'),('3','7'),('2','6'),('4','5'),('5','9'),('9','10')], costo=4)
grafo.add_edges_from([('1', '4'),('3','5'),('6','9'),('7','8'),('7','9'),('8','10')], costo=3)
grafo.add_edges_from([('1','2'),('3','6')], costo=2)
grafo.add_edges_from([('5','8'),('4','6')], costo=1)
grafo.add_edges_from([('2','7'),('6','8')], costo=6)
grafo.add_edges_from([('4','7')], costo=5)
grafo.add_edges_from([('2','5')], costo=7)

solucion = [('1','4'),('4','6'),('6','9'),('9','10')]

color_aristas = ['black' if not arista in solucion else 'red' for arista in grafo.edges()]

valores = {
    'node_color': 'yellow',
    'node_size': 170,
    'width': 1,
    'arrowsize': 12
}

nx.draw_networkx(grafo, **valores,edge_color = color_aristas)
pylab.show()