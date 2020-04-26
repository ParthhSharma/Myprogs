#TO PRINT ALL PRIME NUMBERS IN AN INTERVAL
f_r_o_m=input("checking prime numbers in the interval from - ")
to=input("to - ")
f_r_o_m=int(f_r_o_m)
to=int(to)
i=f_r_o_m
while i<=to :
    j=1
    c=0
    while j<=i :
        if i%j==0 :
            c+=1
        j+=1
    if c==2 :
        print(i)
    i+=1
