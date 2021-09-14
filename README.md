# Gecko

**Analyze Price data for blockchain companies with the CoinGecko API using the PyCoinGecko library**

![Gecko System Flowchart](/images/flowChart.png) 

1. Create environment and install dependencies
    * >> python3 -m venv geckoEnv
    * >> source geckoEnv/bin/activate
    * >> pip install -r req.txt
3. Launch virtual environment
>> source geckoEnv/bin/activate
4. Run [main.sh](main.sh)
    * Executes [fetchGecko.py](fetchGecko.py) && [sampleStats.py](sampleStats.py) && [sma.py](sma.py)
5. Visualize data with a PyQt5 GUI using matplotlib with [plot.py](plot.py)
![Plot.py Screenshot](/images/plotScreenshot.png) 
