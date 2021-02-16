#!/usr/bin/env python
# coding: utf-8

#todo 
#     Strategy 2:  BFS 
#     Strategy 3:  
#     Make loops for BFS / DFS 
#     Test highest dim for BFS / DFS at p = .3
#     Plot for DFS / BFS avg success


import numpy as np
import pandas as pd
import random
from collections import deque
from copy import copy, deepcopy
from queue import PriorityQueue
from dataclasses import dataclass, field
import matplotlib.pyplot as plt

# queue node used in BFS
class Node:
    # (x, y) represents coordinates of a cell in matrix
    # maintain a parent node for printing path
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
 
    def __repr__(self):
        return str((self.x, self.y))
class ENode:
    # (x, y) represents coordinates of a cell in matrix
    # maintain a parent node for printing path
    def __init__(self, x, y, parent,distance,priority):
        self.x = x
        self.y = y
        self.parent = parent
        self.distance = distance
        self.priority = priority
    def __lt__(self, other):
        return self.priority < other.priority
    def __repr__(self):
        return str((self.x, self.y))



row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]
q = .2

def createMatrix(Dim, p):
    Matrix = [ [ 0 for i in range(Dim) ] for j in range(Dim) ]

    for i in range(Dim):
        for j in range(Dim):
            Matrix[i][j] = '0'
    for i in range(Dim):
        for j in range(Dim):
            if ((i != 0) | (j != 0)) and ((i != (Dim-1)) | (j != (Dim-1))):
                if random.random() < p:
                    Matrix[i][j]= '_'
                    
    Matrix[0][0] = 'S'
    Matrix[Dim-1][Dim-1] = 'G'
        
    return np.array(Matrix)

def printMatrix(Matrix):
    print('0 = unexpored')
    print('_ = Barrier')
    print('! = Fire')
    print('1 = Explored')
   
    #print(Matrix)
    

'''
testMatrix = createMatrix(3500, .30)
#dfsTestMatrix = deepcopy(testMatrix)
#astar_testMatrix = deepcopy(testMatrix)

bfsPathMatrix = deepcopy(testMatrix)

dfsPathMatrix = deepcopy(testMatrix)
astarPathMatrix = deepcopy(testMatrix)
strat1Matrix = deepcopy(testMatrix)
strat2Matrix = deepcopy(testMatrix)
'''
#printMatrix(testMatrix)

bfs_nodes_explored = []
a_star_avg = []







def onFire(x,y,grid):
    k = 0
    for i in range(4):
        xp = x  + row[i]
        yp = y  + col[i]
        if (0 <= xp < len(grid)) and (0<= yp < len(grid)):
            if grid[xp][yp] == '!':
                k = k + 1
    return k

def advance_fire(curr_matrix,q):
    N = len(curr_matrix)
    new_grid = deepcopy(curr_matrix)
    for i in range(len(curr_matrix)):
        for j in range(len(curr_matrix[0])):
            if (curr_matrix[i][j] != '!' and curr_matrix[i][j] != '_'):
                k = onFire(i,j,curr_matrix) 
                prob = 1 - pow((1-q),k)
                if random.random() <= prob:
                    new_grid[i][j] = '!'
                    

    new_grid[0][0] = 'S'
    new_grid[N-1][N-1] = 'G'
    return new_grid

def strategy1(path, matrix):
    
    for curr in path:
        x = curr[0]
        y = curr[1]
        if matrix[x][y] == '!':
            print("Path Failed, Maze burned")
            return matrix
        else:
            matrix[x][y] = 'X'
            matrix = advance_fire(matrix)
        counter = counter + 1
    
    print("Successfully exited the maze")
    
    return matrix


def strat1_graph(path, matrix,q):
    for curr in path:
        x = curr[0]
        y = curr[1]
        if matrix[x][y] == '!':
            #print("Path Failed, Maze burned")
            return False
        else:
            matrix[x][y] = 'X'
            matrix = advance_fire(matrix,q)
        #counter = counter + 1
    
    #print("Successfully exited the maze")
    
    return True

def strat2_graph(path, matrix,q):
    total_path = set()
    ordered_path = []
    iterator_index = 0
    while (len(path) > 0):
        curr = path[0]
        x = curr[0]
        y = curr[1]
        matrix[x][y] = 'X'
        total_path.add((y,x))
        ordered_path.append((y,x))
        coord2x = path[len(path)-1][0]
        coord2y = path[len(path)-1][1]
        coord2 = (coord2x,coord2y)
        nodeTemp = BFS(curr,coord2,matrix)
        path = getPathArray(nodeTemp)
        if len(path) == 0:
            '''
            print("Paths failed, Maze Burned")
            print("Attempted Path: ")
            for i in ordered_path:
                print(i, end = ' ')
            print("")
            '''
            return False
        else:
            #remove first element in path array 
            
            path = path[1:]
            matrix = advance_fire(matrix,q)
           
    '''
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] =='!' and (i,j) in total_path:
                matrix[i][j] = 'B'
    print("Successfully exited maze: ")
    print("Path Taken: ")
    for i in ordered_path:
        print(i, end = ' ')

    print("")
    '''
    return True

def strategy2(path,matrix):
    
    '''
    while (iterator_index < len(path))

    Take off first coord from path_arr
    recompute shortest path
    (path = getPathArray(nodeTemp))
    if path does not exist, then return false
    else advance to next element in path array:
        iterator_index++

    add path[iterator_index] to total_path

    advance_fire


    '''
    total_path = set()
    ordered_path = []
    iterator_index = 0
    while (len(path) > 0):
        curr = path[0]
        x = curr[0]
        y = curr[1]
        matrix[x][y] = 'X'
        total_path.add((y,x))
        ordered_path.append((y,x))
        coord2x = path[len(path)-1][0]
        coord2y = path[len(path)-1][1]
        coord2 = (coord2x,coord2y)
        nodeTemp = BFS(curr,coord2,matrix)
        path = getPathArray(nodeTemp)
        if len(path) == 0:
            print("Paths failed, Maze Burned")
            print("Attempted Path: ")
            for i in ordered_path:
                print(i, end = ' ')
            print("")
            return matrix
        else:
            #remove first element in path array 
            
            path = path[1:]
            matrix = advance_fire(matrix)
           

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] =='!' and (i,j) in total_path:
                matrix[i][j] = 'B'
    print("Successfully exited maze: ")
    print("Path Taken: ")
    for i in ordered_path:
        print(i, end = ' ')

    print("")
    return matrix

def buildFireMap(matrix):
    fireMap = [ [ 0 for i in range(len(matrix)) ] for j in range(len(matrix)) ]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (matrix[i][j] != '!' and matrix[i][j] != '_'):
                k = onFire(i,j,matrix)
                sample = []
                for x in range(10):
                    prob = 1 - pow((1-q),k)
                    sample.append(prob)
                avg = float(sum(sample) / float(len(sample)))
                fireMap[i][j] = avg
            elif matrix[i][j] == '_':
                fireMap[i][j] = 0
            elif matrix[i][j] == '!':
                fireMap[i][j] = 1

    return np.array(fireMap)


def getPathArray(node):
    stack = []
    while node:
        stack.append((node.x,node.y))
        node = node.parent

    prime_path = []
    while stack:
        prime_path.append(stack.pop())

    return prime_path
    




dfsPath = []
def DFSsearch(Coord1, Coord2, Matrix):
    stack = []
    start = Node(Coord1[0],Coord1[1],None)
    if (Matrix[Coord2[0]][Coord2[1]] == '!') or (Matrix[Coord1[0]][Coord1[1]] == '!') or (Matrix[Coord1[0]][Coord1[1]] == '_') or (Matrix[Coord1[0]][Coord1[1]] == '_'):
        return False
 
    
    stack.append(start)
    
    while stack:
        
        curr = stack.pop()

        xPos = int(curr.x)
        yPos = int(curr.y)
       
        #Update Maze for Fire

        # 1. Visited 
        # 2. Barrier
            #Compare the value  in the given matrix location
        # 3. Boundries
            #Compare the x and y boundries
        if ( xPos < 0  or xPos >= len(Matrix) or yPos < 0 or yPos >= len(Matrix[0])  or ((Matrix[curr.x][curr.y]) == '1') or ((Matrix[curr.x][curr.y]) == '_')):
            continue

        #Also update fire??
        Matrix[xPos][yPos] = '1'
        
        if (Matrix[Coord2[0]][Coord2[1]] == '!'):
            return None
    
    
        if (xPos == Coord2[0] and yPos == Coord2[1]):
            return curr
        
        #print(str(xPos) + "\t" + str(yPos))
            
        
        #Check up
        #Check Down 
        #Check Right 
        #Check Left
       
        for i in range(4):
            x = xPos + row[i]
            y = yPos + col[i]
            next = Node(x,y,curr)
            stack.append(next)

        '''
        stack.append((xPos + 1,yPos))
        stack.append((xPos -1, yPos))
        stack.append((xPos, yPos + 1))
        stack.append((xPos, yPos - 1))
        '''
    return None

def BFS(Coord1, Coord2, Matrix):
    q = deque()
    visited = set()
    
    if (Matrix[Coord2[0]][Coord2[1]] == '!') or (Matrix[Coord1[0]][Coord1[1]] == '!') or (Matrix[Coord1[0]][Coord1[1]] == '_') or (Matrix[Coord2[0]][Coord2[1]] == '_'):
        return None
 
    start = Node(Coord1[0],Coord1[1], None)
    q.append(start)
    counter = 0
    while q:
        
        curr = q.popleft()
      
        xPos = int(curr.x)
        yPos = int(curr.y)
       
        #Update Maze for Fire

        # 1. Visited 
        # 2. Barrier
            #Compare the value  in the given matrix location
        # 3. Boundries
            #Compare the x and y boundries
        
        if ( xPos < 0  or xPos >= len(Matrix) or yPos < 0 or yPos >= len(Matrix[0])  or ((curr.x,curr.y) in visited) or ((Matrix[curr.x][curr.y]) == '_') or Matrix[curr.x][curr.y] == '!' ):
            continue
        
        counter = counter  + 1

        if (xPos == Coord2[0] and yPos == Coord2[1]):
            bfs_nodes_explored.append(counter)
            return curr
        
        visited.add((curr.x,curr.y))
        
        
        
    
    
        #print(str(xPos) + "\t" + str(yPos))
            
        
        #Check up
        #Check Down 
        #Check Right 
        #Check Left
       
        for i in range(4):
            x = xPos + row[i]
            y = yPos + col[i]
            next = Node(x,y,curr)
            if next not in q:
                q.append(next)

        '''
        queue.append((xPos + 1,yPos))
        queue.append((xPos -1, yPos))
        queue.append((xPos, yPos + 1))
        queue.append((xPos, yPos - 1))
        '''
    bfs_nodes_explored.append(counter)
    return None
    
def heuristic(pointA, pointB):
    point1 = np.array(pointA) 
    point2 = np.array(pointB) 
  
    # calculating Euclidean distance 
    # using linalg.norm() 
    hue = np.linalg.norm(point1 - point2)
    return hue

def a_star(Coord1, Coord2, Matrix):

    pq = PriorityQueue()
    start = ENode(Coord1[0],Coord1[1],None,0,0)
    counter = 0
    if (Matrix[Coord2[0]][Coord2[1]] == '!') or (Matrix[Coord1[0]][Coord1[1]] == '!') or (Matrix[Coord1[0]][Coord1[1]] == '_') or (Matrix[Coord1[0]][Coord1[1]] == '_'):
        return None

    pq.put(start)

    while not pq.empty():
        curr = pq.get()
       
        xPos = (curr.x)
        yPos = (curr.y)
       
        #Update Maze for Fire

        # 1. Visited 
        # 2. Barrier
            #Compare the value  in the given matrix location
        # 3. Boundries
            #Compare the x and y boundries
        if ( xPos < 0  or xPos >= len(Matrix) or yPos < 0 or yPos >= len(Matrix[0])  or ((Matrix[curr.x][curr.y]) == '1') or ((Matrix[curr.x][curr.y]) == '_')):
            continue
        counter = counter + 1
        if (xPos == Coord2[0] and yPos == Coord2[1]):
            a_star_avg.append(counter)
            return curr
        
        Matrix[xPos][yPos] = '1'
        
        if (Matrix[Coord2[0]][Coord2[1]] == '!'):
            return None

        for i in range(4):
            x = xPos + row[i]
            y = yPos + col[i]
           
            hue = heuristic((x,y),Coord2)
            dist = (curr.parent.distance if curr.parent else 0)  + 1
            cost = hue  + dist
            next = ENode(x,y,curr,dist,cost)
            '''
            if not pq.empty():
                print(pq.queue[0].priority)
            '''
            for open_node in pq.queue:
                if next == open_node and next.distance >= open_node.g:
                    break
            else:
               pq.put(next)
            
            
            
    a_star_avg.append(counter)
    return None

def getPath(node,matrix):
    stack = []
    temp = matrix
    while node:
        #print("("+str(node.y) + " , "  + str(node.x)  + ")", end = ' ')
        stack.append((node.y,node.x))
        temp[node.x][node.y] = 'X'
        node = node.parent

   
    while stack:
        print(stack.pop(), end = ' ') 
   
    print("")
    return temp

def startFire(matrix):
    randX = random.randint(0,len(matrix)-1)
    randY = random.randint(0,len(matrix)-1)
    while (matrix[randX][randY] != '0'):
        randX = random.randint(0,len(matrix)-1)
        randY = random.randint(0,len(matrix)-1)

    matrix[randX][randY] = '!'
    return matrix


#print(DFSsearch(a, b, testMatrix))
#print(dfsTestMatrix)
#bfsTemp = BFS(a,b,testMatrix)
#dfsTemp = DFSsearch(a,b,dfsTestMatrix)
testMatrix = createMatrix(10,.2)
astarPathMatrix = deepcopy(testMatrix)
a = (0,0)
b = (9,9)
astar_testMatrix = deepcopy(testMatrix)
astarTemp = a_star(a,b,astar_testMatrix)
testFire = deepcopy(testMatrix)
startFire(testFire)
for i in range(10):
    testFire = advance_fire(testFire,.3)
print(testFire)
print(buildFireMap(testFire))
'''


'''
'''
if dfsTemp:
  
    print("DFS Path: ")
    l = getPath(dfsTemp,dfsPathMatrix)
    print(l)
else:
    print("no path")
'''
'''
if bfsTemp: 
   
    print("BFS Path: ")
    l = getPath(bfsTemp,bfsPathMatrix)
    print(l)

else:
    print("no path")
'''
'''
if astarTemp:
    print("A* Path: ")
    l = getPath(astarTemp,astarPathMatrix)
    print(l)
else:
    print("no path")
print(heuristic(a,b))
'''
'''
print("Trying Strategy 1---------------------------------------|")
stack = []
x = bfsTemp is not None 
if x:
    
    while bfsTemp:
        stack.append((bfsTemp.x,bfsTemp.y))
        bfsTemp = bfsTemp.parent

    prime_path = []
    while stack:
        prime_path.append(stack.pop())

    strat1Matrix = startFire(strat1Matrix)
    print(strategy1(prime_path,strat1Matrix))    
'''
'''
print("Trying Strategy 2--------------------------------------|")
stack = []
x = bfsTemp is not None 
if x:
    
    while bfsTemp:
        stack.append((bfsTemp.x,bfsTemp.y))
        bfsTemp = bfsTemp.parent

    prime_path = []
    while stack:
        prime_path.append(stack.pop())

    strat2Matrix = startFire(strat2Matrix)
    print(strategy2(prime_path,strat2Matrix))

    
'''
'''
#-- DFS success rate vs obsticle density (p)
obsticle_density= np.linspace(.1,1,10)
dfs_success_counter = 0
success_tracker = []
for p in obsticle_density:
    for i  in  range(100):
        loop_matrix = createMatrix(10,p)
        N = len(loop_matrix) - 1
        a = (0,0)
        b = (N,N)
        dfsNode = DFSsearch(a,b,loop_matrix)
        if dfsNode:
            dfs_success_counter += 1

    success_tracker.append(dfs_success_counter / float(100))
    dfs_success_counter = 0

print(obsticle_density)
print(success_tracker)

plt.plot(obsticle_density,success_tracker)

#--- BFS - A star nodes explored vs obsticle density (p)---

diff = []
for p in obsticle_density:
    for i  in  range(100):
        loop_matrix = createMatrix(10,p)
        N = len(loop_matrix) - 1
        a = (0,0)
        b = (N,N)
        bfsNode = BFS(a,b,loop_matrix)
        a_star_node = a_star(a,b,loop_matrix)
        
    bfs_avg_nodes_explored = float((sum(bfs_nodes_explored) / len(bfs_nodes_explored)))
    a_star_avg_nodes = (sum(a_star_avg) / len(a_star_avg))
    diff.append(bfs_avg_nodes_explored - a_star_avg_nodes)
    bfs_nodes_explored = []
    a_star_avg = []
    diff = [round(num, 2) for num in diff]

'''
'''
#--- Strategy 1  and  Strategy 2 success rate vs. fire intensity (q) with stable obstacle density (p = .3)---
fire_rate = np.linspace(.1,1,10)
success_strat1 = []
success_strat2 = []
s1_count = 0
s2_count = 0
for qf in fire_rate:
    for j in range(100):
        strat1 = createMatrix(10,.3)
        strat2 = deepcopy(strat1)
        N = len(strat1) - 1
        a = (0,0)
        b = (N,N)
        bfsNode = BFS(a,b,strat1)
        stack = []
        if (bfsNode is not None):
            while bfsNode:
                stack.append((bfsNode.x,bfsNode.y))
                bfsNode = bfsNode.parent

            prime_path = []
            while stack:
                prime_path.append(stack.pop())

            strat1Matrix = startFire(strat1)
            strat2Matrix = deepcopy(strat1Matrix)
            strat_1_result = strat1_graph(prime_path,strat1Matrix,qf)
            strat_2_result = strat2_graph(prime_path,strat2Matrix,qf)
            
            if strat_1_result:
                s1_count += 1
            
            if strat_2_result:
                s2_count += 1

    success_strat1.append(s1_count)
    success_strat2.append(s2_count)
    s1_count = 0
    s2_count = 0


print("")
print(success_strat1)
print(success_strat2)
print(fire_rate)

'''