
# CryptoPulse

**CryptoPulse** is an automated cryptocurrency trading bot that leverages machine learning to predict price movements and execute trades in real-time. Built on the [Freqtrade](https://www.freqtrade.io/) framework, it supports backtesting and live trading, making it ideal for both strategy development and real-world deployment. The initial version focuses on the BTC/USD trading pair, with plans for future expansion.

## Features
- **Machine Learning Predictions**: Employs a Random Forest model for price forecasting, with GPU-accelerated training support.
- **Customizable Strategies**: Easily modify trading logic via the Freqtrade strategy interface.
- **Backtesting**: Test strategies on historical data to evaluate performance.
- **Live Trading**: Deploy the bot on supported exchanges using API keys.
- **Extensible Design**: Built to support additional models, indicators, and trading pairs.

## Installation

### Prerequisites
- Python 3.8 or higher
- Git
- An exchange account with API keys (e.g., Binance)
- (Optional) NVIDIA GPU for faster model training

### Steps
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/CryptoPulse.git
   cd CryptoPulse
   ```

2. **Install Freqtrade**  
   ```bash
   pip install freqtrade
   ```

3. **Install Dependencies**  
   ```bash
   pip install scikit-learn tensorflow pandas numpy
   ```

4. **Configure Freqtrade**  
   - Copy `config.json.example` to `config.json`.
   - Add your exchange API keys and adjust settings as needed (see [Freqtrade docs](https://www.freqtrade.io/en/stable/configuration/)).

## Usage

### Backtesting a Strategy
Run a backtest to evaluate the bot’s performance on historical data:  
```bash
freqtrade backtesting --strategy MLStrategy
```

### Live Trading
Deploy the bot for real-time trading:  
```bash
freqtrade trade --strategy MLStrategy
```

### Customizing the Strategy
The machine learning strategy is defined in `user_data/strategies/MLStrategy.py`. Modify this file to tweak the Random Forest model or add new features.

## Technologies Used
- **Python**: Core language for development.
- **Freqtrade**: Framework for trading logic and exchange integration.
- **scikit-learn**: Implements the Random Forest model.
- **TensorFlow**: Enables GPU-accelerated training and future LSTM integration.
- **Pandas & NumPy**: Handles data processing and analysis.

## Project Structure
```
CryptoPulse/
├── config.json             # Freqtrade configuration
├── user_data/
│   ├── strategies/
│   │   └── MLStrategy.py   # Machine learning strategy
│   └── data/               # Historical data (downloaded by Freqtrade)
├── README.md               # Project documentation
└── roadmap.md              # Future development plans
```

## Contributing
This is a portfolio project, but contributions are welcome! Fork the repo, make improvements, and submit a pull request.

## License
MIT License
