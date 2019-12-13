from pprint import pprint 
from kiteconnect import KiteTicker
import pandas as pd
from flask import Flask, render_template, request
import logging
import json
from kiteconnect import KiteConnect

PORT = 5010
HOST = "127.0.0.1"

logging.basicConfig(level=logging.DEBUG)

kite_api_key = open('secret/api_key.txt','r').read()
access_token= open('secret/access_token.txt','r').read()

kite_api_secret = open('secret/api_secret.txt','r').read()
kite = KiteConnect(api_key=kite_api_key)
kite.set_access_token(open('secret/access_token.txt','r').read())


kws = KiteTicker(kite_api_key, access_token)

trd_portfolio = {55016455:"CRUDEOIL19DECFUT",54568199: "SILVER19DECFUT",54568455:"GOLD19DECFUT"}

def on_ticks(ws, ticks): 
    for single_company in ticks:
        
        last_price =single_company['last_price']
        inst_of_single_company = single_company['instrument_token']
        time=single_company['last_trade_time']
        name = trd_portfolio[inst_of_single_company]
        print(last_price,name,time)
        print("\n")
        print(ticks)
    print("\n")



inst_token = [55016455, 54568199,54568455]
def on_connect(ws, response): 
    ws.subscribe(inst_token)
    ws.set_mode(ws. MODE_FULL, inst_token)




kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.connect()