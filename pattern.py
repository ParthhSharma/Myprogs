import sys
i = 1
while i<=5 :
    j = 1
    while j<=i :
        sys.stdout.write("*")
        j+=1
    print("\n")
    i+=1
