# PulseStrategy
An automated trading bot built upon `freqtrade` using ML algorithims to execute a simple trading strategy.


## Setup
- The strategy is in `user_data/strategies`
- The Python scripts are inside `scripts`


## Configuring the bot
- You will need to generate a config file using:


```bash
freqtrade new-config --config user_data/config.json
```


## Running the bot


```bash
freqtrade trade --config user_data/config.json --strategy PulseStrategy
```


## Requirements
- TA-Lib:


On macOS:


```bash
brew install ta-lib
```


On Linux:


```bash
sudo apt-get && sudo apt-get install -y build-essential talib
```


- > Python 3.11
- Create and setup a virtual enviroment using:


```bash
python3 -m venv env
source env/bin/activate
```

- Install the following dependencies *in* the virtual enviroment:


```bash
pip install freqtrade matplotlib pandas scikit-learn numpy  
```