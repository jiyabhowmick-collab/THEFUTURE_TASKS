n=int(input("Enter no: "))
a=0
b=1
count=0
total=0
print("jiya")
while a<=n:
    print(a,end=" ")
    total+=a
    count+=1
    c=a+b
    a=b
    b=c
print("\nTotal terms generated: ",count)
print("\nSum of series: ",total)
