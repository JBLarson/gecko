# Gecko

## Analyze daily prices and 7, 30, 50, and 200-day moving averages
## For BTC, ETH, KAVA, XMR, ATOM, and DAI
#### Data provided by the CoinGecko API using the PyCoinGecko library

1. Create environment and install dependencies
    * >> python3 -m venv geckoEnv
    * >> source geckoEnv/bin/activate
    * >> pip install -r req.txt


2. Run [main.sh](main.sh)
    * Executes [fetchGecko.py](fetchGecko.py) && [movingAvgs.py](movingAvgs.py)


3. Visualize data with a PyQt5 GUI using matplotlib with [plot.py](plot.py)
   * >> Select a date range to analyze
   * >> ![plot.py screenshot 1](/images/dateRange.png)
   * >> Use the simple GUI to choose which pair you want to view
   * >> ![plot.py screenshot 2](/images/gui.png)
   * >> Try to recognize trends between price and various moving averages
   * >> Moving the mouse around the chart show's different dates / prices
   * >> The dates on the X-axis clearly need work
   * >> ![plot.py screenshot 3](/images/kavaChart.png)


## Work in progress: analyzing correlation coefficient

Create and analyze correlation coefficient data with [correlation.py](correlation.py)

#### More to come!
