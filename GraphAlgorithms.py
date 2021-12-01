from math import inf
from queue import PriorityQueue
import networkx as nx
import random
import matplotlib.pyplot as plt


class GraphAlgorithms:

    def __dijkstra(self, input_graph, source):
        """
        This method (private) implements Dijkstra's Algorithm to find the shortest path from source vertex to every
        other vertex of the graph.
        :param input_graph: Graph on which the algorithm will run.
        :param source: Source vertex from which distances to all other vertices are calculated.
        :return: shortest distances of all vertices along with information on the parent nodes.
        """
        parent_nodes = {v: str(None) for v in list(input_graph.nodes)}
        distance = {v: inf for v in list(input_graph.nodes)}
        visited = set()
        pq = PriorityQueue()
        distance[source] = 0
        pq.put((distance[source], source))
        while pq.qsize() != 0:
            vertex = pq.get()[1]

            if vertex in visited:
                continue
            for adj_vertex in list(input_graph.neighbors(vertex)):
                if adj_vertex not in visited:
                    new_distance = int(distance[vertex] + input_graph.get_edge_data(vertex, adj_vertex).get('weight'))

                    if distance[adj_vertex] > new_distance:
                        distance[adj_vertex] = new_distance
                        pq.put((distance[adj_vertex], adj_vertex))
                        parent_nodes[adj_vertex] = vertex
            visited.add(vertex)
        return distance, parent_nodes

    def __CalculateDistances(self, distances, parent_nodes, nodes, source):
        """
        The method (private) will print distances to each vertex calculated from Dijkstra's Algorithm along with the
        path from source.
        :param distances: shortest distances to each vertex from the source.
        :param parent_nodes: parent node of each vertex.
        :param nodes: all vertices of the graph except source.
        :param source: source vertex of the graph.
        """
        paths = []
        for node in nodes:
            path = node + ': ' + str(distances[node])
            while node != source:
                path = parent_nodes[node] + '-' + path
                node = parent_nodes[node]
            paths.append(path)
        print(paths)

    def ShortestPath(self, G, source):
        """
        The method is a calling function for Dijkstra's Algorithm.
        :param G: Input graph.
        :param source: Source vertex of the graph.
        """
        if source is None:
            print("Source vertex is not provided. Randomly selecting a source vertex")
            source = random.choice(list(G.nodes()))
            print("Randomly selected source vertex is: ", source)
        else:
            print("Source vertex provided by the user: ", source)
        distances, parent_nodes = self.__dijkstra(G, source)
        nodes = list(G.nodes)
        nodes.remove(source)
        self.__CalculateDistances(distances, parent_nodes, nodes, source)

    def __kruskal_algo(self, G):
        """
        This method (private) implements Kruskal's Algorithm to find the minimum spanning tree of the graph.
        :param G: Input graph.
        :return: All edges of the graph that are part of the spanning tree.
        """
        min_spanning_tree = nx.Graph()
        graph_sorted_edge_list = sorted(G.edges(data=True), key=lambda t: t[2].get('weight', 1))
        for edge in graph_sorted_edge_list:
            if min_spanning_tree.number_of_edges() >= G.number_of_nodes():
                break
            min_spanning_tree.add_edges_from([edge])
            try:
                nx.find_cycle(min_spanning_tree, orientation="ignore")
                min_spanning_tree.remove_edges_from([edge])
            except:
                continue
        print('Edge list with Weights')
        print('\t', end='')
        print(min_spanning_tree.edges(data=True))
        # To validate result uncomment below.
        # print(nx.minimum_spanning_tree(G, weight='weight').edges(data=True))
        print('Total Weight of Tree: ', end='')
        print(min_spanning_tree.size(weight='weight'))
        return min_spanning_tree

    def __GraphPlot(self, G):
        """
        The method (private) will display the spanning tree calculated by Kruskal's Algorithm.
        :param G: Input graph.
        """
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        labels = {e: G.edges[e]['weight'] for e in G.edges}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        # plt.show()
        plt.savefig("graph.png")

    def MinimumSpanningTree(self, G, show_graph=False):
        """
        The method will check if the input graph is a directed or undirected graph. If directed, MST will not be called
        and appropriate message will be displayed.
        :param G: Input graph.
        :param show_graph: If yes, MST will be displayed.
        """
        if nx.is_directed(G):
            print('\tCannot find Minimum Spanning Tree for Directed Graph')
        else:
            min_spanning_tree = self.__kruskal_algo(G)
            if show_graph:
                self.__GraphPlot(min_spanning_tree)


if __name__ == "__main__":
    print()
    print('Class implementing Graph Algorithms')
