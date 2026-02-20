# Binance Futures Trading Bot (Testnet)

This project is a **Python CLI bot** that places **MARKET** and **LIMIT** orders on Binance Futures Testnet.  
It demonstrates correct API integration, order handling, and prints detailed order responses.

---

## Features

- Place **MARKET orders** that execute immediately if minimum order size is met.  
- Place **LIMIT orders** near market price for testing purposes.  
- Compatible with **One-Way mode accounts** (no `positionSide` needed).  
- Prints **order summary** and **order response** including `status`, `executedQty`, and `average price`.

---

## Project Structure
trading_bot/
├── bot/
│   ├── check_bal.py
│   ├── client.py
    ├── config.py
    ├── orders.py
    ├── test.py
    ├── validators.py    
├── cli.py
├── requirements.txt
└── README.md

## Exmaple Commnad
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.005 --price 40000

## output

===== ORDER SUMMARY =====
Symbol: BTCUSDT
Side: BUY
Type: LIMIT
Quantity: 0.005
Price: 40000.0

===== ORDER RESPONSE =====
Order ID: 12420957116
Status: NEW
Executed Quantity: 0.000
Average Price: 0.00
SUCCESS ✅
