#Using Python, write out a function to output the fibbonacci sequence of a given numbe

#fibonacci number = 0,1,1,2,3,5,8,...n

n=int(input("Enter n:"))
a = 0
b = 1

c = a + b

print(a)
print(b)

while c<=n:
    print(c)
    a = b
    b = c
    c = a + b
    
    
     
     
