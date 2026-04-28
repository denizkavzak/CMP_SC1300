##
# Selection sort implementation
##

from random import randint
from time import time

def _main():
    unsortedList = [5,9,17,11,12]
    printList(unsortedList)
    startTime = time()
    selectionSort(unsortedList)
    endTime = time()
    printList(unsortedList)
    
    ## how to time it
    print("Time: ", (endTime - startTime))    
    
    randomList = createRandomList(1000)
    printList(randomList)
    startTime = time()
    selectionSort(randomList)
    endTime = time()
    printList(randomList)
    
    ## how to time it
    print("Time: %.3f seconds" % (endTime - startTime))
    
## we can use perf_counter() 
# from time import perf_counter
# for running times that are too fast
# perf has finer resolution

## Helper function finding minimum position
# in a given list starting from the start
# parameter value
def minimumPosition(values, start):
    minPos = start
    for i in range(start + 1, len(values)):
        if values[i] < values[minPos]:
            minPos = i
            
    return minPos        

def selectionSort(values):
    for i in range(len(values)):
        minPos = minimumPosition(values, i)
        temp = values[minPos]
        values[minPos] = values[i]
        values[i] = temp

def printList(values):
    st = ""
    for i in range(len(values)):
        st = st + str(values[i]) + " "
    print(st)
  
def createRandomList(size):
    randomList = []
    for i in range(size):
        randomList.append(randint(1,100))
    return randomList
  
_main()    