#!/bin/bash


/usr/bin/python3 fetchGecko.py && echo && echo 'Success fetching Coin Gecko Data and creating sample stats' && /usr/bin/python3 movingAvgs.py && echo && echo 'Success creating Simple Moving Averages' && echo
