from graph import Graph

def earliest_ancestor(ancestors, starting_node):

    # - import and create graph
        # - store vertices
        # - store edges

    # search through parents till the end, or the fursthest parent node and return that node

    # return -1 if no parent nodes



    graph = Graph()

    # for pair in ancestors:
    #     parent = pair[0]
    #     child = pair[1]
    #     if parent not in graph.vertices:
    #         graph.add_vertex(parent)
    #     graph.add_edge(parent, child)
    
    # for pair in ancestors:
    #     parent = pair[0]
    #     child = pair[1]
    #     graph.add_edge(parent, child)

    print(ancestors)

    for pair in ancestors:
        # (parent, child)
        parent = pair[0]
        child = pair[1]
        # adding parent once as a vertex
        if parent not in graph.vertices:
            graph.add_vertex(parent)
        # adding children as vertex, even though some wont have edges
        if child not in graph.vertices:
            graph.add_vertex(child)
        # child, parent from bottom to top
        graph.add_edge(child, parent)

    if len(graph.vertices[starting_node]) == 0:
        print("this", graph.vertices[starting_node])
        return -1
    else:
        print("here", graph.vertices)
        earliest_ancestor_path = graph.dft(starting_node)
        return earliest_ancestor_path[-1]

    