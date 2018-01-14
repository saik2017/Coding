from graph import*

def DFS(graph,start,end,path,shortest):
    """
    Assumes graph is a Digraph
    :param graph: Digraph
    :param start:starting node
    :param end: ending node
    :param path:path of nodes from start to end
    :param shortest: the shortest path frm start to end
    :return:shortest
    """
