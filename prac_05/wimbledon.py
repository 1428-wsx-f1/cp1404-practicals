"""
Word Occurrences
Estimate: 120 minutes
Actual:   234 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    data = retrieve_records(FILENAME)
    championships_to_count, countries = process_records(data)
    display_records(championships_to_count, countries)


def retrieve_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            csv_part = line.strip().split(",")
            records.append(csv_part)

    return records


def process_records(data):
    championships_to_count = {}
    countries = set()
    for datum in data:
        countries.add(datum[1])
        try:
            championships_to_count[datum[2]] += 1
        except KeyError:
            championships_to_count[datum[2]] = 1

    return championships_to_count, countries


def display_records(championships_to_count, countries):
    max_name_length = max(len(name) for name in championships_to_count)
    print("Wimbledon Champions: ")
    for name, wins in championships_to_count.items():
        print(f"{name:{max_name_length}} = {wins}")
    print(f"\nThese {len(countries)} have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
