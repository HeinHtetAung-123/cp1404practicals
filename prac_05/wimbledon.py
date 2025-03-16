FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2

def main():
    records = read_wimbledon_data(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count,countries)

def read_wimbledon_data(filename):
    """Reading the data from the file"""
    records = []
    with open(filename, "r", encoding="utf-8") as filename:
        filename.readline()
        for line in filename:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Looking through the file and counting the champions names and winning countries"""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        champion_to_count[record[INDEX_CHAMPION]] = champion_to_count.get(record[INDEX_CHAMPION], 0 )+1
    return champion_to_count,countries


def display_results(champion_to_count, countries):
    """Displaying the results"""
    print("Wimbledon Champions:")
    for name, count in champion_to_count.items():
        print(name,count)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

main()