from forex_python.converter import CurrencyRates

def CurrencyRates():
    dolars= ['AUDUSD=0.8371', 
    'CADUSD=0.8711',
    'USDCNY=6.1715', 
    'EURUSD=1.2315', 
    'GBPUSD=1.5683', 
    'NZDUSD=0.7750', 
    'USDJPY=119.95', 
    'EURCZK=27.6028',
    'EURDKK=7.4405', 
    'EURNOK=8.6651',
    'USDEUR=0.9256'
    ]
    return dolars

def convert_currency(amount, from_currency, to_currency):
    currency_converters = from_currency + to_currency
    currency_rates = CurrencyRates()
    for x in currency_rates:
        dollar_from_to = x[:6]
        if currency_converters in dollar_from_to:
            dollar_values = x.split("=")[1]
            print("Exchange Rate:",float(dollar_values))
            val = float(dollar_values)
            int(val)
            converted_amount = int(amount) * int(val)
            print(converted_amount)
            return converted_amount

amount = input("Amount:")
from_currency = input("Dollar_Currency_You_Have:")
to_currency = input("Dollar_Currency_You_Need_To_Convert:")

converted_amount = convert_currency(amount, from_currency, to_currency)
print(converted_amount)

