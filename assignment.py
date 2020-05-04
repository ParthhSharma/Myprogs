import re
inp=input("Enter the file name")
fh=open(inp)
listofnum=list()
for line in fh:
    stuff=re.findall('[0-9]+',line)
    listofnum+=stuff
sum=0
for num in listofnum:
    num=int(num)
    sum+=num
print(sum)
