pos, neg = 0, 0
num = int(input())
while num != 0 :
    if num > 0 :
        pos += num 
    else :
        neg += num 
    num = int(input())
print(pos,'\n',neg)
        
 
print(*[i for i in range(1,int(input())+1) if (i*i) % (10**len(str(i))) == i])
