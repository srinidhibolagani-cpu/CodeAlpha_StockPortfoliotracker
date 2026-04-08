# Stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130
}

total_investment = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total_investment += value
        print(f"Investment in {stock}: ₹{value}")
    else:
        print("Stock not found!")

print("Total Investment Value: ₹", total_investment)
