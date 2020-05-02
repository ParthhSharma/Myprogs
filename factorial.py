#TO CALCULATE FACTORIAL OF A NUMBER ENTER BY USER
num = input("enter the number = ")
num = int(num)
def factorial(n) :
    if n==0 or n==1 :
        return 1
    else :
        return ((n)*factorial(n-1))
print("the factorial of",num,"is",factorial(num))
