
# coding: utf-8

# In[20]:

## Code for Stack
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


# In[21]:

s = Stack()


# In[25]:

s.push(1)
s.push(12)
s.size()
x=s.peek();
print x
y = s.peek1();
print y


# In[11]:

1


# In[14]:

mazee[3][2]


# In[30]:

## Initializing the maze
import numpy
def maze(dim1,dim2,prob):
    maz = [[numpy.random.choice(numpy.arange(0, 2), p=[1-prob,prob]) for i in range(dim1)] for j in range(dim2)]
    maz[0][0]=0
    maz[dim1-1][dim2-1]=2
    return maz
mazee=maze(4,4,0.1)
print mazee


# In[31]:

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
        elif(mazee[x1][y1] ==3 or mazee[x1][y1] ==2):
            print "Node already visited at %d %d" %(x1,y1)
            j = j+1;
        elif(mazee[x1][y1] ==0):
            mazee[x1][y1] = 3;  ## Mark it as visited node
            print "Visited Node %d %d" %(x1,y1)
            s.push(y1);
            s.push(x1);
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



# In[ ]:



