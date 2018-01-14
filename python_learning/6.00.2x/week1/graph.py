class Node(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self,source,end):
        self.source=source
        self.end=end

    def getSource(self):
        return self.source
    def getEnd(self):
        return self.end
    def __str__(self):
        return self.source.getName()+'->'+self.end.getName()

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        # Your code here
        Edge.__init__(self,src,dest)
        self.weight=weight

    def getWeight(self):
        # Your code here
        return self.weight

    def __str__(self):
        # Your code here
        return self.source.getName()+'->'+self.end.getName()+'('+str(self.weight)+')'

class diGraph(object):
    """
    stores the graph as an adjacency list using a dict with key as nodes and values as edges starting from the node
    """
    def __init__(self):
        self.adj_list={}

    def addNode(self,node):
        if node not in self.adj_list:
            self.adj_list[node]=[]
        else:
            raise ValueError('Node already present')

    def addEdge(self,edge):
        if not (edge.getSource() in self.adj_list and edge.getEnd() in self.adj_list):
            raise ValueError('Invalid edge')
        else:
            self.adj_list[edge.getSource()].append(edge.getEnd())

    def getEdges(self,node):
        for i in self.adj_list[node]:
            edge=Edge(node,i)
            print(edge,end='  ,')


    def hasNode(self,node):
        return node in self.adj_list

    def getNode(self,name):
        for n in self.adj_list:
            if n.getName()==name:
                return n
        raise NameError(name)

    def __str__(self):
        result=''
        for start in self.adj_list:
            for end in self.adj_list[start]:
                result+=start.getName()+'->'+end.getName()+'\n'
        return result[:-1]

class Graph(diGraph):
    def addEdge(self,edge):
        diGraph.addEdge(self,edge)
        rev_edge=Edge(edge.getEnd(),edge.getSource())
        diGraph.addEdge(self,rev_edge)



# nodes = []
# nodes.append(Node("ABC")) # nodes[0]
# nodes.append(Node("ACB")) # nodes[1]
# nodes.append(Node("BAC")) # nodes[2]
# nodes.append(Node("BCA")) # nodes[3]
# nodes.append(Node("CAB")) # nodes[4]
# nodes.append(Node("CBA")) # nodes[5]
#
# g = Graph()
# for n in nodes:
#     g.addNode(n)
# edges=[]
# edges.append(Edge(nodes[0],nodes[1]))
# edges.append(Edge(nodes[3],nodes[5]))
# edges.append(Edge(nodes[3],nodes[2]))
# edges.append(Edge(nodes[1],nodes[4]))
# edges.append(Edge(nodes[4],nodes[5]))
# edges.append(Edge(nodes[0],nodes[2]))
#
# for e in edges:
#     g.addEdge(e)
# print(g)
#
#
#
