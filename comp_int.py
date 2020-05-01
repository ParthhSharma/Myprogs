#TO CALCULATE COMPOUND INTEREST
p=input("Enter the principal amount (in INR) = ")
p=float(p)
r=input("Enter the rate of interest (%) =  ")
r=float(r)
t=input("Enter the time span (in years) = ")
t=float(t)
comp_int=p*(pow((1+r/100),t))
print("The compund interest is calculated to be = INR ",comp_int)
