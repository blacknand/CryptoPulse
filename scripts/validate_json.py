from colorama import Fore, Back, Style
import json
import os

print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} CWD: {os.getcwd()}")

try:
    with open('user_data/backtest_results/backtest-result.json', 'r') as f:
        data = json.load(f)
    print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} JSON is valid. Keys: {data.keys()}")
except FileNotFoundError:
    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} File user_data/backtest_results/backtest-result.json does not exist")
except json.JSONDecodeError:
    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} File contains invalid JSON")
except Exception as e:
    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Unexpected error: {str(e)}")