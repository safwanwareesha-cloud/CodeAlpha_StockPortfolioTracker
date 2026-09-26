def stock_tracker():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 420,
        "AMZN": 180
    }

    total_investment = 0

    print("Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    while True:
        stock = input("Enter stock name (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not found. Please choose from the available stocks.")
            continue

        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"{stock}: ${stock_prices[stock]} x {quantity} = ${investment}")

    print(f"\nTotal Investment Value: ${total_investment}")


stock_tracker()