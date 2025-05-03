from colorama import Fore, Back, Style
import json
import os

print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} CWD: {os.getcwd()}")

try:
    with open('/user_data/backtest_results/backtest-result.json', 'r') as f:
        data = json.load(f)
    print(data.keys())
except FileNotFoundError:
    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} file does not exist")
except:
    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} unexpected error has occured")