import requests
import json
import builtins
import json
import requests


class SleeperAPI:
    def __init__(self, league_id=None, league_name=None):
        self.base_url = 'https://api.sleeper.app/v1'
        self.league_name = league_name
        self.league_id = league_id  # Ensure league_id is set properly when the object is instantiated

    def get_data(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        res = requests.get(url)
        data = res.json() if res.status_code == 200 else None  # Make sure we handle bad responses

        if res.status_code == 200:
            return data
        else:
            print(f"Failed to fetch data from {url}. Status code: {res.status_code}")
            return None

    # def get_league_data(self):
    #     if self.league_id is None:
    #         print("League ID is not set.")
    #         return None
    #
    #     print(f"Fetching league data for League ID: {self.league_id}")
    #     return self.get_data(f'league/{self.league_id}')  # Fetch league data using the league_id
    #
    # def get_rosters(self):
    #     if self.league_id is None:
    #         print("League ID is not set.")
    #         return None
    #
    #     print(f"Fetching rosters for League ID: {self.league_id}")
    #     print(f"Writing league to file....")
    #
    #     self.write_to_file(self.get_data(f'league/{self.league_id}/rosters'), self.league_name )
    #     return self.get_data(f'league/{self.league_id}/rosters')  # Fetch rosters using the league_id
    #

