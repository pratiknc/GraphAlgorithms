import networkx as nx


class GraphTypeDefinitionException(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class InitializeGraph:
    def __InitializeUndirectedGraph(self, graph_details):
        """
        The method will initialize undirected graph.
        :param graph_details:
        :return: Graph object
        """
        G = nx.Graph()
        return G

    def __InitializeDirectedGraph(self, graph_details):
        """
        The method will initialize directed graph.
        :param graph_details:
        :return: Graph object
        """
        G = nx.DiGraph()
        return G

    def __ConstructGraph(self, G, graph_details):
        """
        The method will create a graph based on the vertices and edges information.
        :param G: input graph object.
        :param graph_details: vertices and edges information from input text file.
        :return: Graph object
        """
        for data in graph_details:
            G.add_edge(data[0], data[1], weight=int(data[2]))
        return G

    def getGraph(self):
        """
        Getter function for graph.
        :return: Graph object
        """
        return self.__G

    def getSource(self):
        """
        Getter function for source vertex of a directed graph.
        :return: Source vertex of graph.
        """
        return self.__source

    def __init__(self, file_name):
        """
        Initialize the input text file in a graph object. This will be used to find shortest path and minimum
        spanning tree.
        :param file_name: Text file input with details on vertices and edges to construct a graph.
        """

        graph_details = [i.strip('\n').split(' ') for i in open(file_name)]

        if len(graph_details[len(graph_details) - 1]) == 1:
            self.__source = graph_details.pop().pop()
        else:
            self.__source = None

        graph_params = graph_details.pop(0)
        graph_type = graph_params.pop()

        if graph_type.upper() == 'U':
            self.__G = self.__InitializeUndirectedGraph(graph_details)
        elif graph_type.upper() == 'D':
            self.__G = self.__InitializeDirectedGraph(graph_details)
        else:
            error_msg = "Graph Type Definition '" + str(graph_type.upper()) + "' is incorrect"
            raise GraphTypeDefinitionException(error_msg)

        self.__ConstructGraph(self.__G, graph_details)


if __name__ == "__main__":
    print()
    print('Class to Initialize Graph from input file')
