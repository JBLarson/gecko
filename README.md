# Gecko

**Analyze Price data for blockchain companies with the CoinGecko API using the PyCoinGecko library**

1. Create environment and install dependencies
    * >> python3 -m venv geckoEnv
    * >> source geckoEnv/bin/activate
    * >> pip install -r req.txt
2. Run [main.sh](main.sh)
    * Executes [fetchGecko.py](fetchGecko.py) && [sampleStats.py](sampleStats.py) && [sma.py](sma.py)
3. Visualize data with a PyQt5 GUI using matplotlib with [plot.py](plot.py)
![Plot.py Screenshot](/images/plotScreenshot.png) 

Correlation Coefficient Example

>>CorrCoef Example
> Started Correlation Coefficient Script on: 09/26/21 at: 16:15:19

> Currency Pair: AdaUsd Corr Coefs: {'btc': 0.694055, 'eth': 0.939808}
> Currency Pair: AdaEur Corr Coefs: {'btc': 0.700659, 'eth': 0.9416}
> Currency Pair: BtcUsd Corr Coefs: {'btc': 1.0, 'eth': 0.757446}
> Currency Pair: BtcEur Corr Coefs: {'btc': 1.0, 'eth': 0.7599}
> Currency Pair: EthUsd Corr Coefs: {'btc': 0.757446, 'eth': 1.0}
> Currency Pair: EthEur Corr Coefs: {'btc': 0.7599, 'eth': 1.0}
> Currency Pair: LinkUsd Corr Coefs: {'btc': 0.880485, 'eth': 0.789894}
> Currency Pair: LinkEur Corr Coefs: {'btc': 0.880813, 'eth': 0.789465}
> Currency Pair: DaiUsd Corr Coefs: {'btc': -0.505491, 'eth': -0.466145}
> Currency Pair: DaiEur Corr Coefs: {'btc': -0.220097, 'eth': -0.081494}

> Completed Correlation Coefficient Script on: 09/26/21 at: 16:15:19

