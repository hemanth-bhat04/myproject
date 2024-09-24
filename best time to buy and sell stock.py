def maxprofit(prices):
    l,r=0,1
    maxp=0
    while r<len(prices):#iterate through the prices list
        if prices[l]<prices[r]:
            profit=prices[r]-prices[l]
            maxp=max(maxp,profit)
        else:
            l=r
        r+=1
    print("Maximum Profit is "+ str(maxp))
prices=[5,2,7,1,4]
maxprofit(prices)
