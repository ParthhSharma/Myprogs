#TO PRINT FIBONACCI SERIES
k=input("Enter number of elements in the fibonacci series = ")
k=int(k)
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
i=1
while i<=k:
    print(fib(i))
    i+=1
