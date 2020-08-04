

import requests  
from bs4 import BeautifulSoup
from datetime import datetime

prices = []
times = []

def get_price(stock):
    url = f'https://de.finance.yahoo.com/quote/{stock}?p={stock}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    try: 
        price = soup.find('span', {'class': "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
        get_price.lastprice = price
        return price
    except:
        if not 'get_price.lastprice' in locals(): 
            get_price.lastprice = 0
        return get_price.lastprice