for i in range(10):
    print(i)
    
for i in "rajesh kumar":
    print(i)
    
a=[1,4,6,78,8,9]
for i in a:
    print(i)
    
for i in range(20,1,-1):
    print(i)

for i in range(1,20,2):
    print(i)
    
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if(i%2==0):
        print(i,"is even")
    else:
        print(i,"is odd")

a=[4,6,7,89,12,45]
for i in a:
    if(i==6):
        print(i)
        break
    print(i)
    
a=[4,6,7,89,12,45]
for i in a:
    if(i==6):
        continue
    print(i)

i=0
while(i<=20):
    print(i)
    i=i+1

a=0
b=0
while(a<=10 and b<=20):
    print(a,b)
    a=a+1
    b=b+2

a=1
b=1
while(a<=10 and b<=10):
    c=a*b
    print(a,b,"is",c)
    a=a+1
    b=b+1

c=0
while(c<=1):
    for i in "srkd":
        print(i)
    c=c+1

def rk(i,j):
    c=i+j
    return c
def m(i,j):
    c=i*j
    return c

a=int(input("enter the number:"))
b=int(input("enter the number:"))
print(rk(a,b))
print(m(a,b))



    
