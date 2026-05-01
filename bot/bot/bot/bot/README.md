# Binance Futures Testnet Trading Bot

A simple Python CLI application to place MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M). Built with pure `requests` and custom HMAC SHA256 signing for maximum transparency and minimal dependencies.

## Setup

1. **Clone the repository** (or unzip the folder) and navigate to the project root.
2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   3.Set your API credentials as environment variables:
   Linux / macOS:
   export BINANCE_API_KEY="your_testnet_api_key"
export BINANCE_API_SECRET="your_testnet_api_secret"
Windows (Command Prompt):
set BINANCE_API_KEY=your_testnet_api_key
set BINANCE_API_SECRET=your_testnet_api_secret

How to Run Examples
1. Place a MARKET BUY Order
  python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

2. Place a LIMIT SELL Order
  python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.05 --price 80000

   Logging
All API requests, responses, and errors are safely logged to bot.log in the root directory.
Assumptions
The user has sufficient USDT testnet funds to execute the requested orders.
The API Key has Futures trading permissions enabled on the Testnet.
The system time is synced (Binance API rejects requests if the local timestamp is outside the receiving window).
