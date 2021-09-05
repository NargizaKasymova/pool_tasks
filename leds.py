a=input()
a1=int(a)

# b=[]

for i in range(a1):
    b1=input()
    b.append(b1)

for i in range(len(b)):
    print(b[i])
    sum=0
    for j in range(len(b[i])):
        # print(b[i][j])
        if int(b[i][j])==1:
            sum=sum+2
        if int(b[i][j])==2:
            sum=sum+5
        if int(b[i][j])==3:
            sum=sum+5
        if int(b[i][j])==4:
            sum=sum+4
        if int(b[i][j])==5:
            sum=sum+5
        if int(b[i][j])==6:
            sum=sum+6
        if int(b[i][j])==7:
            sum=sum+3
        if int(b[i][j])==8:
            sum=sum+7
        if int(b[i][j])==9:
            sum=sum+6
        if int(b[i][j])==0:
            sum=sum+6
    print(str(sum)+" "+"leds")