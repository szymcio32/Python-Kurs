EURO_EXCHANGE_RATE = 4.29
USD_EXCHANGE_RATE = 3.7

def convertFromPlnToEuro(amount):
    global EURO_EXCHANGE_RATE
    amount_in_eur = amount / EURO_EXCHANGE_RATE
    print(f"Amount in EUR: {amount_in_eur}")
    EURO_EXCHANGE_RATE = 5
    print(f"ID of a object inside the function: {id(EURO_EXCHANGE_RATE)}")

def convertFromPlnToUsd(amount):
    amount_in_usd = amount / USD_EXCHANGE_RATE
    print(f"Amount in USD: {amount_in_usd}")

amount_in_pln = 25

convertFromPlnToEuro(amount_in_pln)
convertFromPlnToUsd(amount_in_pln)

print(f"ID of a object in main program: {id(EURO_EXCHANGE_RATE)}")
print(f"New exchange rate for EUR: {EURO_EXCHANGE_RATE} zl")