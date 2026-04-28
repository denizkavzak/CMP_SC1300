## Merge sort implementation

from random import randint
from time import time

def _main():
    unsortedList = [5,9,17,11,12]
    printList(unsortedList)
    startTime = time()
    mergeSort(unsortedList)
    endTime = time()
    printList(unsortedList)
    
    ## how to time it
    print("Time: %.3f seconds" % (endTime - startTime))    
    
    randomList = createRandomList(10)
    printList(randomList)
    startTime = time()
    mergeSort(randomList)
    endTime = time()
    printList(randomList)
    
    ## how to time it
    print("Time: %.3f seconds" % (endTime - startTime))
    
## we can use perf_counter() 
# from time import perf_counter
# for running times that are too fast
# perf has finer resolution

def mergeSort(values):
    if len(values) <=1: 
        return
    
    mid = len(values) // 2
    firstHalf = values[ : mid]
    secondHalf = values[mid : ]
    mergeSort(firstHalf)
    mergeSort(secondHalf)
    mergeLists(firstHalf, secondHalf, values)
    
    
def mergeLists(firstHalf, secondHalf, values):
    currentIndexFirstHalf = 0
    currentIndexSecondHalf = 0
    currentIndexInValues = 0

    # loop while both halves still have values to be checked    
    while currentIndexFirstHalf < len(firstHalf) and currentIndexSecondHalf < len(secondHalf):
        if firstHalf[currentIndexFirstHalf] < secondHalf[currentIndexSecondHalf]:
            values[currentIndexInValues] = firstHalf[currentIndexFirstHalf]
            currentIndexFirstHalf += 1
        else:
            values[currentIndexInValues] = secondHalf[currentIndexSecondHalf]    
            currentIndexSecondHalf += 1    
            
        currentIndexInValues += 1
        
    # now one of the halves might still have elements
    # to be added to the values list
    
    # if the firstHalf still has elements:
    while currentIndexFirstHalf < len(firstHalf):
        values[currentIndexInValues] = firstHalf[currentIndexFirstHalf]
        currentIndexFirstHalf += 1
        currentIndexInValues += 1
    
    # if the secondHalf still has elements:
    while currentIndexSecondHalf < len(secondHalf):
        values[currentIndexInValues] = secondHalf[currentIndexSecondHalf]
        currentIndexSecondHalf += 1
        currentIndexInValues += 1
        
        
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