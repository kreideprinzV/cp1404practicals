min_bonus=0.1
max_bonus=0.15
sales= float(input("Enter Sales: $"))
while sales>0:
    if sales >= 1000:
        bonus=max_bonus
    elif sales < 1000:
        bonus=min_bonus
    else:
        break
    print(f"You get {bonus*100}% bonus and you will received {sales+(sales*bonus)}" )
    sales = float(input("Enter Sales: $"))