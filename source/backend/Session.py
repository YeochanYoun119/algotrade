import ccxt
import threading
import time
import pandas as pd

#define exchange locally

exchange = ccxt.binance()
markets = exchange.load_markets()
symbols = exchange.symbols
currencies = exchange.currencies

exchange.apiKey = 'nOK54jyAMTSkrCicsBtqZErob8SORYj3qXjrIull8PSgkSs4dVxSbVz9HIYkpv13'
exchange.secret = '0l93ZNwaAzHaWGSiphrKvFJw0w9BH3nT5NlcLvQbfXotx4tbdOW5sTfqBAbwgON1'

class Session(threading.Thread):

    def __init__(self, session_id, order_queue, initial_investment, currency):
        threading.Thread.__init__(self, daemon= True)
        self.session_id = session_id
        self.order_queue = order_queue
        self.counter = 0
        self.initial_investment = initial_investment
        self.total = initial_investment
        self.totalcoin = 0
        self.totalcash = initial_investment
        self.totalprofit = 0
        self.currency = currency
        self.exitFlag = 0

    def trade_update(self, trade_structure):
        #TODO: calcProfit()

        if(int(trade_structure.session_id) != self.session_id):
            print("wrong match")
        else:
            if(trade_structure.side == "buy"):
                self.totalcoin += trade_structure.amount * trade_structure.price
                self.totalcash -= trade_structure.amount
            elif(trade_structure.side == "sell"):
                self.totalcoin -= trade_structure.amount * trade_structure.price
                self.totalcash += trade_structure.amount
        print("Updated balance")

    def calc_balance(self):
        #calculates the current valuation
        current_balance = 0
        current_balance += self.totalcash
        current_balance += self.totalcoin * self.fetch_price()
        return current_balance
        #return current_balance

    def fetch_price(self):
        #fetches the latest bid price from exchange
        orderbook = exchange.fetch_order_book (self.currency)
        bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
        return bid

    def calc_profit(self):
        #returns profit in percentage
        return (self.calc_balance()-self.initial_investment)/self.initial_investment * 100

    # calc current balance and
    # def calc_profit():

    # fetch current price and calculate current valuation of total
    # def update_balance():