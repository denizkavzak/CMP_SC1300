def main():
    print(func1(2))

def func1(a):
    # result = func2(a)
    # result2 = func3(result)
    # return result2
    return func3(func2(a))

def func2(b):
    return b ** b

def func3(c):
    return c * 3

main()