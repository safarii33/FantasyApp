import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get('api_key_sports')

base_url = "https://api.sportradar.com/nfl/official/trial/v7/en"

# Endpoint to get all players in the league
url = f"{base_url}/league/hierarchy.json"

response = requests.get(url, params={"api_key": api_key})

if response.status_code == 200:
    data = response.json()

    # Create a structured output
    leagues_data = []

    # Extracting teams in "AFC West"
    afc_west_teams = []
    for conference in data['conferences']:
        if conference['name'] == 'AFC':
            for division in conference['divisions']:
                if division['name'] == 'AFC West':
                    afc_west_teams = division['teams']
                    break

    # Print each team's name, market, and venue
    for team in afc_west_teams:
        print(f"Team: {team['name']}, Market: {team['market']}")
        print(f"Venue: {team['venue']['name']}, Location: {team['venue']['city']}, {team['venue']['state']}")
        print(f"Colors: {', '.join([color['hex_color'] for color in team['team_colors']])}")
        print('-' * 40)

    # Write to a JSON file
    with open("nfl_hierarchy.json", "w") as file:
        json.dump(leagues_data, file, indent=4)
else:
    print(f"Error: {response.status_code}, {response.text}")
