import requests
import json

''' Return top 3 best challenger players by win rate '''

class RiotAPI:
    def __init__(self):
        self.routing_value = "na1.api.riotgames.com"
        self.api_key = "RGAPI-05b2dabe-7f02-4187-8905-d8143076bb5b"

    def lookup(self):
        response = requests.get("https://" + self.routing_value +
                                "/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=" + self.api_key)
        top_player_info = json.loads(response.content)
        self.print_highest_winrates(self.find_winrates(top_player_info["entries"]))

    def find_winrates(self, summoner_list):
        winrates = {}
        for player_info in summoner_list:
            curr_winrate = float(player_info["wins"]) / (float(player_info["losses"]) + float(player_info["wins"]))
            winrates[player_info["summonerName"]] = curr_winrate
        return winrates

    def print_highest_winrates(self, winrates):
        sorted_winrates = sorted(winrates.items(), key = lambda x: x[1], reverse = True)
        for x in range(3):
            print("Summoner Name: {name}, Win Ratio: {wr:.2f}").format(name = sorted_winrates[x][0], wr = sorted_winrates[x][1])

x = RiotAPI()
x.lookup()