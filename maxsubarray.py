def maxsubarray(nums):
    maxsub=nums[0]#initialise the 1st element of the list to zero
    cursum=0
    for n in nums:#iterating through the list
        if cursum<0:
            cursum=0
        cursum+=n
        maxsub=max(maxsub,cursum)
    print(maxsub)
nums=[-2,1,2,3,-1,4,-3]
maxsubarray(nums)
