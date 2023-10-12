FILENAME = "wimbledon.csv"

def main():
    year_to_info = file_extractor()
    champion_calculator(year_to_info)
    winning_countries(year_to_info)


def file_extractor():
    year_to_info = {}

    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            strip_line = str(line.strip())
            split_data = strip_line.split(",")
            year_to_info[split_data[0]] = split_data[1:]

    # 'Year': ['Country', 'Champion', 'Country', 'Runner-up', 'Score in the final']

    year_to_info.pop("Year")

    return year_to_info

def champion_calculator(year_to_info):
    champions = []
    for year in year_to_info:
        champions.append(year_to_info[year][1])
    champions_to_wins = {str(names): int(champions.count(names)) for names in champions}

    print("Wimbledon Champions:\r")

    for name in champions_to_wins:
        print(f"{name} - {champions_to_wins[name]}")


def winning_countries(year_to_info):
    countries = set()
    for year in year_to_info:
        countries.add(year_to_info[year][0])

    print(f"These {len(countries)} have won Wimbledon:")
    print(", ".join(countries))

main()