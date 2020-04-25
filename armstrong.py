num=input("Enter the number to be checked = ")
c=0
for x in num :
    c+=1
num=int(num)
num2=num
sum=0
while num>=0 :
    r=num%10
    sum+=pow(r,c)
    num/=10
if sum==num2 :
    print("YES!! it is an Armstrong number")
else :
    print("NO!! it is not an Armstrong number")
