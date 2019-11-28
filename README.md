# Ecoin-Scrapper
This is a cryptocurrency scrapper. It works by taking the data of different websites (eg. binance) through the ccxt library. It automatically calculates delays to take as many as possible data without causing a rejection from the target website. It then stores those timeseries data into a database controlled through sqlite3.

Libraries:matlibplot,ccxt,

Special Libraries: python-binance (needs installation of this:http://landinghub.visualstudio.com/visual-cpp-build-tools )


## ToDo List:
- [x] Sql Integration for storing of Data.
- [x] Test all the exchanges for Data check.
- [x] Reformat Binance, Unpack, Plot Libraries before pushing.
- [x] Test the integration.
