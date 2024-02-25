for ten_gap_count in range(0, 101, 10):
    print(ten_gap_count, end=' ')
print()

for inverse_count in range(0, 101, 10):
    print(inverse_count, end=' ')
print()


loops=int(input("Number of stars: "))
for star in range(1,loops+1):
    print("*"*star)
print()