from GraphAlgorithms import GraphAlgorithms
import InitializeGraph as IG

"""This part of the code is used to take user input for creating the graph and calling initialization functions for 
the same.
Error handling in case file path is incorrect. """
while True:
    try:
        initializer = IG.InitializeGraph(input("Enter file name storing Graph information: "))
        break
    except FileNotFoundError:
        print("Please Enter Valid File Name -- <file.extension>")
    except IG.GraphTypeDefinitionException as e:
        print(e)
    except:
        print('Critical Failure')
        exit(-1)

G = initializer.getGraph()
source = initializer.getSource()
algos = GraphAlgorithms()
while True:
    problem = int(input("Enter problem number to solve:\n\t1. Shortest Path Problem\n\t2. Minimum Spanning Tree\n\t"
                        "3. To exit\n"))
    if problem == 1:
        print('Shortest Path from given source to each vertex')
        algos.ShortestPath(G, source)
    elif problem == 2:
        print_mst_graph = True if str(input("Do you want to display the minimum spanning tree? (Y/N)")).upper() == 'Y' \
            else False
        print('Minimum Spanning Tree using Kruskal\'s Algorithm')
        algos.MinimumSpanningTree(G, print_mst_graph)
    elif problem == 3:
        exit(0)
    else:
        print("Incorrect selection!")
