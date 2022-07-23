n=int(input())
x=[]
sum=0
s=dict()
x=list(map(int,input().split()))

for l in x:
    if l in s:
        s[l]+=1
    else:
        s[l]=1            
k=int(input())
for i in range(0,k):
    size,price=(map(int,input().split()))
   
    if size in s and s[size]!=0:
        sum+=price 
        s[size]-=1 
        
print(sum)   
