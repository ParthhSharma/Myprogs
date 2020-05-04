inp=input("Enter the elements with commas btw them = ")
lst=inp.split(",")
count=0
for num in lst:
    count+=1
temp=lst[0]
lst[0]=lst[count-1]
lst[count-1]=temp
print(lst)
