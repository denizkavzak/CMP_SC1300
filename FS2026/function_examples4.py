def main():
    listOfValues = [100,20,30,400,50]
    limit = 500
    print(findIndex(listOfValues, limit))
    
def findIndex(listOfValues, limit):
    found = False
    pos = 0
    while pos < len(listOfValues) and not found :
        if listOfValues[pos] > limit :
            found = True
        else :
            pos = pos + 1
    return found

main()