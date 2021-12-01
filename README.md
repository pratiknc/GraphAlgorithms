Project name: Graph Algorithms
<br>
<br>The project implements uses graph-based algorithms to tackle two problems –
<br>
<br>1. Single-source Shortest Path – Find shortest path tree in both directed and undirected weighted 
<br>graphs for a given source vertex. To do so, we make use of Dijkstra’s Algorithm.
<br>2. Minimum Spanning Tree Algorithm – Given a connected, undirected, weighted graph, find a spanning 
<br>tree using edges that minimizes the total weight. To find this, we use Kruskal’s Algorithm.
<br>
<br>The driver file takes the following aspects as input –
<br>1. A text file containing graph details – This file will be placed at a user preferred location and the user 
<br>will be required to mention the entire file name when prompted.
<br>2. The algorithm to run – Based on which algorithm – Shortest path or Minimum Spanning tree, the user 
<br>will be required to input either (1) for shortest path or (2) for Minimum Spanning Tree.
<br>3. For shortest path algorithm, if the user has not provided a source vertex, then the program will 
<br>randomly select a vertex from the graph as source vertex and run Dijkstra’s Algorithm.
<br>4. If minimum spanning tree is selected, then user will be provided an option to display the MST.
<br><br>Prerequisites:
<br>Before you begin, ensure you have met the following requirements:
<br>• You have installed Python version 3.7+
<br>• You have installed networkx version 2.5 and matplotlib libraries.
<br>pip install networkx
<br><br>All Operating Systems are supported.
<br><br>Usage:
<br>1. Extract the zip file on desired path.
<br>2. Navigate to src folder.
<br>3. Run Driver.py –
<br>python Driver.py
<br><br>On execution, follow the prompts –
<br>"Enter file name storing Graph information:" – This is the absolute path of the input file which stores the 
<br>graph details.
<br>Example - C:\Users\<user>\myProjects\Project2\Programs\Graph\input_graph\network.txt
<br><br>The code will check if such a file exists, else will throw an error and ask for file name again.
<br>If a file is found, the user will be prompted for a choice –
<br>Enter problem number to solve:
1. Shortest Path Problem
2. Minimum Spanning Tree
3. To exit
<br>If user selects 1 – Shortest path from source vertex to every other vertex of the graph will be calculated
and result will de displayed. In case the input file given by the user doesn’t have a source vertex, the 
driver program will randomly select a vertex from the graph and find shortest path from that vertex to 
every other vertex.
<br>If user selects 2 – Based on the input file a Minimum Spanning Tree (MST) will be calculated and all the 
edges that are a part of the spanning tree will be displayed along with its weight. User will also be 
prompted if the MST needs to be displayed. If a directed graph is provided, the program will display 
below message prior to beginning finding MST –
Cannot find Minimum Spanning Tree for Directed Graph.
<br>If user selects 3 – The program will exit
