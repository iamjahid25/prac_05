"""
Wimbledon
Estimate: 60 minutes
Actual:   123 minutes
"""


FILENAME = "wimbledon.csv"

def main():
    records = read_wimbledon_data(FILENAME)
    champions_to_wins = count_champions(records)
    countries = get_unique_countries(records)

    print("Wimbledon Champions:")
    display_champions(champions_to_wins)

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def read_wimbledon_data(filename):
    """Get data from the CSV file and display it as a list of records."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # skip header
        records = [line.strip().split(',') for line in in_file]
    return records


def count_champions(records):
    """Figure out how many times each champion has won and put the results in a dictionary."""
    champion_to_wins = {}
    for record in records:
        champion = record[2]
        if champion in champion_to_wins:
            champion_to_wins[champion] += 1
        else:
            champion_to_wins[champion] = 1
    return champion_to_wins

def get_unique_countries(records):
    """Return a set of unique countries from the records."""
    return {record[1] for record in records}

def display_champions(champion_to_wins):
    """Display each champion and how many times they have won."""
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")


main()
