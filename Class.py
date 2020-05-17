# 사과장수 프로그램 #2
class FruitSeller:
    def __init__(self, money=0, appleNum=20, price=1000):
        self.myMoney = money
        self.numOfApple = appleNum
        self.APPLE_PRICE = price

    def saleApple(self, money):
        num = money/self.APPLE_PRICE
        self.numOfApple -= num
        self.myMoney += money
        return num

    def showSaleResult(self):
        print('남은 사과: ' + str(self.numOfApple))
        print('판매 매출: ' + str(self.myMoney))

class FruitBuyer:
    def __init__(self, money, appleNum):
        self.myMoney = money
        self.numOfApple = appleNum

    def buyApple(self, seller, money):
        self.numOfApple += seller.saleApple(money)
        self.myMoney -= money

    def showBuyResult(self):
        print('사과 개수: ' + str(self.numOfApple))
        print('현재 잔액: ' + str(self.myMoney))

seller = FruitSeller()
buyer = FruitBuyer(money=5000, appleNum=0)

buyer.buyApple(seller, 2000)

print('과일 판매자의 현 상황')
seller.showSaleResult()
print('과일 구매자의 현 상황')
buyer.showBuyResult()