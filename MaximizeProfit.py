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

# http://keithschwarz.com/interesting/code/?dir=single-sell-profit
def BruteForceSingleSellProfit(arr):
    # Store the best possible profit we can make; initially this is 0.
    bestProfit = 0;

    # Iterate across all pairs and find the best out of all of them.  As a
    # minor optimization, we don't consider any pair consisting of a single
    # element twice, since we already know that we get profit 0 from this.
    for i in range(0, len(arr)):
        for j in range (i + 1, len(arr)):
            bestProfit = max(bestProfit, arr[j] - arr[i])

    return bestProfit


def DynamicProgrammingSingleSellProfit(arr):
    # If the array is empty, we cannot make a profit.
    if len(arr) == 0:
        return 0

    # Otherwise, keep track of the best possible profit and the lowest value
    # seen so far.
    profit = 0
    cheapest = arr[0]

    # Iterate across the array, updating our answer as we go according to the
    # above pseudocode.
    for i in range(1, len(arr)):
        # Update the minimum value to be the lower of the existing minimum and
        # the new minimum.
        cheapest = min(cheapest, arr[i])

        # Update the maximum profit to be the larger of the old profit and the
        # profit made by buying at the lowest value and selling at the current
        # price.
        profit = max(profit, arr[i] - cheapest)

    return profit


def findMaxProfit(arr):
    maxPos, maxVal = 0, arr[0]
    minPos, minVal = 0, arr[0]
    profit = maxVal - minVal
    for i in range(1, len(arr)):
        if arr[i] < minVal:
            minPos, minVal = i, arr[i]

        tmpProfit = arr[i] - minVal
        if profit < tmpProfit:
            maxPos, maxVal = i, arr[i]
            profit = tmpProfit

    return profit, minPos+1, maxPos+1

ARR1 = [-1, 0, 3, 6, 5, 2, -10]
ARR2 = [5, 10, 4, 6, 12]
ARR3 = [-10, 4, 3, 10, 30]
ARR4 = [15, 10, 4, 6, 12, -10]


ARR_N = [ARR1, ARR2, ARR3, ARR4]

for k in ARR_N:
    print("My    - ", findMaxProfit(k)) 
    #print("Max   - ", maxProfit(i)) # incorrect
    print("Dyn   - ", DynamicProgrammingSingleSellProfit(k))
    print("Brute - ", BruteForceSingleSellProfit(k))
    print("------")
