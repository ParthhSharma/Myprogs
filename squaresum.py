#to print sum of squares of n natural numbers
n=input("upto which natural number?--->")
n=int(n)
i=1
sum=0
while i<=n:
    sum+=i*i
    i+=1
print("sum of squares of ",n,"natural numbers is ",sum)
