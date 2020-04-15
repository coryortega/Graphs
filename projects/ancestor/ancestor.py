from graph import Graph

def earliest_ancestor(ancestors, starting_node):

    # - import and create graph
        # - store vertices
        # - store edges

    # search through parents till the end, or the fursthest parent node and return that node

    # return -1 if no parent nodes



    graph = Graph()

    graph.add_vertex(10)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(4)
    graph.add_vertex(11)
    graph.add_vertex(3)
    graph.add_vertex(5)
    graph.add_vertex(8)
    graph.add_edge(10, 1)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(4, 5)
    graph.add_edge(4, 8)
    graph.add_edge(11, 8)
    graph.add_edge(3, 6)
    graph.add_edge(5, 6)
    graph.add_edge(5, 7)
    graph.add_edge(8, 9)

    # for pair in ancestors:
    #     parent = pair[0]
    #     child = pair[1]
    #     if parent not in graph.vertices:
    #         graph.add_vertex(parent)
    #     graph.add_edge(parent, child)

        # we're doing child: parent because we're traversing from bottom to top
    

    # for pair in ancestors:
    #     parent = pair[0]
    #     child = pair[1]
    #     graph.add_edge(parent, child)



    print(graph.vertices)

    graph.dfs_recursive(starting_node, 6)



    print(ancestors, starting_node)