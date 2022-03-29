
from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()


def get_links():
    """
    Get the base URL
    """
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links


def get_scoreboard():
    """
    scoreboard for today's games
    """
    current_date = get_links()['currentDate']
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']

    today = current_date[4:6] + '/' + current_date[6:] + '/' + current_date[:4]
    print('Today:', today)
    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']

        print("------------------------------------------")
        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"{home_team['score']} - {away_team['score']}")
        print(f"{clock} - {period['current']}")


def get_ppg():
    """
    Team rank of Point Per Game
    """
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(
        BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

    teams = list(filter(lambda x: x['name'] != "Team", teams))       # filter out teams with name starting with Team
    printer.pprint(teams)
    teams.sort(key=lambda x: int(x['ppg']['rank']))

    print("--------------------------------------")
    print("Point Per Game Rank")
    print('   Team -\t Nickname -   PPG')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']
        print(f"{i + 1}. {name} - {nickname} - {ppg}")


if __name__ == '__main__':
    # get_links()
    # get_scoreboard()
    get_ppg()

