from freqtrade.strategy import IStrategy
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

class MLStrategy(IStrategy):
    INTERFACE_VERSION = 3
    minimal_roi = {"0": 0.01}  # 1% ROI
    stoploss = -0.05  # 5% stop-loss
    timeframe = "1h"

    def populate_indicators(self, dataframe: pd.DataFrame, metadata: dict) -> pd.DataFrame:
        # Add technical indicators
        dataframe['ma7'] = dataframe['close'].rolling(window=7).mean()
        dataframe['ma21'] = dataframe['close'].rolling(window=21).mean()
        dataframe['rsi'] = self.calculate_rsi(dataframe['close'], 14)
        return dataframe

    def calculate_rsi(self, prices: pd.Series, period: int) -> pd.Series:
        # Calculate RSI over a 14 period window
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        # Forumla = RSI = 100 - (100 / (1 + RS)) where RS = (Average Gain / Average Loss)
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    # Generate buy signals usign Random Forest
    def populate_entry_trend(self, dataframe: pd.DataFrame, metadata: dict) -> pd.DataFrame:
        # Prepare features and target
        features = dataframe[['open', 'high', 'low', 'close', 'ma7', 'ma21', 'rsi']].dropna()
        if len(features) < 50:  # Ensure enough data
            dataframe['enter_long'] = 0
            return dataframe

        # Align X and y using the features dataframe
        X = features[['open', 'high', 'low', 'close', 'ma7', 'ma21', 'rsi']].values[:-1]
        y = (features['close'].shift(-1) > features['close']).astype(int).values[:-1]
        
        if len(X) > 10:
            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X, y)
            prediction = model.predict([features.values[-1]])[0]
            dataframe.loc[dataframe.index[-1], 'enter_long'] = 1 if prediction == 1 else 0
        else:
            dataframe['enter_long'] = 0

        return dataframe

    def populate_exit_trend(self, dataframe: pd.DataFrame, metadata: dict) -> pd.DataFrame:
        # Exit if price drops below MA7
        dataframe['exit_long'] = np.where(dataframe['close'] < dataframe['ma7'], 1, 0)
        return dataframe