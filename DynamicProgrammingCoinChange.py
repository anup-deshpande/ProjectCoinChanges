def findMinimumCoins(coinValueList,N,minCoins,coinsUsed):

   for cents in range(N+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[N]

def printChange(coinsUsed,N):
   coin = N
   dict={}

   while coin > 0:
       thisCoin = coinsUsed[coin]
       if thisCoin in dict.keys():
           dict[thisCoin]=dict.get(thisCoin)+1
       else:
           dict.update({thisCoin: 1})
       coin = coin - thisCoin

   for i in dict.keys():
       if dict.get(i) != 0:
           if dict[i] == 1:
               print(dict[i], "coin of denomination",i)
           else:
               print(dict[i], "coins of denomination",i)

if __name__== '__main__':
   # try:
        N = int(input("Enter value to make change : "))
        print("Making change for",N,"requires")
        denominations = [1, 5, 10, 25]
        coinsUsed = [0] * (N + 1)
        coinCount = [0] * (N + 1)

        findMinimumCoins(denominations, N, coinCount, coinsUsed)
        printChange(coinsUsed, N)

#    except Exception as e:
 #       print("Please enter valid input")
