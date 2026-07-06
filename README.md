# Simplified Trading Bot (Binance Futures Testnet)

This project is a simplified trading bot built in Python for the Binance Futures Testnet (USDT-M). It allows users to place Market, Limit, and Stop-Limit orders via a command-line interface or a lightweight web frontend.

## Features

*   Connects to Binance Futures Testnet (`https://testnet.binancefuture.com/fapi`).
*   Places Market, Limit, and Stop-Limit orders.
*   Supports both BUY and SELL order sides.
*   Uses the `python-binance` library for API interaction.
*   Includes basic input validation for order parameters.
*   Logs API requests, responses, and errors to a file (`tradingbot.log`) and the console.
*   Provides two interfaces:
    *   A basic Command-Line Interface (CLI).
    *   A lightweight Web Frontend using Flask.

## Project Structure

*   `bot.py`: Contains the `BasicBot` class with the core trading logic and order placement methods.
*   `cli.py`: The command-line interface script for interacting with the bot.
*   `logger.py`: Module for setting up and configuring the project logger.
*   `requirements.txt`: Lists the necessary Python dependencies.
*   `app.py`: The Flask application for the web frontend.
*   `templates/`: Directory containing HTML templates for the web frontend (`index.html`, `result.html`).
*   `static/`: Directory containing static files like CSS (`style.css`) for the web frontend.
*   `tradingbot.log`: (Generated after running) Log file containing records of bot activity, API calls, and errors.

## Setup and Installation
  
1.  **Install dependencies:** Make sure you have Python installed. Then, install the required libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Binance Futures Testnet Account:**
    *   Register and log in to the Binance Futures Testnet: [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
    *   Generate your Testnet API Key and Secret Key from the API Management section. Ensure the keys have permissions for reading and futures trading.
    *   Obtain testnet USDT from the testnet faucet (usually available on the testnet site).

## Running the Bot

You can run the bot using either the CLI or the Web Frontend.

### Running the CLI

Execute the `cli.py` script:

```bash
python cli.py
```

Follow the prompts to enter your Testnet API keys and order details.

### Running the Web Frontend

Execute the `app.py` script:

```bash
python app.py
```

The Flask development server will start, usually at `http://127.0.0.1:5000/`. Open this URL in your web browser to access the frontend. Enter your Testnet API keys and order details in the form.

*(Note: For simplicity, API keys are entered via the form. In a production environment, secure methods like environment variables should be used.)*

## Logging

The bot logs its activity, including API requests, responses, and errors, to the console and the `tradingbot.log` file in the project directory. Check this file for detailed information on order placements and any issues encountered.

## Next Steps / Potential Improvements (Optional)

*   Implement more robust input validation (e.g., against exchange trading rules/filters).
*   Add support for other advanced order types (e.g., OCO).
*   Fetch account balance and display it in the frontend.
*   Implement position management.
*   Use environment variables or a secure config file for API keys in the Flask app.
*   Deploy the Flask app to a production server.

---
