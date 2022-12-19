import requests
import random

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
]


def get_headers():
    headers = {'Connection': 'keep-alive',
               'Cache-Control': 'max-age=0',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': random.choice(user_agent_list),
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
               'referer': 'bing.com'}
    return headers


def get_quote(symbol):
    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=" + symbol
    response = requests.get(url, headers=get_headers())
    if response.status_code == 403:
        return "Invalid Headers!"
    elif response.status_code == 404:
        return "Invalid Symbol!"
    else:
        return consolidateinfo(response.json())


def consolidateinfo(jsoninfo):
    quote = jsoninfo['quoteResponse']['result'][0]
    return {
        'symbol': quote['symbol'],
        'regularMarketPrice': quote['regularMarketPrice'],
        'regularMarketChange': quote['regularMarketChange'],
        'regularMarketChangePercent': quote['regularMarketChangePercent'],
        'regularMarketTime': quote['regularMarketTime'],
        'regularMarketDayHigh': quote['regularMarketDayHigh'],
        'regularMarketDayLow': quote['regularMarketDayLow'],
        'regularMarketVolume': quote['regularMarketVolume'],
        'fiftyTwoWeekHigh': quote['fiftyTwoWeekHigh'],
        'fiftyTwoWeekLow': quote['fiftyTwoWeekLow'],
        'fiftyDayAverage': quote['fiftyDayAverage'],
        'twoHundredDayAverage': quote['twoHundredDayAverage'],
        'averageDailyVolume10Day': quote['averageDailyVolume10Day'],
        'averageDailyVolume3Month': quote['averageDailyVolume3Month'],
        'marketCap': quote['marketCap'],
        'trailingPE': quote['trailingPE'],
        'forwardPE': quote['forwardPE'],
        'priceToBook': quote['priceToBook'],
        'fiftyTwoWeekHighChange': quote['fiftyTwoWeekHighChange'],
        'fiftyTwoWeekHighChangePercent': quote['fiftyTwoWeekHighChangePercent'],
        'fiftyTwoWeekLowChange': quote['fiftyTwoWeekLowChange'],
        'fiftyTwoWeekLowChangePercent': quote['fiftyTwoWeekLowChangePercent'],
        'fiftyDayAverageChange': quote['fiftyDayAverageChange'],
        'fiftyDayAverageChangePercent': quote['fiftyDayAverageChangePercent'],
        'twoHundredDayAverageChange': quote['twoHundredDayAverageChange'],
        'twoHundredDayAverageChangePercent': quote['twoHundredDayAverageChangePercent'],
        'exchange': quote['exchange'],
        'currency': quote['currency'],
        'shortName': quote['shortName'],
        'longName': quote['longName'],
        'messageBoardId': quote['messageBoardId'],
        'exchangeTimezoneName': quote['exchangeTimezoneName'],
        'exchangeTimezoneShortName: ': quote['exchangeTimezoneShortName'],
    }

