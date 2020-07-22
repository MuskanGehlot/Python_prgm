class graph:
    def __init__(self,totalNodes):
        self.ajmtrx = [[0 for x in range(totalNodes)] for y in range(totalNodes)]
        self.totalNode=totalNodes       

    def add_DirectedEdge(self,V1,V2):
        self.ajmtrx[V1][V2]=1
        self.ajmtrx[V2][V1]=1

    def DirectedEdgeRemove(self,V1,V2):
        self.ajmtrx[V1][V2]=0
        self.ajmtrx[V2][V1]=0

    def add_UndirectedEdge(self,V1,V2):
        self.ajmtrx[V1][V2]=1

    def UndirectedEdgeRemove(self,V1,V2):
        self.ajmtrx[V1][V2]=0


n=int(input("total no of nodes"))
g=graph(n)
y=int(input("press 1 if u want the directed mode and 2 if undirected"))
x=int(input("enter total no of edges"))
for i in range(x):
    a=int(input("enter vertex one"))
    b=int(input("enter vertex two"))
    if y is 1:
        g.add_DirectedEdge(a,b)
    elif y is 2:
        g.add_UndirectedEdge(a,b)
    else:
        print(choose from 1 and 2)    
print(g.ajmtrx)
p=int(input("vetrex one of edge to be deletd"))
q=int(input("vetrex two of edge"))
if y is 1:
    g.DirectedEdgeRemove(p,q)
elif y is 2:
    g.UndirectedEdgeRemove(p,q)
print(g.adlist)    
