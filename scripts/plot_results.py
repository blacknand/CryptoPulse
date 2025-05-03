import pandas as pd
import matplotlib.pyplot as plt

def plot_backtest_results(backtest_file: str):
    # Load backtest results (adjust path as needed)
    df = pd.read_json(backtest_file)
    df['cum_profit'] = df['profit_abs'].cumsum()
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['close_time'], df['cum_profit'], label='Cumulative Profit')
    plt.title('CryptoPulse Backtest Results')
    plt.xlabel('Date')
    plt.ylabel('Profit (USDT)')
    plt.legend()
    plt.grid(True)
    plt.savefig('backtest_results.png')

if __name__ == "__main__":
    plot_backtest_results('user_data/backtest_results/backtest-result.json')