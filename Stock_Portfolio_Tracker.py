import yfinance as yf
from tabulate import tabulate

portfolio = []

def add_stock():
    symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
    try:
        quantity = float(input("Enter quantity: "))
        buy_price = float(input("Enter buy price per share: "))
        portfolio.append({"symbol": symbol, "quantity": quantity, "buy_price": buy_price})
        print(f"{symbol} added to portfolio.")
    except ValueError:
        print("Invalid input. Try again.")

def remove_stock():
    symbol = input("Enter stock symbol to remove: ").upper()
    global portfolio
    portfolio = [stock for stock in portfolio if stock["symbol"] != symbol]
    print(f"{symbol} removed from portfolio.")

def fetch_stock_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")
        return round(data["Close"].iloc[-1], 2)
    except:
        return None

def view_portfolio():
    if not portfolio:
        print("Your portfolio is empty.")
        return

    table = []
    total_invested = total_current = 0

    for stock in portfolio:
        current_price = fetch_stock_price(stock["symbol"])
        if current_price:
            invested = stock["buy_price"] * stock["quantity"]
            current_value = current_price * stock["quantity"]
            profit = current_value - invested
            profit_pct = (profit / invested) * 100
            table.append([
                stock["symbol"],
                stock["quantity"],
                stock["buy_price"],
                current_price,
                round(profit, 2),
                f"{profit_pct:.2f}%"
            ])
            total_invested += invested
            total_current += current_value
        else:
            table.append([stock["symbol"], "N/A", "N/A", "N/A", "Error", "Error"])

    print("\nPortfolio Summary:")
    headers = ["Symbol", "Qty", "Buy Price", "Current Price", "P/L", "P/L %"]
    print(tabulate(table, headers=headers, tablefmt="pretty"))

    total_profit = total_current - total_invested
    print(f"\nTotal Invested: ${total_invested:.2f}")
    print(f"Current Value:  ${total_current:.2f}")
    print(f"Total Profit/Loss: ${total_profit:.2f}")

def menu():
    while True:
        print("\n--- Stock Portfolio Tracker ---")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            remove_stock()
        elif choice == "3":
            view_portfolio()
        elif choice == "4":
            print("Exiting tracker.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
