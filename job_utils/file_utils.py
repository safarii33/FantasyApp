import json
import os

def write_to_file(data, filename, category):
    directory = os.path.join('Dynasty Football Leagues', 'League_Name', category)
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data written to {filepath}")
