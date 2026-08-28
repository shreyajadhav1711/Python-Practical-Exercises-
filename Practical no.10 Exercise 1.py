prices = [2500.50, 1200.75, 5000.25, 3200.00, 1800.50]

prices.sort(reverse=True)

print("Prices from highest to lowest:", prices)
print("Top 3 Priciest Entries:")

for price in prices[:3]:
    print(price)
