def main():
    values = [100,20,30,400,50]
    
    limit = 100
    pos = 0
    found = False
    
    while pos < len(values) and not found :
        if values[pos] > limit :
            found = True
        else :
            pos = pos + 1
    if found :
        print("Found at position:", pos)
    else :
        print("Not found") 

main()

