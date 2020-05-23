import random
import matplotlib.pyplot as plt
import time

"""
Please call allSimulation() to test the code.
--> allSimulation() is the main function which calls three simulation(p) for values of p 0.6, 0.75 and 0.9
    to plot first two figures and call another simulation(p) for value of p 0.8 for third Figure. 
    This function also plots all graphs in one show. 
--> simulation(p) is the main simulation function which starts with a Global Graph and calls birthProcess()
    and deathProcess() for time defined in for loop.
--> birthProcess() is the main function for birth process at a given stage.
--> deathProcess() is the main function for death process at a given stage. 
--> numberOfNodes() is the function to calculate number of nodes at a given stage. This function is used 
    in all above function calls. 
--> numberOfEdges() is the function to calculate number of edges at a given stage. This function is used
    in all above function calls. 
--> degreeOfNode(x) is a function to calculate degree of node x. This function is also used in some of the
    obove functions.
"""

Graph = [[1], [0,4, 5,7], [3, 4], [2], [1, 2], [1],[-1], [1],[-1]] #Starting with this Global Graph

def allSimulation():
    t = [400,800,1200,1600,2000]
    global Graph
    n1,e1 = simulation(0.6)
    print("Simulation 1 Done")
    Graph = [[1], [0,4, 5,7], [3, 4], [2], [1, 2], [1],[-1], [1],[-1]]
    n2,e2 = simulation(0.75)
    print("Simulation 2 Done")
    Graph = [[1], [0,4, 5,7], [3, 4], [2], [1, 2], [1],[-1], [1],[-1]]
    n3,e3 = simulation(0.9)
    print("Simulation 3 Done")
    Graph = [[1], [0,4, 5,7], [3, 4], [2], [1, 2], [1],[-1], [1],[-1]]
    n3,e3 = simulation(0.8)
    print("Simulation 4 Done")
    k = [x for x in range(0,101)]
    out=[]
    for x in k:
        s =0
        for y in Graph:
            if degreeOfNode(y) == x:
                s=s+1 
        out.append(s/numberOfNodes())
    pk = []
    for i in range(0,len(out)):
        pk.append(sum(out[i:]))
    plt.subplot(221)
    plt.plot(t,n1, label='p=0.6')
    plt.plot(t,n2, label='p=0.75')
    plt.plot(t,n3, label='p=0.9')
    plt.xlabel('Time')
    plt.ylabel('E[nt]')
    plt.legend()
    plt.subplot(222)
    plt.plot(t,e1, label='p=0.6')
    plt.plot(t,e2, label='p=0.75')
    plt.plot(t,e3, label='p=0.9')
    plt.xlabel('Time')
    plt.ylabel('E[mt]')
    plt.legend()
    plt.subplot(223)
    plt.loglog(k,pk, label='Degree Distribution')
    plt.xlabel('k')
    plt.ylabel('pk')
    plt.legend()
    plt.savefig('imagex')
    plt.show()

def simulation(p):
    #start_time = time.time()
    n_nodes =[]
    n_edges =[]
    for i in range(1,2001):
        rd = random.uniform(0,1)
        if rd <= p:
            #print('birth')
            birthProcess()
        else:
            #print('death')
            deathProcess()
        if i in (400,800,1200,1600,2000):
            n_nodes.append(numberOfNodes())
            n_edges.append(numberOfEdges())
    return n_nodes,n_edges    
    """ print(Graph)
    print(numberOfEdges())
    print(numberOfNodes())
    print(n_nodes)
    print(n_edges)
    print(time.time()-start_time) """

def birthProcess():
    global Graph
    p_graph = [0]*len(Graph)
    p_graph = [degreeOfNode(x) for x in Graph]
    #print(p_graph)
    s=0
    for i in range(0,len(p_graph)):
        p_graph[i] = s+p_graph[i] 
        s = p_graph[i]
    #print(p_graph)
    prob = random.randint(1,2*numberOfEdges())
    #print(prob)
    a=0
    cor_node = None
    for i in range(0,len(p_graph)):
        if prob >a and prob <=p_graph[i]:
            cor_node = i
            break
        a = p_graph[i]
    #print(cor_node)
    Graph[cor_node].append(len(Graph))
    Graph.append([cor_node])
    #print(Graph)

def deathProcess():
    global Graph
    p_graph = [0]*len(Graph)
    p_graph = [(numberOfNodes() - degreeOfNode(x)) if len(x) != 0 else 0 for x in Graph]
    #print(p_graph)
    s=0
    for i in range(0,len(p_graph)):
        p_graph[i] = s+p_graph[i]
        s = p_graph[i]
    #print(p_graph)
    prob = random.randint(1,numberOfNodes()**2 - 2*numberOfEdges())
    #print(prob)
    a=0
    cor_node = None
    for i in range(0,len(p_graph)):
        if prob >a and prob <=p_graph[i]:
            cor_node = i
            break
        a = p_graph[i]
    #print(cor_node)
    if Graph[cor_node] == [-1]:
        Graph[cor_node] = []
    else:
        for x in Graph[cor_node]:
            if degreeOfNode(Graph[x]) == 1:
                Graph[x] = [-1]
            else:
                Graph[x].remove(cor_node)
        Graph[cor_node] =[]
    #print(Graph)

def numberOfEdges():
    global Graph
    n_edges = 0
    for i in range(0,len(Graph)):
        if Graph[i] == [-1]:
            continue
        else:
            n_edges = n_edges + len(Graph[i])
    return int(n_edges/2)

def numberOfNodes():
    nodes = 0
    global Graph
    for i in range(0,len(Graph)):
        if len(Graph[i]) != 0:
            nodes = nodes+1
    return nodes

def degreeOfNode(x):
    if x == [-1]:
        return 0
    else:
        return len(x)

"""
I have also coded directed functions for all three figures and plotted them to compare graphs from simulation. 
Please call plot() function to run this part.
--> firstGraph() is the function to calculate E(n). Expected number of nodes value through farmula given 
    in the paper i.e. without any simulation.
--> secondGraph() is the function to calculate E(m). Expected number of edges value through farmula given 
    in the paper i.e. without any simulation.
--> thirdGraph() is the function to calculate log of degree distribution value through farmula given 
    in the paper i.e. without any simulation.
--> plot() is the main function to plot all three graphs. It calls firstGraph(), secondGraph() and 
    thirdGraph()
"""

def firstGraph():
    p1,p2,p3 = 0.6,0.75,0.9
    q1,q2,q3=1-p1, 1-p2,1-p3
    t = [10000,20000,30000,40000,50000]
    En1,En2,En3 = [0]* len(t),[0]* len(t), [0]* len(t)
    for i in range(0,len(t)):
        En1[i] = (p1-q1)*t[i] + 2*q1
        En2[i] = (p2-q2)*t[i] + 2*q2
        En3[i] = (p3-q3)*t[i] + 2*q3
    return En1,En2,En3

def secondGraph():
    p1,p2,p3 = 0.6,0.75,0.9
    q1,q2,q3=1-p1, 1-p2,1-p3
    t = [10000,20000,30000,40000,50000]
    En1,En2,En3 = [0]* len(t),[0]* len(t), [0]* len(t)
    for i in range(0,len(t)):
        En1[i] = p1*(p1-q1)*t[i]
        En2[i] = p2*(p2-q2)*t[i]
        En3[i] = p3*(p3-q3)*t[i]
    return En1, En2, En3

def thirdGraph():
    p = 0.8
    temp = (-1-1*((2*p)/(2*p-1)))
    k = [x for x in range(1,101)]
    answ = [0]*len(k)
    for i in range(0,len(k)):
        answ[i] = k[i]**temp
    sumx = 0
    sums = []
    for x in range(0, len(k)):
        sumx = sum(answ[x:])
        sums.append(sumx)
    return sums,k
    
def plot():
    a,b,c = firstGraph()
    d,e,f =secondGraph()
    g,h =thirdGraph()
    t = [10000,20000,30000,40000,50000]
    plt.figure(figsize=(8,6))
    plt.subplot(2, 2, 1)
    plt.plot(t,a, label='p=0.6')
    plt.plot(t,b, label='p=0.75')
    plt.plot(t,c, label='p=0.9')
    plt.title('Figure 2')
    plt.subplot(2, 2, 2)
    plt.plot(t,d, label='p=0.6')
    plt.plot(t,e, label='p=0.75')
    plt.plot(t,f, label='p=0.9')
    plt.title('Figure 3')
    plt.subplot(2, 2, 3)
    plt.loglog(h, g)
    plt.title('Figure 5')
    plt.show()

#print(birthProcess())
#print(deathProcess())
#print(simulation(0.6))
#print(numberOfEdges())
#print(numberOfNodes())
#plot()

allSimulation()
plot()