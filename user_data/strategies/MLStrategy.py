from freqtrade.strategy import IStrategy
import pandas as pd
import numpy as np

class MLStrategy(IStrategy):
    INTERFACE_VERSION = 3
    minimal_roi = {"0": 0.01}  # 1% ROI
    stoploss = -0.05  # 5% stop-loss
    timeframe = "1h"

    def __init__(self, config: dict):
        super().__init__(config)
        print("MLStrategy initialized with config")

    def populate_indicators(self, dataframe: pd.DataFrame, metadata: dict) -> pd.DataFrame:
        print(f"Populating indicators for {metadata['pair']}")
        dataframe['ma7'] = dataframe['close'].rolling(window=7).mean()
        dataframe['ma21'] = dataframe['close'].rolling(window=21).mean()
        dataframe['rsi'] = self.calculate_rsi(dataframe['close'], 14)
        print(f"Indicators added. Dataframe shape: {dataframe.shape}")
        return dataframe

    def calculate_rsi(self, prices: pd.Series, period: int) -> pd.Series:
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def populate_entry_trend(self, dataframe: pd.DataFrame, metadata: dict) -> pd.DataFrame:
        print(f"Populating entry trend for {metadata['pair']}")
        # Simple entry: Buy when close > MA7 and RSI < 30
        dataframe['enter_long'] = np.where(
            (dataframe['close'] > dataframe['ma7']) & (dataframe['rsi'] < 30),
            1,
            0
        )
        print(f"Entry signals: {dataframe['enter_long'].sum()}")
        return dataframe

    def populate_exit_trend(self, dataframe: pd.DataFrame, metadata: dict) -> pd.DataFrame:
        print(f"Populating exit trend for {metadata['pair']}")
        # Exit when close < MA7 or RSI > 70
        dataframe['exit_long'] = np.where(
            (dataframe['close'] < dataframe['ma7']) | (dataframe['rsi'] > 70),
            1,
            0
        )
        return dataframe