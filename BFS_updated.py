
# coding: utf-8

# In[8]:

## Queue initialization:

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


## intializing the mazee

import numpy
def maze(dim1,dim2,prob):
    maz = [[numpy.random.choice(numpy.arange(0, 2), p=[1-prob,prob]) for i in range(dim1)] for j in range(dim2)]
    maz[0][0]=0
    maz[dim1-1][dim2-1]=2
    return maz
mazee=maze(4,4,0.1)
print mazee

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
                mazee[x1][y1] = 3;  ## Markint as visited node
                print "Visited Node %d %d" %(x1,y1)
            elif (mazee[x1][y1]==2):
                print "Destination reached"
           
                

                
## Calling BFS to explore all nodes
BFS(q)


# In[6]:

mazee[2][1]


# In[ ]:



