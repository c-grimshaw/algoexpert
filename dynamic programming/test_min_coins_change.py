from min_coins_change import minNumberOfCoinsForChange

def testMinNumberOfCoinsForChange():
    assert minNumberOfCoinsForChange(n=7, denoms=[1,5,10]) == 3
    assert minNumberOfCoinsForChange(n=6, denoms=[1,2,4]) == 2
    assert minNumberOfCoinsForChange(n=1, denoms=[10]) == -1
    assert minNumberOfCoinsForChange(n=135, denoms=[39, 45, 130, 40, 4, 1, 60, 75]) == 10