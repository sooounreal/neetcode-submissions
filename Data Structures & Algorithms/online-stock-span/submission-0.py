

class StockSpanner:

    def __init__(self):
        self.hist_prices = []

    def next(self, price: int) -> int:
        res = 1
        for i in range(len(self.hist_prices)-1, -1, -1):
            if self.hist_prices[i] <= price:
                res += 1
            else:
                break
        self.hist_prices.append(price)
        return res