discount=0.1
total_cost=0
while total_cost >=0:
    total_item=int(input("Total number of item(s): "))
    for item in range(total_item):
        item_price=float(input("Enter the price of the item: "))
        total_cost= total_cost+item_price

    if total_cost >100:
        price=total_cost*discount
        print(f"Total price for {total_item} is {total_cost-price}")
        break
    else:
        print(f"Total price for {total_item} is {total_cost}")
        break