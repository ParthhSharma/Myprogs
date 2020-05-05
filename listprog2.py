inp=input("Enter the elements with commas btw them = ")
lst=inp.split(",")
swap=input("which positions do you want to swap?")
swap=swap.split(",")
temp=lst[int(swap[0])-1]
lst[int(swap[0])-1]=lst[int(swap[1])-1]
lst[int(swap[1])-1]=temp
print(lst)
