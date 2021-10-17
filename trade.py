from kiteconnect import KiteConnect

api_key=open('secret/api_key.txt','r').read()
api_secret=open('secret/api_secret.txt','r').read()


kite = KiteConnect(api_key=api_key)
kite.set_access_token(open('secret/access_token.txt','r').read())

def order():
    orderid=kite.place_order(tradingsymbol = "INFY", 
                            quantity = "1", 
                            exchange = "NSE", 
                            transaction_type = "BUY", 
                            order_type = "MARKET", 
                            product = "CNC", 
                            validity = "DAY", 
                            variety = "regular")
    print(orderid)
order()

Lastprice=kite.ltp('NSE:INFY')
    
print(Lastprice)
