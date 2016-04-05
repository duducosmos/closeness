from numpy import loadtxt, array, sort, unique, where, zeros

"""
The centrality algorithm was written based in the work of Freman (1979)
and in the information in the
site https://en.wikipedia.org/wiki/Centrality#Closeness_centrality.

References:
Freeman L. C. Centrality in Social Networks Conceptual Clarification. Social
Networks. 1979. 1. 215.
"""

class CentralityMetrics:
    def __init__(self, edges=None, graphArq='edges'):

        if(graphArq is not None and edges is None):
            self.graphArq = graphArq
            self.edges = self.__loadEdges(self.graphArq)
        else:
            if(edges is None):
                raise NameError('Not edges entry.')
            else:
                self.edges = edges
        self.vertices = unique(sort(self.edges[:,1]))

    def __loadEdges(self, graphArq):
        with open(graphArq) as arq:
            edges = loadtxt(arq, delimiter=" ")
            edges = edges.astype(int)
        return edges

    def farness(self, pi, p):
        allpi = where(p == pi)[0].size - 1
        return allpi

    def closeness(self, pi, p):
        return 1.0 /  self.farness(pi, p)

    def rankedVerticesCloseness(self):
        farnessForAll = array([self.farness(vi, self.edges)
                for vi in self.vertices])
        n = farnessForAll.size
        rank = farnessForAll
        vc = self.vertices
        for i in range(n):
            mi = i
            for j in range(i + 1, n):
                if(farnessForAll[j] > farnessForAll[mi]):
                    mi = j
            if(mi != i):
                rank[i], rank[mi] = rank[mi], rank[i]
                vc[i], vc[mi] = vc[mi], vc[i]
        return vc, 1.0 / rank

if(__name__ == "__main__"):
    centralityMertrics = CentralityMetrics(graphArq='edges')
    vrank = centralityMertrics.rankedVerticesCloseness()
    print('Vertices ordenados:')
    print(vrank[0])
    print('')
    print('closeness:')
    print(vrank[1])
