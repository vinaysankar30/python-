def Pali(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
        if(temp==rev):
            print(rev)
        else:
            break
n = int(input("enter no"))
for i in range(0,100):
    print(Pali(i))
    