from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
from logger import setup_logger

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.logger = setup_logger()
        self.client = Client(api_key, api_secret, testnet=testnet)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        self.logger.info("Initialized Binance Client (Testnet: %s)", testnet)

    def place_market_order(self, symbol, side, quantity):
        try:
            side = side.upper()
            if side not in ['BUY', 'SELL']:
                self.logger.error(f"Invalid side: {side}")
                print("Order side must be BUY or SELL.")
                return
            quantity = float(quantity)
            self.logger.info(f"Placing MARKET order: {side} {quantity} {symbol}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            self.logger.info(f"Order response: {order}")
            print(f"Market order placed: {order}")
        except BinanceAPIException as e:
            self.logger.error(f"Binance API Exception: {e}")
            print(f"API Error: {e}")
        except Exception as e:
            self.logger.error(f"Exception: {e}")
            print(f"Error: {e}")

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            side = side.upper()
            if side not in ['BUY', 'SELL']:
                self.logger.error(f"Invalid side: {side}")
                print("Order side must be BUY or SELL.")
                return
            quantity = float(quantity)
            price = float(price)
            self.logger.info(f"Placing LIMIT order: {side} {quantity} {symbol} @ {price}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            self.logger.info(f"Order response: {order}")
            print(f"Limit order placed: {order}")
        except BinanceAPIException as e:
            self.logger.error(f"Binance API Exception: {e}")
            print(f"API Error: {e}")
        except Exception as e:
            self.logger.error(f"Exception: {e}")
            print(f"Error: {e}")

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        try:
            side = side.upper()
            if side not in ['BUY', 'SELL']:
                self.logger.error(f"Invalid side: {side}")
                print("Order side must be BUY or SELL.")
                return
            quantity = float(quantity)
            price = float(price)
            stop_price = float(stop_price)
            self.logger.info(f"Placing STOP-LIMIT order: {side} {quantity} {symbol} Stop: {stop_price} Limit: {price}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_STOP_LOSS_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price,
                stopPrice=stop_price
            )
            self.logger.info(f"Order response: {order}")
            print(f"Stop-Limit order placed: {order}")
        except BinanceAPIException as e:
            self.logger.error(f"Binance API Exception: {e}")
            print(f"API Error: {e}")
        except Exception as e:
            self.logger.error(f"Exception: {e}")
            print(f"Error: {e}") 