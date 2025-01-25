class FootballAPI:
    def __init__(self, route, season):
        self.base_url = "https://api.sportradar.com/nfl/official/trial/v7/en"
        self.season = season
    def get_nfl_data(self, ep):
        url = f'self.base_url{ep}'
    def get_stats(self, ep):
        # url = f"{self.base_url}/seasons/{self.season}/REG/players/{PLAYER_ID}/statistics.json"
        pass
