def moveK(num1):

    maxi =0
    n=len(num1)

    for i in range(0,n):
        num=num1[i]
        count=1
        while num+1 in num1:
            count=count+1
            num=num+1
        maxi=max(maxi,count)
    return maxi

print(moveK([1,99,101,98,2,5,3,100,1,1]))
# num = [1,2,3,4,5]