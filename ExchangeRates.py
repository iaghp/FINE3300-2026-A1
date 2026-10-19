class ExchangeRates:
    def __init__(self, filename):
        # read the whole Bank of Canada CSV into a list of lines
        with open(filename) as file:
            lines = file.readlines()

        values = lines[-1].split(",") # last row has the most recent rates
        self.rate = float(values[-2]) 
        # second to last column is USD/CAD + Convert the text to a number and store it for later conversions.

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency: # same currency in and out, so nothing to convert
            return amount 
        elif from_currency == "USD" and to_currency == "CAD": # the rate is CAD per 1 USD, so multiply to go USD -> CAD
            return amount * self.rate
        elif from_currency == "CAD" and to_currency == "USD": # and divide to go back the other way
            return amount / self.rate
        # anything else doesnt print anything
        return None

print("----------------------------------------")
print("Welcome to the best currency exchange calculator in the world!")
print("----------------------------------------")

exchange = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

print(f"Current exchange rate from USD to CAD is: {exchange.rate: .2f}")
print(f"Current exchange rate from CAD to USD is: {1/exchange.rate: .2f}")
print("----------------------------------------")

# the code broke on lowercase input, so I put .upper() to turn "usd" into "USD"
from_currency = input("From currency (USD or CAD): ").upper() 
to_currency = input("To currency (USD or CAD): ").upper()
amount = float(input(f"Enter the amount in {from_currency}: "))

result = exchange.convert(amount, from_currency, to_currency)
print(f"${amount:,.2f} {from_currency} equals to ${result:,.2f} {to_currency}")
# :,.2f adds thousands separators and rounds to cents