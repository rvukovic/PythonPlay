# http://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/
# Returns maximum profit with two transactions on a given 
# list of stock prices price[0..n-1]
def maxProfit(price):
    n = len(price)
    # Create profit array and initialize it as 0
    profit = [0]*n
     
    # Get the maximum profit with only one transaction
    # allowed. After this loop, profit[i] contains maximum
    # profit from price[i..n-1] using at most one trans.
    max_price=price[n-1]
     
    for i in range( n-2, 0 ,-1):
         
        if price[i]> max_price:
            max_price = price[i]
             
        # we can get profit[i] by taking maximum of:
        # a) previous maximum, i.e., profit[i+1]
        # b) profit by buying at price[i] and selling at
        #    max_price
        profit[i] = max(profit[i+1], max_price - price[i])
         
    # Get the maximum profit with two transactions allowed
    # After this loop, profit[n-1] contains the result    
    min_price=price[0]
     
    for i in range(1,n):
         
        if price[i] < min_price:
            min_price = price[i]
 
        # Maximum profit is maximum of:
        # a) previous maximum, i.e., profit[i-1]
        # b) (Buy, Sell) at (min_price, A[i]) and add
        #    profit of other trans. stored in profit[i]    
        profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))
         
    result = profit[n-1]
    return result

def findMaxProfit(arr):
    maxPos, maxVal = 0, arr[0]
    minPos, minVal = 0, arr[0]
    for i in range(1, len(arr)):
        if arr[i] < minVal and maxPos >= i:
            minPos, minVal = i, arr[i]
        elif arr[i] > maxVal and maxPos >= minPos:
            maxPos, maxVal = i, arr[i]

    return maxVal-minVal, minPos+1, maxPos+1


ARR = [ -1, 0 ,3 , 6, 5, 2, -10]

print(maxProfit(ARR))
print(findMaxProfit(ARR))