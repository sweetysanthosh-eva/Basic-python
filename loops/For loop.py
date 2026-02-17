for i in range(1,6):
    print(i)
for i in range(1,6,2):
    print(i)
for i in range(5):
    print(i)
for i in range(1,11,4):
    print(i)
for i in range(1,11,2):
    print(i)
name= "subitty"
for i in name:
    if i=="t":
        #print(i)
        continue
    else:
        print("no")

c=0
for i in name:
    if i=="t":
        pass
    c=c+1
print(c)




