from jobi.sleeper_api import SleeperAPI
from job_utils import file_utils


class Roster:
    def __init__(self, user_id, sleeper_api: SleeperAPI):
        self.user_id = user_id
        self.sleeper_api = sleeper_api
        self.ep = f'/league/{user_id}/rosters'

    def get_roster(self, user_id):
        print(user_id)
        print(self.ep)
        data = self.sleeper_api.get_data(self.ep)
        print(data)
        print("stop")
        # self.write_to_file()