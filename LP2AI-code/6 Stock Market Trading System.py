#Stock Market Trading System
class StockMarketTradingSystem:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, company_name, price):
        self.stocks[symbol] = {'company_name': company_name, 'price': price}
        print("Stock added successfully!")

    def update_stock_price(self, symbol, price):
        if symbol in self.stocks:
            self.stocks[symbol]['price'] = price
            print("Stock price updated successfully!")
        else:
            print("Stock not found.")

    def get_stock_info(self, symbol):
        if symbol in self.stocks:
            print(f"Stock Symbol: {symbol}")
            for key, value in self.stocks[symbol].items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Stock not found.")

# Example usage with user input:
stock_system = StockMarketTradingSystem()

while True:
    print("\n1. Add Stock\n2. Update Stock Price\n3. Get Stock Information\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        symbol = input("Enter stock symbol: ")
        company_name = input("Enter company name: ")
        price = float(input("Enter stock price: "))
        stock_system.add_stock(symbol, company_name, price)
    elif choice == '2':
        symbol = input("Enter stock symbol: ")
        price = float(input("Enter new stock price: "))
        stock_system.update_stock_price(symbol, price)
    elif choice == '3':
        symbol = input("Enter stock symbol: ")
        stock_system.get_stock_info(symbol)
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
