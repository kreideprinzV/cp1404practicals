year = 1922
brand = "Gibson"
model = "L-5 CES"
price = 16035.0

output_string = f"{year} {brand} {model} for about ${price:,.2f}!"
print(output_string)

for i in range(0, 201, 50):
    print(f"{i:>3}")
