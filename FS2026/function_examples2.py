def main():
    x = 10
    # func1(x)
    # print(countEvens(x))
    # searchForValue(x,5)
    
    string2 = "abcde"
    index = findIndex(string2, "h")
    print(index)
    if index == -1:
        print("Not found")
    else:
        print("Found")

def func1(n):
    for i in range(n):
        if i % 2 == 0:
            print("Even")
        else:
            print("Odd")

def countEvens(n):
    evenCounter = 0
    for i in range(n):
        if i % 2 == 0:
            evenCounter = evenCounter + 1
    return evenCounter

def searchForValue(n, value):
    for i in range(n):
        if i == value:
            print("Found")
            return
        
def findIndex(string1, ch):
    index = 0
    while index < len(string1):
        if string1[index] == ch:
            return index
        index = index + 1
        #print(index)
             
    return -1 # if code is here, it means it was not found

main()