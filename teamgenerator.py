import pandas as pd
import random

#  Export generated fantasy teams to CSV (optional use)
def export_teams_to_csv(teams, filename="fantasy_teams.csv"):
    rows = []
    for i, team in enumerate(teams):
        for p in team["team"]:
            name = p
            role_credit = p.split("(")[-1].replace(")", "")
            role, credit = role_credit.split(",")
            credit = credit.replace("cr", "").strip()
            rows.append({
                "Team #": i + 1,
                "Player": name.replace(f" ({role},{credit}cr)", ""),
                "Role": role.strip(),
                "Credit": credit,
                "Captain": "" if team["captain"] == p else "",
                "Vice-Captain": "" if team["vice_captain"] == p else ""
            })
    df = pd.DataFrame(rows)
    df.to_csv(filename, index=False)
    print(f"\n All teams exported to: {filename}")

#  Core model: generate 20 teams with random C/VC
def generate_multiple_teams(players):
    teams = []
    for _ in range(20):
        team = random.sample(players, 11)
        captain = random.choice(team)
        vice_captain = random.choice([p for p in team if p != captain])
        teams.append({
            "team": team,
            "captain": captain,
            "vice_captain": vice_captain
        })
    return teams
