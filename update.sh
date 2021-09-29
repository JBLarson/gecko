#!/bin/bash

/usr/bin/python3 updateGecko.py && echo 'Updated gecko data' && echo && /usr/bin/python3 smaUpdate.py && echo 'Updated moving avgs' && echo

