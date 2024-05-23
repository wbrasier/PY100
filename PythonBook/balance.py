starting_amount = 1000.00
interest_rate = .05

years = 5

balance = starting_amount
for year in range(years):
  balance += balance * interest_rate

print(balance)

balance = starting_amount * (1.05**years)
print(balance)