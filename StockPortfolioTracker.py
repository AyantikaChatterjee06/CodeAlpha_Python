import csv
prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 415,
        "NVDA": 875,
}
print("=== STOCK PORTFOLIO TRACKER ===")
print("Stocks:",",".join(prices.keys()))
print()
total=0
portfolio_list=[]
while True:
    symbol=input("Enter stock (or 'done'): ").upper()
    if symbol == "DONE":
        break
    if symbol not in prices:
        print("Stock not found. Try again.")
        continue
    qty=int(input(f"Quantity of {symbol}: "))
    value = prices[symbol] * qty
    total += value
    print(f" {symbol} x {qty} = ${value}\n")
    portfolio_list.append({
    "Symbol": symbol,
    "Price": prices[symbol],
    "Quantity": qty,
    "Total Value": value
    })
print(f"\nTotal Investment: ${total}")
with open ("portfolio.csv",mode="w",newline="") as file:
    fieldnames = ["Symbol", "Price", "Quantity", "Total Value"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for item in portfolio_list:
        writer.writerow(item)
    writer.writerow({"Symbol":"TOTAL INVESTMENT","Price": "","Quantity": "","Total Value": total})
print("Portfolio saved successfully to 'portfolio.csv'!")
