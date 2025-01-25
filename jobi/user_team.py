from jobi.sleeper_api import SleeperAPI



class UserTeam:
    def __init__(self, league_id, league_users: list, sleeper_api: SleeperAPI):
        self.league_id = league_id
        self.sleeper_api = sleeper_api
        self.league_users = league_users
        self.ep = f'/league/{self.league_id}/users'

    def get_users_in_league(self, user_id):
        users = self.sleeper_api.get_data(self.ep)
        for user in users:
            for key, val in user.items():
                if key == 'display_name':
                    display_name = val
                elif key == 'metadata':
                    team_name = val.get('team_name')
                elif key == 'user_id':
                    user_id = val
        # print(users)
        return users

    def get_user(self, team_id):
        for user in self.league_users:
            if user["team_id"] == team_id:
                print(user['user_id'])
                return user["user_id"]
