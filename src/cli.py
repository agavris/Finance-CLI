import data
import random
from colorama import Fore, Style

arr = []

for i in range(1, 14):
    d = dir(Fore)
    arr.append("Fore." + d[i])

#print(arr)


def price(symbol):
    change = data.get_quote(symbol)['regularMarketChange']
    if change > 0:
        return f"Price: {Fore.WHITE}{data.get_quote(symbol)['regularMarketPrice']}{Style.RESET_ALL} | Change: {Fore.GREEN}{change}{Style.RESET_ALL} "
    elif change < 0:
        return f"Price: {Fore.WHITE}{data.get_quote(symbol)['regularMarketPrice']}{Style.RESET_ALL} | Change: {Fore.RED}{change}{Style.RESET_ALL} "
    else:
        return f"Price: {Fore.WHITE}{data.get_quote(symbol)['regularMarketPrice']}{Style.RESET_ALL} | Change: {Fore.YELLOW}{change}{Style.RESET_ALL} "


def companyInfo(symbol):
    listedInfo = {"regularMarketVolume": "Volume", "marketCap": "Market Cap", "trailingPE": "Trailing PE",
                  "forwardPE": "Forward PE", "priceToBook": "Price To Book", "exchange": "Exchange", "longName": "Name"}
    for k, v in listedInfo.items():
        print(f"{eval(random.choice(arr))}{v}: {data.get_quote(symbol)[k]}{Style.RESET_ALL}")


def marketInfo(symbol):
    listedInfo = {"regularMarketPrice": "Price", "regularMarketChange": "Change", "regularMarketChangePercent": "Change Percent",
                  "regularMarketTime": "Time", "regularMarketDayHigh": "Day High", "regularMarketDayLow": "Day Low", "regularMarketVolume": "Volume",
                  "fiftyTwoWeekHigh": "52 Week High", "fiftyTwoWeekLow": "52 Week Low", "fiftyDayAverage": "50 Day Average", "twoHundredDayAverage": "200 Day Average",
                  "averageDailyVolume10Day": "10 Day Avg Volume", "averageDailyVolume3Month": "3 Month Avg Volume", "marketCap": "Market Cap",
                  "trailingPE": "Trailing PE", "forwardPE": "Forward PE", "priceToBook": "Price To Book",
                  "fiftyTwoWeekHighChange": "52 Week High Change", "fiftyTwoWeekHighChangePercent": "52 Week High Change Percent",
                  "fiftyTwoWeekLowChange": "52 Week Low Change", "fiftyTwoWeekLowChangePercent": "52 Week Low Change Percent",
                  "fiftyDayAverageChange": "50 Day Average Change", "fiftyDayAverageChangePercent": "50 Day Average Change Percent",
                  "twoHundredDayAverageChange": "200 Day Average Change", "twoHundredDayAverageChangePercent": "200 Day Average Change Percent",
                  "exchange": "Exchange", "currency": "Currency", "shortName": "Short Name", "longName": "Long Name", "messageBoardId": "Message Board ID"}
    for k, v in listedInfo.items():
        print(f"{eval(random.choice(arr))}{v}: {data.get_quote(symbol)[k]}{Style.RESET_ALL}")