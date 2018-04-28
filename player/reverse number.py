m=int(input("enter the number: "))
n=0
while(m>0):
    c=m%10
    n=n*10+c
    m=m//10
print(n)
