
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


def get_teams():
    """
    return a list of NBA teams
    """
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(
        BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

    teams = list(filter(lambda x: x['name'] != "Team", teams))
    return teams


def get_ppg():
    """
    Team rank of Point Per Game
    """
    teams = get_teams()
    teams.sort(key=lambda x: int(x['ppg']['rank']))

    print("--------------------------------------")
    print("Point Per Game Rank")
    print('  \t Team    -   \t  PPG')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        team_name = name + ' ' + nickname
        ppg = team['ppg']['avg']
        print(f"{i + 1}. {team_name} - {ppg}")


def get_assist():
    """
    Team rank of average assists
    """
    teams = get_teams()
    printer.pprint(teams)
    teams.sort(key=lambda x: int(x['apg']['rank']))

    print("--------------------------------------")
    print("Assist Per Game")
    print('   \t Team       -    \t AST')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        team_name = name + ' ' + nickname
        ast = team['apg']['avg']
        print(f"{i + 1}. {team_name} - {ast}")


def get_rebound():
    """
    Team rank of average rebound
    """
    teams = get_teams()
    printer.pprint(teams)
    teams.sort(key=lambda x: int(x['trpg']['rank']))

    print("--------------------------------------")
    print("Rebound Per Game")
    print('  \t Team    -     \t Rebound')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        team_name = name + ' ' + nickname
        reb = team['trpg']['avg']
        print(f"{i + 1}. {team_name} - {reb}")

def get_block():
    """
    Team's average blocks per game
    """
    teams = get_teams()
    printer.pprint(teams)
    teams.sort(key=lambda x: int(x['bpg']['rank']))

    print("--------------------------------------")
    print("Rebound Per Game")
    print('  \t Team    -     \t Rebound')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        team_name = name + ' ' + nickname
        blk = team['bpg']['avg']
        print(f"{i + 1}. {team_name} - {blk}")


def get_efficiency():
    """
    Team's Efficiency
    """
    teams = get_teams()
    printer.pprint(teams)
    teams.sort(key=lambda x: int(x['eff']['rank']))

    print("--------------------------------------")
    print("Rebound Per Game")
    print('  \t Team    -     \t Rebound')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        team_name = name + ' ' + nickname
        eff = team['eff']['avg']
        print(f"{i + 1}. {team_name} - {eff}")


def get_fgp():
    """
    Team's Efficiency
    """
    teams = get_teams()
    printer.pprint(teams)
    teams.sort(key=lambda x: int(x['fgp']['rank']))

    print("--------------------------------------")
    print("Field Goals %")
    print('  \t Team    -     \t FG%')
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        team_name = name + ' ' + nickname
        fgp = int(float(team['fgp']['avg'])*100)
        print(f"{i + 1}. {team_name} - {fgp}")


if __name__ == '__main__':
    # get_links()
    # get_scoreboard()
    # get_ppg()
    # get_assist()
    # get_rebound()
    # get_block()
    # get_efficiency()
    get_fgp()
