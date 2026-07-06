from bot import BasicBot

def is_valid_symbol(symbol):
    return symbol.isalnum() and symbol.endswith('USDT')

def is_valid_side(side):
    return side.upper() in ['BUY', 'SELL']

def is_valid_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def main():
    print("Welcome to the Binance Futures Testnet Trading Bot!")
    api_key = input("Enter your Binance API Key: ").strip()
    api_secret = input("Enter your Binance API Secret: ").strip()
    bot = BasicBot(api_key, api_secret, testnet=True)

    while True:
        print("\nOrder Menu:")
        print("1. Market Order")
        print("2. Limit Order")
        print("3. Stop-Limit Order")
        print("4. Exit")
        choice = input("Select order type (1/2/3/4): ").strip()

        if choice == '4':
            print("Exiting bot.")
            break

        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            continue

        symbol = input("Enter symbol (e.g., BTCUSDT): ").strip().upper()
        if not is_valid_symbol(symbol):
            print("Invalid symbol. Must be alphanumeric and end with 'USDT'.")
            continue

        side = input("Enter side (BUY/SELL): ").strip().upper()
        if not is_valid_side(side):
            print("Invalid side. Must be BUY or SELL.")
            continue

        quantity = input("Enter quantity: ").strip()
        if not is_valid_float(quantity):
            print("Invalid quantity. Must be a number.")
            continue

        if choice == '1': # Market Order
            bot.place_market_order(symbol, side, quantity)
        
        elif choice == '2': # Limit Order
            price = input("Enter limit price: ").strip()
            if not is_valid_float(price):
                print("Invalid price. Must be a number.")
                continue
            bot.place_limit_order(symbol, side, quantity, price)

        elif choice == '3': # Stop-Limit Order
            stop_price = input("Enter stop price: ").strip()
            if not is_valid_float(stop_price):
                print("Invalid stop price. Must be a number.")
                continue
            price = input("Enter limit price: ").strip()
            if not is_valid_float(price):
                print("Invalid limit price. Must be a number.")
                continue
            bot.place_stop_limit_order(symbol, side, quantity, price, stop_price)


if __name__ == "__main__":
    main() 