from copy import deepcopy

COINS = (1, 5, 10, 25)

def ways_to_pay(n):
    dp = [[] for i in range(n+1)]
    dp[0].append([])
    for coin in reversed(COINS):
        idx = 0
        while idx + coin <= n:
            for e in dp[idx]:
                new = deepcopy(e)
                new.append(coin)
                dp[idx + coin].append(new)



if __name__ == '__main__':
    # for i in range(25):
    #     print(recursive_ways_to_pay(i))

    print(ways_to_pay(6))