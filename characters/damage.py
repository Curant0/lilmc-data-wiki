import csv
import json
from pathlib import Path

def update_data(name: str, pd: str, md: str):
    # Obtain a file matching the pattern, excuse the poor readbility.
    char_file = list(Path(".").glob(f"*{name.lower()}.json"))[0]
    with open(char_file, 'r') as file:
        char_data = json.load(file)

    char_data["attributes"]["pd"] = int(pd)
    char_data["attributes"]["md"] = int(md)

    with open(char_file, 'w') as file:
        json.dump(char_data, file, indent=2)


with open('damage.csv', 'r') as file:
    table = csv.reader(file)

    for row in table:
        # print(row[0], row[2], row[3])
        update_data(row[0], row[2], row[3])
        
