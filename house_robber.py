def rob(nums:list[int])->int:
    r1=0
    r2=0
    for n in nums:
        temp=max(n+r1,r2)
        r1=r2
        r2=temp
    print(r2)
nums=[1,2,3,1,4,5,6,8]
rob(nums)