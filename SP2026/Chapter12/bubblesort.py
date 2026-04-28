##
# Selection sort implementation
##

from random import randint
from time import time

def _main():
    unsortedList = [5,9,17,11,12]
    printList(unsortedList)
    startTime = time()
    bubbleSort(unsortedList)
    endTime = time()
    printList(unsortedList)
    
    ## how to time it
    print("Time: %.3f seconds" % (endTime - startTime))    
    
    randomList = createRandomList(10000)
    #printList(randomList)
    startTime = time()
    bubbleSort(randomList)
    endTime = time()
    #printList(randomList)
    
    ## how to time it
    print("Time: %.3f seconds" % (endTime - startTime))
    
## we can use perf_counter() 
# from time import perf_counter
# for running times that are too fast
# perf has finer resolution

def bubbleSort(values):
    for i in range(len(values)):
        for j in range(len(values)-1):
            if values[j]>values[j+1]:
                swap(values, j, j+1)
                # temp = values[j]
                # values[j] = values[j+1]
                # values[j+1] = temp        


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
 
def swap(values, index1, index2):
    temp = values[index1]
    values[index1] = values[index2]
    values[index2] = temp
  
_main()    