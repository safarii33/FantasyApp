class LeagueFinder:
    def __init__(self, leagues):
        self.leagues = leagues

        # id_ol = id of league
    def get_league_id(self, id_ol):
        for league in self.leagues:
            if league["ID"] == id_ol:
                return league["LeagueID"]

    def get_league_name(self, id_ol):
        for league in self.leagues:
            if league["ID"] == id_ol:
                return league["Name"]
