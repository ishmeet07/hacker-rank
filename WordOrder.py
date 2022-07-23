# Enter your code here. Read input from STDIN. Print output to STDOUT
s=dict()
l=[]
sum =0
i=int(input())

for k in range (0,i):
    l.append(input())
 
for x in l:
        if x  in s:
            s[x]+=1
        else:
             s[x]=1    
for x  in s:
    sum+=1
print(sum) 
for key in s:
 print (s[key],"",end="")   
