# TickerBot

### A bot that interacts with stock tickers through yfinance
#### requirements
 - discord==1.0.1
 - yfinance==0.1.5

## functionality

#### ticker information
- summary info; ex - $info GOOG, $summary GOOG
- - - ```Symbol: GOOG
Name: Alphabet Inc.
Sector: Communication Services
Market Cap: 964157571072
Full Time Employees: 123048
Summary: Alphabet Inc. provides online advertising services in the United States, Europe, the Middle East, Africa, the Asia-Pacific, Canada, and Latin America. It offers performance and brand advertising services. The company operates through Google and Other Bets segments. The Google segment offers products, such as Ads, Android, Chrome, Google Cloud, Google Maps, Google Play, Hardware, Search, and YouTube, as well as technical infrastructure. It also offers digital content, cloud services, hardware devices, and other miscellaneous products and services. The Other Bets segment includes businesses, including Access, Calico, CapitalG, GV, Verily, Waymo, and X, as well as Internet and television services. Alphabet Inc. was founded in 1998 and is headquartered in Mountain View, California.
Denominated in: USD
```
- Volume
- Last Close price
- has options

#### options
- delta; the rate of change between the options price and $1 change in underlying asset price
- theta; rate of change between the option price and time
- gamma; rate of change between delta and underlying asset price
- vega; rate of change between options value and underlying assets iv
- rho; rate of change between and options value and a 1% change in the interest rate
