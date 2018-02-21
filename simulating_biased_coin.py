from random import random
def biasedCoin():
    return int(random() < 0.2)

def fairCoin():
    coin1, coin2 = 0, 0
    while coin1 == coin2:
        coin1, coin2 = biasedCoin(), biasedCoin()
    return coin1

sum(fairCoin() for x in range(100000)) / 100000
