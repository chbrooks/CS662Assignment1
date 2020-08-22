import pickle

### build graph: 
### takes as input a file in the form:
## a b dist time
### where a and b are destinations, dist is the distance between them, and 
### time is the time needed to travel between them and constructs a graph.

### This graph should be represented as an adjacency list, and stored as a 
### dictionary, with the key in the dictionary being the source of an edge and 
### the value being a tuple containing the destination, distance, and cost.
### For example:
### g[a] = (b,dist,time)

class graph() :
    def __init__(self, infile=None) :
        self.adjlist = {}
        if infile :
            self.buildGraph(infile)


    ### method to print a graph.
    def __repr__(self) :


### method that takes as input a file name and constructs the graph described 
### above. Assume that the file has the format used in the 'sfdata' file.

    def buildGraph(self, infile) :

    

### this method should use the Floyd-Warshall algorithm to compute all-pairs shortest path on the graph, and return a matrix of distances, 
### stored as a list of lists.


    def floydWarshall(self) :


class edge() :
    def __init__(self, src, dest, cost) :
        self.src = src
        self.dest = dest
        self.cost = cost

class vertex(self, name, xval, yval) :
    self.name = name
    self.xval = xval
    self.yval = yval

### usage: buildGraph {--pfile=outfile} {-p} infile
### if --pfile=outfile is provided, write a pickled version of the graph 
### to outfile. Otherwise, print it to standard output.

if __name__ == '__main__' :
