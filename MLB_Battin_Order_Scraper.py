from bs4 import BeautifulSoup
import requests
import csv


url='https://www.mlb.com/starting-lineups/2019-06-12'

re = requests.get(url)
soup = BeautifulSoup(re.content, "html.parser")

all_teams = []    # initialize a list into which you'll save the dictionaries of the teams and players
teams = soup.find_all("div", "starting-lineups__matchup")


c = 0 #player counter
for team in teams:
    players_list = []
    teamnames = team.find_all("span", "starting-lineups__team-name")
    team1 = teamnames[0].text.strip()
    team2 = teamnames[2].text.strip()
    players_collection = team.find("div", "starting-lineups__teams--sm")
    players = players_collection.find_all('li', 'starting-lineups__player')
    # from these players 9 will belong to team1 and 9 to team2
    for player in players[:9]:   # take the first 9 players
         name = player.find("a").contents[0]
         c += 1
         print(c, name)
         players_list.append(name)
    all_teams.append({"team": team1, "players": players_list})   # add dictionary to the list
    players_list = []    # reset list
    for player in players[9:]:   # take the second 9 players
         name = player.find("a").contents[0]
         c += 1
         print(c, name)
         players_list.append(name)
    all_teams.append({"team": team2, "players": players_list})   # add dictionary to the list



with open('test2.csv', 'w', newline='') as f:
    thewriter=csv.writer(f)
    thewriter.writerow(['Team', 'Player 1','Player 2','Player 3','Player 4','Player 5','Player 6','Player 7', 'Player 8', 'Player 9'])
    for batters in all_teams:
        _temp = [batters["team"]]
        for p in batters["players"]:
            _temp.append(p)
        thewriter.writerow(_temp)