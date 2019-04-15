def findMinimumCoins(V):
    denominations = [1,5,10,25]
    total_denominations = len(denominations)

    change = [0,0,0,0]

    i = total_denominations - 1
    while (i >= 0):

        while (V >= denominations[i]):
            V -= denominations[i]
            change[i]=change[i]+1;

        i -= 1

    for i in range(len(change)):
        if change[i]!=0:
            if change[i]==1:
                print(change[i],"coin of denomination",denominations[i])
            else:
                print(change[i], "coins of denomination", denominations[i])


if __name__ == '__main__':
    try:
        N = int(input("Enter value to make change : "))
        print("Making change for",N,"requires")
        findMinimumCoins(N)

    except Exception as e:
        print("Please enter valid input")

