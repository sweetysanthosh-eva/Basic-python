def findmax(*args):  # *args is used for variable length function
    print(max(args))
    return max(args)
print(findmax(5,9,12))
print(findmax(2,6))
print(findmax(3,))

def findmin(*args):
    print(min(args))
    return min(args)
print(findmin(5,9,12))
print(findmin(2,6))

