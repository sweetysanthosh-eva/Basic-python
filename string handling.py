message="Hello World"
print (message[1])
print (message[-1])

#slicing
print(message[:5])
print(message[2:7])

#string concatenation
concat="hey "+message
print(concat)

#case changing
print(message.upper())
print(message.lower())
print(message.title())

#searching
print("hey" in concat)

#replacing
new = message.replace("Hello","who")
print(new)
s1="hello"
s2="hello"
print(s1==s2)
print(s1 is s2)

