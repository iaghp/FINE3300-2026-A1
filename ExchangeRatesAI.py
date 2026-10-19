import csv
import sys

class ExchangeRates:
    def __init__(self, filename):
        with open(filename, newline="") as f:
            rows = list(csv.DictReader(f))
        # Last row holds the latest rate: 1 USD = usd_cad CAD
        self.usd_cad = float(rows[-1]["FXAUSDCAD"])

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        if from_currency == "USD":
            return amount * self.usd_cad
        return amount / self.usd_cad

def main():
    rates = ExchangeRates(sys.argv[1] if len(sys.argv) > 1 else "BankOfCanadaExchangeRate.2026.csv")
    amount = float(input("Enter the amount: "))
    from_currency = input("Convert from (USD or CAD): ").strip().upper()
    to_currency = input("Convert to (USD or CAD): ").strip().upper()
    result = rates.convert(amount, from_currency, to_currency)
    print(f"${amount:,.2f} {from_currency} = ${result:,.2f} {to_currency}")


if __name__ == "__main__":
    main()