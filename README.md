\# 📈 Binance Futures Trading Bot (Testnet)

A simple Python-based CLI trading bot that places **MARKET** and **LIMIT** orders on Binance Futures Testnet (USDT-M).
Built as part of an internship assignment to demonstrate API integration, clean code structure, logging, and error handling.

---

## 🚀 Features

* ✅ Place **MARKET** orders
* ✅ Place **LIMIT** orders
* ✅ Supports both **BUY** and **SELL**
* ✅ CLI-based input using `argparse`
* ✅ Input validation
* ✅ Logging of API requests, responses, and errors
* ✅ Structured, modular code

---

## 🛠 Tech Stack

* Python 3.x
* python-binance
* argparse (built-in)
* logging (built-in)
* python-dotenv

---

## 📂 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance API client setup
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│   └── cli.py             # CLI entry point
│
├── logs/                  # Log files (generated at runtime)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/trading-bot-binance.git
cd trading-bot-binance
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Create `.env` file

Create a `.env` file in the root directory:

```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret_key
```

⚠️ Do NOT share or upload your `.env` file.

---

### 4. Binance Testnet Setup

* Register at: https://testnet.binancefuture.com
* Generate API keys from API Management
* Use those keys in `.env`

---

## ▶️ Usage

### 🔹 MARKET Order

```
python bot/cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### 🔹 LIMIT Order

```
python bot/cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## 📊 Output Example

```
✅ Order Success!
Order ID: 12345678
Status: FILLED
Executed Qty: 0.001
Avg Price: 60000
```

---

## 🧾 Logging

* Logs are stored in: `logs/app.log`
* Includes:

  * API request details
  * API responses
  * Errors and exceptions

---

## ⚠️ Error Handling

The application handles:

* Invalid user inputs
* Missing parameters
* API errors
* Network failures

---

## 📌 Assumptions

* Only supports USDT-M Futures Testnet
* User provides correct symbol (e.g., BTCUSDT)
* Quantity and price follow Binance rules

---

## 🎯 Evaluation Highlights

This project demonstrates:

* Clean modular code structure
* Proper use of external APIs
* Logging and debugging practices
* CLI-based interaction
* Error handling

---

## 📎 Notes

* This project uses **Binance Futures Testnet**, so no real funds are involved
* Designed for learning and demonstration purposes

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/AlokMishra594

---
