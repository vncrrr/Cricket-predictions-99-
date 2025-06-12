import requests
from bs4 import BeautifulSoup

def get_lineup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    team_data = {"team1": [], "team2": []}
    all_blocks = soup.find_all('div', class_='player-box')

    current_team = "team1"
    for block in all_blocks:
        name_tag = block.find('div', class_='player-name')
        role_tag = block.find('div', class_='player-role')

        if not name_tag:
            continue

        name = name_tag.text.strip()
        role = role_tag.text.strip().lower() if role_tag else "all"

        player_info = {
            "name": name,
            "role": role  # "bat", "bowl", "wk", "all"
        }

        if "Team 2" in name:
            current_team = "team2"
            continue

        team_data[current_team].append(player_info)

    return team_data