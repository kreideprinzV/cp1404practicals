import csv

def main():
    filename = 'wimbledon.csv'
    data = read_csv_data(filename)
    champions_wins = count_champions_wins(data)
    countries = extract_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in champions_wins.items():
        print(f"{champion} {wins}")

    print("\nThese countries have won Wimbledon:")
    print(', '.join(countries))

def read_csv_data(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header
        data = list(csv_reader)
    return data


def count_champions_wins(data):
    champions = {}
    for row in data:
        champion = row[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def extract_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
    return sorted(countries)



main()
