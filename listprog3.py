list1=input("Enter a sentence with repetetive words")
list1=list1.split()
print(list1)
w=input("which word? =")
N=int(input("which occurance of this word? ="))
count=0
list2=list()
for x in list1:
    if x==w:
        count+=1
        if count!=N:
            list2.append(x)
    else:
        list2.append(x)
print(list2)
