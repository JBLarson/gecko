#!/bin/bash


/usr/bin/python3 fetchGecko.py && echo && echo 'Success fetching Coin Gecko Data' && /usr/bin/python3 sampleStats.py && echo && echo 'Success creating sample statistics' && /usr/bin/python3 sma.py && echo && echo 'Success creating Simple Moving Averages' && echo && echo 'Launching Plot.py GUI' && /usr/bin/python3 plot.py &&
