from jobi.football_api import FootballAPI


class Team:
    def __init__(self):
        self.ep = '/league/hierarchy.json'

    def get_team_by_name(self):
        pass

    def get_teams_in_div(self, division, data):
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