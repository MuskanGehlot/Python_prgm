class graph:
    def __init__(self,totalNodes):
        self.adlist = dict()
        self.totalNodes=totalNodes 
        for i in range(totalNodes):
            self.adlist[i]=[]

    def addUndirectedEdge(self,v1,v2):
        if (v2 in g.adlist[v1]): 
            print ("Edge already exists ")
        else:
            g.adlist[v1].append(v2)
            g.adlist[v2].append(v1)

    def addDirectedEdge(self,v1,v2):
        if (v2 in g.adlist[v1]): 
            print ("Edge already exists ")
        else:
            g.adlist[v1].append(v2)

    def removeDirectedEdge(self,v1,v2):
        g.adlist[v1].remove(v2)

    def removeUndirectedEdge(self,v1,v2):
        g.adlist[v1].remove(v2)    
        g.adlist[v2].remove(v1)     
                    
n=int(input("total no of nodes"))
g=graph(n)    
y=int(input("press 1 if u want the directed mode and 2 if undirected"))
x=int(input("enter total no of edges"))
for i in range(x):
    a=int(input("enter vertex one"))
    b=int(input("enter vertex two"))
    if y is 1:
        g.addDirectedEdge(a,b)
    elif y is 2:
        g.addUndirectedEdge(a,b)
    else:
        print("choose from 1 and 2")    
print(g.adlist)
p=int(input("vetrex one of edge to be deletd"))
q=int(input("vetrex two of edge"))
if y is 1:
    g.removeDirectedEdge(p,q)
elif y is 2:
    g.removeUndirectedEdge(p,q)