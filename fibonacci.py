#TO OBTAIN nth FIBONACCI NUMBER
n=input("Enter which fibonacci number you need = ")
n=int(n)
def fibonacci(k) :
    if k<=0 :
        print("invalid input")
    elif k==1 :
        return 0
    elif k==2 :
        return 1
    else :
        return (fibonacci(k-1)+fibonacci(k-2))
print(fibonacci(n))
