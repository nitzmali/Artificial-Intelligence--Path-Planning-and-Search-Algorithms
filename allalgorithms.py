
# coding: utf-8

# In[59]:

## Queue initialization:
import time 
start=time.time()
class Queue:
    def __init__(self):
        self.items=[]
        
    def isempty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)
        
    def dequeue(self):
        return self.items.pop()
       
            
    def size(self):
        return len(self.items)
        
q = Queue()

dim1=50
dim2=50

## intializing the mazee

import numpy
## writing the code to generate maze with the required probability
def maze(dim1,dim2,prob):
    maz = [[numpy.random.choice(numpy.arange(0, 2), p=[1-prob,prob]) for i in range(dim1)] for j in range(dim2)]
    maz[0][0]=0
    maz[dim1-1][dim2-1]=2
    return maz
mazee=maze(dim1,dim2,0.2)
mazet=mazee
print mazee

## creating an edge varible to store the parent values
## this will help to find the optimum path 
edge = [[(dim1*dim2,dim1*dim2) for i in range(dim1)] for j in range(dim2)]

print edge

## creating  0,0 as the start point
q.enqueue(0);
q.enqueue(0);
mazee[0][0] = 3;
## Code for BFS:
def BFS(q):
    ## checking if the queue is empty
    print q.size()
    while (q.size() != 0):
        x = q.dequeue();
        y = q.dequeue();
        # exploring all near by nodes:
        k = [] ##list to store all nearby by nodes.
        if x < (len(mazee)-1):
            k.append(x+1)
            k.append(y)
        if x >0:
            k.append(x-1)
            k.append(y)
        if y<(len(mazee)- 1):
            k.append(x)
            k.append(y+1)
        if y >0:
            k.append(x)
            k.append(y-1)
        print k

        i = 0
        while (i <len(k)):
            x1 = k[i];
            y1 = k[i+1];
            i = i+2;
            if(mazee[x1][y1] ==1):
                print "Wall at %d %d " %(x1,y1)
            elif(mazee[x1][y1] ==3):
                print "Node already visited at %d %d" %(x1,y1)
            elif(mazee[x1][y1] ==0):
                q.enqueue(x1)
                q.enqueue(y1)
                mazee[x1][y1] = 3;  ## Mark it as visited node
                print "Visited Node %d %d" %(x1,y1)
                edge[x1][y1] = (x,y)
            elif (mazee[x1][y1]==2):
                print "Destination reached"
                edge[x1][y1] = (x,y)
                mazee[x1][y1] =3;
           
                

                
## Calling BFS to explore all nodes
BFS(q)
end=time.time()
print end-start
print "seconds"
## setting the goal node location after the path is explored
g1 = dim1-1
g2 = dim2-1
print edge
path=[]
## using the  edge matrix data to find the parents and store in the list
## this tells the path traversed
while (edge[g1][g2]!= (0,0)):
    if(edge[g1][g2] == (dim1*dim2,dim1*dim2)):
        print "The algorithm could not search the path, Failure!"
        break
    z = edge[g1][g2]
    path.append(z)
    g1 = z[0]
    g2 = z[1]

    
    
## printing the path
print "The path used by BFS is:"
for item in path:
    print item    




    

stack


# coding: utf-8

# In[15]:

## Code for Stack 
## Stack is needed to implement DFS

dim1=10
dim2=10
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]
    
     def peek1(self):
        return self.items[len(self.items) -2]

     def size(self):
         return len(self.items)

s = Stack()
## object creation

## Initializing the maze
import numpy
def maze(dim1,dim2,prob):
    maz = [[numpy.random.choice(numpy.arange(0, 2), p=[1-prob,prob]) for i in range(dim1)] for j in range(dim2)]
    maz[0][0]=0
    ##maz[dim1-1][dim2-1]=2
    return maz
mazee=maze(dim1,dim2,0.2)
print mazee
## creating an edge varible to store the parent values
## this will help to find the optimum path 
edge = [[(dim1*dim2,dim1*dim2) for i in range(dim1)] for j in range(dim2)]

## Writing code for DFS
## entering the starting point
s.push(0);
s.push(0);

while(s.size() !=0):
## Discovering nearby nodes:
    x = s.peek();
    y = s.peek1();
    k=[]
    if x < (len(mazee)-1):
        k.append(x+1)
        k.append(y)
    if x >0:
        k.append(x-1)
        k.append(y)
    if y<(len(mazee)- 1):
        k.append(x)
        k.append(y+1)
    if y >0:
        k.append(x)
        k.append(y-1)
    print k

## Examining All near by nodes:
    i = 0;
    j = 0;
    length = len(k)
    print length
    while (i <len(k)):
        x1 = k[i];
        y1 = k[i+1];
        i = i+2;
        if(mazee[x1][y1] ==1):
            print "Wall at %d %d " %(x1,y1)
            j = j+1;
        elif(mazee[x1][y1] ==3):
            print "Node already visited at %d %d" %(x1,y1)
            j = j+1;
        elif(mazee[x1][y1] ==0):
            mazee[x1][y1] = 3;  ## Mark it as visited node
            print "Visited Node %d %d" %(x1,y1)
            s.push(y1);
            s.push(x1);
            edge[x1][y1] = (x,y)
            break 
        ##elif (mazee[x1][y1]==2):
            ##print "Destination reached"
    print j
    if j == (length/2):
    ## All nodes are unvisitable 
    ## we neeed to pop current node (x and y) from stack
        s.pop()
        s.pop()
        print "entry popped out of stack"

## setting the goal node location after the path is explored
g1 = 9
g2 = 9
path=[]
## using the  edge matrix data to find the parents and store in the list
## this tells the path traversed
while (edge[g1][g2]!= (0,0)):
    if(edge[g1][g2] == (dim1*dim2,dim1*dim2)):
        print "The algorithm could not search the path, Failure!"
        break
    z = edge[g1][g2]
    path.append(z)
    g1 = z[0]
    g2 = z[1]

    
    
## printing the path
print "The path used by DFS is:"
for item in path[::-1]:
    print item    



###A*

##A* 

##A* 
import time
import numpy as np
import heapq
import math
start=time.time()
dim1=200
dim2=200
prob=0.1
##define matrix
'''def maze():
    a= [[0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 2]] 
    
    return a ''' 
def maze(dim1,dim2,prob):
    maz = [[np.random.choice(np.arange(0, 2), p=[1-prob,prob]) for i in range(dim1)] for j in range(dim2)]
    maz[0][0]=0
    maz[dim1-1][dim2-1]=2
    return maz
##define heuristic for euclidean distance
def heuristic():
    x2=dim1-1
    y2=dim2-1
    n=dim1*2
    x=0
    while (x<dim1):
        y=0
        while(y<dim2):
            mazee1[x][y]= int(math.sqrt(((x-x2)*(x-x2))+((y-y2)*(y-y2))))
            n=n-1
            y=y+1
        x=x+1
        n=n+(n/2)
    return mazee1 

##define heuristic for manhatan distance
'''def heuristic():
    x2=9
    y2=9
    n=20
    x=0
    while (x<10):
        y=0
        while(y<10):
            mazee1[x][y]= int(math.fabs(x-x2))+int(math.fabs(y-y2))
            n=n-1
            y=y+1
        x=x+1
        n=n+10
    return mazee1 '''

##call matrix to create
print "below is the maze"
mazee=maze(dim1,dim2,prob)
print np.matrix(mazee)
print "\n"

##call matrix to create heuristic
print  "below is the heuristic"
mazee1=maze(dim1,dim2,0)
heumat=heuristic()
print np.matrix(heumat)
 ## matrix to store heuristics
print "\n"


##create list open and closed
openlist=[]

heapq.heapify(openlist)
goal_queue = []

heapq.heapify(goal_queue)
heapq.heappush(openlist,(heumat[0][0],0,0))
#print openlist

mazee[0][0]=3 ## start node as visited
def a_star(q):
    while(len(q)!=0):
        print q
        q1 = heapq.heappop(q)
        if(q1[-2] ==9 and q1[-1] ==9):
            heapq.heappush(goal_queue, q1)
            
            
            ## doing this because we do not want to pop goal node data out
        
        
        y = q1[-1];
        x = q1[-2];
        print x,y
        k=[]
        if x<len(mazee)-1:
            k.append(x+1)
            k.append(y)
            
        if x>0:
            k.append(x-1)
            k.append(y)
        if y<len(mazee)-1:
            k.append(x)
            k.append(y+1)
        
        if y>0:
            k.append(x)
            k.append(y-1)
        i=0
        print k
        while(i<len(k)):
            x1=k[i]
            y1=k[i+1]
            #print mazee[x1][y1]
            i=i+2
            
            if mazee[x1][y1]==1:
                print "Wall reached at [%d][%d] "%(x1,y1)
            elif mazee[x1][y1]==3:
                print "Node already visited at [%d][%d] "%(x1,y1)
            elif mazee[x1][y1]==0:
                
                q2 = []
                q2 = tuple(q2);
                q2 = q1 + (x1,y1)
                ## updating the cost function
                m = len(q2);
                cost1 = ((m-1)-2)/2
                cost = cost1 + heumat[x1][y1];
                q2 = list(q2);
                q2[0] = cost;
                q2 = tuple(q2);
                heapq.heappush(q,q2)
                ## heapq.heappush(q,(heumat[x1][y1],x1,y1))
                #print "itmes pushed %d",%q
                
                mazee[x1][y1]=3
                print "Visited node at [%d][%d] "%(x1,y1)
            elif mazee[x1][y1]==2:
                
                q2 = []
                q2 = tuple(q2);
                q2 = q1 + (x1,y1)
                ## updating the cost function
                m = len(q2);
                cost1 = ((m-1)-2)/2
                cost = cost1 + heumat[x1][y1];
                q2 = list(q2);
                q2[0] = cost;
                q2 = tuple(q2);
                heapq.heappush(q,q2)
                ## heapq.heappush(q,(heumat[x1][y1],x1,y1))
                #print "itmes pushed %d",%q
                print "destination reached at [%d][%d] "%(x1,y1)
                
                print k
        n1 = len(q)
        count = 0
        for p in range(0,n1):
            if q[p][-1] == 9 and q[p][-2] ==9:
                count = count+1;
            p = p+1;
    



a_star(openlist)
end=time.time()
print end-start
print "seconds"

l1 = len(goal_queue)

if l1!=0:
    z =heapq.heappop(goal_queue)
    
    z=list(z)
    del z[0]
    print "best path is: " 
    print z
else:
    
    print "No possible way to reach"
if l1!=0:
    path= []
    i =0
    while (i !=(len(z)-2)):
        path.append((z[i], z[i+1]))
        i = i+2
    path.append((9,9))
print path

##turtle


import turtle
turtle.speed(0)
n=10
dimen=n
walls=[]
k=[]
def drawGrid():
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.forward(n*n)
    turtle.right(90)
    turtle.forward(n*n)
    turtle.right(90)
    turtle.forward(n*n)
    turtle.right(90)
    turtle.forward(n*n)

def drawColumns():
    for i in range(n/2):
        
        #turtle.begin_fill()
        turtle.right(90)
        turtle.forward(n)
        turtle.right(90)
        turtle.forward(n*n)
        turtle.left(90)
        turtle.forward(n)
        turtle.left(90)
        turtle.forward(n*n)
        #turtle.end_fill()
     

def drawRows():
    turtle.left(180)
    rows = 0 
    while rows <= (n/2)-1:
        rows += 1
        turtle.forward(n)
        turtle.right(90)
        turtle.forward(n*n)
        turtle.left(90)
        turtle.forward(n)
        turtle.left(90)
        turtle.forward(n*n)
        turtle.right(90)

def getwalls():
    i=0
    j=0
    for i in range(n):
        for j in range(n):
        
            k.append((i,j,mazee[i][j]))
                
    for i in range(n*n):
        x,y,z=k[i]
        if z==1:
            walls.append((x,y))

print len(k)

        
def drawwalls():
    #leng=[(0,2),(2,4),(3,3),(9,9)]
    #l.append((-300+0,250+0))
    #l.append((-300+(50*0),250-(50*2)))
    #l.append((-300+(50*1),250-(50*2)))
    #l.append((-300+(50*1),250-(50*4)))
    #l.append((-300+(50*7),250-(50*7)))
    for i in range(len(walls)):   
        x,y=walls[i]
        print x,y
        turtle.penup()
        turtle.goto(10*x,-10*y)
        turtle.pendown()
        turtle.color("black")
        turtle.begin_fill()
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.end_fill()    
def drawpath():
    
    for i in range(len(path)):   
        x,y=path[i]
        print x,y
        turtle.penup()
        turtle.goto(10*x,-10*y)
        turtle.pendown()
        turtle.color("red")
        turtle.begin_fill()
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.end_fill()  
    
    
def main():
    drawGrid()
    drawColumns()
    drawRows()
    getwalls()
    drawwalls()
    drawpath()
    #print item

    turtle.penup()
    turtle.goto(0,0)
if __name__ == "__main__":
    main()
    


##Minsweeper generator
def mazegen():
    mazee=[[0, 1, 2, 2],
         [0, 1,10, 10],
         [1, 3, 4, 3],
         [1, 10,10, 1]]
    return mazee
## Discovering nearby nodes:
def neighbour(x,y):
    k=[]
    if x < (len(mazee)-1):
            k.append((x+1,y))
            while(x!=len(mazee)-1):
                k.append((x+1,y+1))
                break
        
    if x >0:
            k.append((x-1,y))
            while(x!=0):
                k.append((x-1,y-1))
                break
            
    if y<(len(mazee)- 1):
            k.append((x,y+1))
            while(x!=0):
                k.append((x-1,y+1))
                break
    if y >0:
            k.append((x,y-1))
            while(x!=len(mazee)-1):
                k.append((x+1,y-1))
                break
    return k
def iden0(k):
    i=0
    while(i<len(k)):## k consisit of co-ordinates neighbours
        t,p=k[i]
        val=(mazee[t][p])  ##value of the matrix
        
        dict2={(t,p):val}##value of cells and co-ordinates
        dict1.update(dict2)
        i=i+1
        return dict1
    

##main function
if __name__=='__main__':
    safe=[]
    dict1={}
    dict2={}
    lval0=[]
    mazee=mazegen()
    print("these are the co-ordinates which you need to enter the value")
    x=int(input("enter the x Value"))
    y=int(input("enter the y Value"))

    safe.append([(x,y)])
    k=neighbour(x,y)     ##call neighbour nodes
    dict1=iden0(k)
    for key,value in dict1.items():
        if value==0:
            lval0.append((key))
            x1,y1=key
            k=neighbour(x1,y1)
            dict3=iden0(k)
    for e in lval0:
        del dict1[e]
    print (dict1)
    
    