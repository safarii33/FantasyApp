from jobi.sleeper_api import SleeperAPI


class Player:
    def __init__(self, league_id):
        self.sleeper_api = SleeperAPI(league_id)

    def get_players(self):
        return self.sleeper_api.get_data(f'league/{self.sleeper_api.league_id}/players')
