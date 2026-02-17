def add(x,y): #x and y is called formal parameter
    print(x+y)
add(5,6)
add(4,5) #4,5 values is actual parameter
def addition(x,y):
    return x+y
print(addition(8,9))
#multiple types of user defined functions
def addition(x,y):
    return x+y,x-y,x*y,x/y
print(addition(5,6))
print(addition(4,5))
