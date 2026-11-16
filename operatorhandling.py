
field1 = 43
field2 = 65
field3 = 25
field4 = 78
field5 = 89

sum_fields = field1 + field2 + field3 + field4 + field5
average = sum_fields / 5

print(f'Total harvest: {sum_fields}\nAverage harvest: {average}')

price_per_kg = 15

total_price = price_per_kg * sum_fields
print(f'Total price: Rs.{total_price}')

bags = sum_fields // 25
leftovers = sum_fields % 25

print(f'Full bags packed: {bags}\nLeftover grains: {leftovers}')

last_year = 500

print(f'Better than last year: {sum_fields > last_year}\nWorse than last year: {sum_fields < last_year}\nEqual to last year: {sum_fields == last_year}\nAt least as good as last year?: {sum_fields >= last_year}')