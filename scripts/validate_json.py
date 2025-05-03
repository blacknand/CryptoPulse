import json
import os

print(f"CWD: {os.getcwd()}")

try:
    with open('/user_data/backtest_results/backtest-result.json', 'r') as f:
        data = json.load(f)
    print(data.keys())
except FileNotFoundError:
    print("File does not exist")
except:
    print("Unexpected error")