# python3

import sys
import threading
import numpy


    
def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    marked = [False] * n
    height = [0] * n

    for i in range(n):
        if not marked[i]:
            trace = [i]
            marked[i]=True
            height[i]=1
            v= parents[i]
            while v != -1:
                if not marked[v]:
                    marked[v]=True
                    trace.append(v)
                    for j in trace:
                        height[j]+=1

                    v= parents[v]
                else:
                    for j in trace:
                        height[j]+=height[v]
                    v = -1
    # print(height)
    max_height= numpy.max(height)


    
    return max_height


def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

    text = input()
    if 'I' in text:
        size = input()
        text = input()
    elif 'F' in text:
        name = input()
        if not 'a' in name: 
            name = "test/"+name
            f = open(name, "r")
            size = f.readline()
            text = f.readline()
            # text = f.read()
            # raise Exception(text)
    
    Ttree = text.split(" ")
    Itree = []
    for i in Ttree:
        Itree.append(int(i))
    size = len(Itree)
    print(compute_height(size,Itree))
        
    


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
