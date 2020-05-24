# TickerBot

### A bot that interacts with stock tickers through yfinance
#### requirements
 - discord==1.0.1
 - yfinance==0.1.5
 - lxml==4.5.1
 
## functionality
### ticker information and commands
#### General and Summary Information
> $info GOOG, $summary GOOG
```
Symbol: GOOG
Name: Alphabet Inc.
Sector: Communication Services
Market Cap: 964157571072
Full Time Employees: 123048
Summary: Alphabet Inc. provides online advertising services in the United States, Europe, the Middle East, Africa, the Asia-Pacific, Canada, and Latin America. It offers performance and brand advertising services. The company operates through Google and Other Bets segments. The Google segment offers products, such as Ads, Android, Chrome, Google Cloud, Google Maps, Google Play, Hardware, Search, and YouTube, as well as technical infrastructure. It also offers digital content, cloud services, hardware devices, and other miscellaneous products and services. The Other Bets segment includes businesses, including Access, Calico, CapitalG, GV, Verily, Waymo, and X, as well as Internet and television services. Alphabet Inc. was founded in 1998 and is headquartered in Mountain View, California.
Denominated in: USD
```


> $price GOOG, $price-info goog, $info-price GoOg
```
Daily High: 1412.76
Daily Low: 1392.02
Last Close: 1402.8
Last Open: 1396.71
52 Week High: 1532.106
52 Week Low: 1013.536
```


> $volume AAPL
```
Market Volume: 20450754
10 Day Average Volume: 30653414
Average Volume: 51660098
```


> $pe AAPL, $price-earnings AAPL
```
Forward PE: 21.649017
Trailing PE: 25.054213
PEG Ratio: 2.05
```


#### Historic series
>$price-history SPY, $7day SPY, $weekly SPY, $week spy, $hist SpY
```
7 Day Price History for $SpY
Date               High               Low                Open               Close
2020-05-22         295.63             293.22             294.57             295.44
2020-05-21         297.67             293.69             296.79             294.88
2020-05-20         297.87             295.57             295.82             296.93
2020-05-19         296.21             291.95             294.35             291.97
2020-05-18         296.75             292.7              293.05             295.0
2020-05-15         286.33             281.34             282.37             286.28
2020-05-14         285.11             272.99             278.95             284.97
```


#### Upcoming Earnings
##### this data is kinda sus
>$earning AAPL, $calendar AAPL, $earnings AAPL
```
Upcoming Earnings for $AAPL
Upcoming Earnings Call: 2020-08-03
```

## TODO
Options & option chains
