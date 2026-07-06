from flask import Flask, render_template, request
from bot import BasicBot
from logger import setup_logger

app = Flask(__name__)

# Although we initialize the bot here, API keys will be taken from the form for each request
bot = None # This will be instantiated in place_order

# Basic validation functions (can be expanded)
def is_valid_symbol(symbol):
    # In a real bot, you'd fetch supported symbols from the exchange
    return symbol.isalnum() and symbol.upper().endswith('USDT')

def is_valid_side(side):
    return side.upper() in ['BUY', 'SELL']

def is_valid_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False
    except TypeError:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/place_order', methods=['POST'])
def place_order():
    api_key = request.form.get('api_key')
    api_secret = request.form.get('api_secret')
    symbol = request.form.get('symbol', '').upper()
    side = request.form.get('side', '').upper()
    quantity_str = request.form.get('quantity')
    order_type = request.form.get('order_type')
    price_str = request.form.get('price')
    stop_price_str = request.form.get('stop_price')

    # Input validation
    if not api_key or not api_secret:
        return render_template('result.html', message="Error: API Key and Secret are required.")
    if not is_valid_symbol(symbol):
        return render_template('result.html', message=f"Error: Invalid symbol {symbol}. Must be alphanumeric and end with 'USDT'.")
    if not is_valid_side(side):
        return render_template('result.html', message=f"Error: Invalid side {side}. Must be BUY or SELL.")
    if not is_valid_float(quantity_str):
         return render_template('result.html', message="Error: Invalid quantity. Must be a number.")

    quantity = float(quantity_str)

    try:
        # Initialize bot with keys from form
        bot = BasicBot(api_key, api_secret, testnet=True)

        if order_type == 'MARKET':
            result = bot.place_market_order(symbol, side, quantity)
            message = "Market order placed."
        elif order_type == 'LIMIT':
            if not is_valid_float(price_str):
                return render_template('result.html', message="Error: Invalid limit price. Must be a number.")
            price = float(price_str)
            result = bot.place_limit_order(symbol, side, quantity, price)
            message = "Limit order placed."
        elif order_type == 'STOP_LIMIT':
            if not is_valid_float(stop_price_str):
                 return render_template('result.html', message="Error: Invalid stop price. Must be a number.")
            if not is_valid_float(price_str):
                 return render_template('result.html', message="Error: Invalid limit price. Must be a number.")
            stop_price = float(stop_price_str)
            price = float(price_str)
            result = bot.place_stop_limit_order(symbol, side, quantity, price, stop_price)
            message = "Stop-Limit order placed."
        else:
            return render_template('result.html', message="Error: Invalid order type.")

        # The bot methods print output directly, so we'll just indicate success here.
        # In a more complex app, you'd get return values from bot methods.
        return render_template('result.html', message=message, details="Check console/logs for details.")

    except Exception as e:
        # Log the error in the Flask app context
        app.logger.error(f"An error occurred: {e}")
        return render_template('result.html', message="An error occurred:", details=str(e))

if __name__ == '__main__':
    # Note: In a real application, you would not hardcode keys here.
    # We will handle key input via the form for simplicity in this example.
    # For deployment, set debug=False and use a production-ready server like Gunicorn or uWSGI
    app.run(debug=True) 