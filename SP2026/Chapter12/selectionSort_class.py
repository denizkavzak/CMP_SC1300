def findMinimumIndex(unsortedList, startIndex):
    minIndex = startIndex
    for j in range(startIndex + 1, len(unsortedList)):
        if unsortedList[minIndex] > unsortedList[j]:
            minIndex = j
    return minIndex

## implementing the selection sort
unsortedList = [5, 9, 17, 11, 12]

for i in range(len(unsortedList)-1):
    # find the minimum in the list i to end of the list
    minIndex = findMinimumIndex(unsortedList, i)
    if minIndex != i:
        temp = unsortedList[minIndex]
        unsortedList[minIndex] = unsortedList[i]
        unsortedList[i] = temp
        
## print the sorted list
for i in range(len(unsortedList)):
    print(unsortedList[i])
    
    