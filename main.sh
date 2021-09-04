#!/bin/bash


/usr/bin/python3 fetchGecko.py && echo && echo 'Success fetching Coin Gecko Data' && /usr/bin/python3 analyze.py
