import pandas as pd

def export_teams_to_csv(teams, filename="fantasy_teams.csv"):
    rows = []
    for i, team in enumerate(teams):
        for p in team["team"]:
            name = p
            role_credit = p.split("(")[-1].replace(")", "")
            role, credit = role_credit.split(",")
            credit = credit.replace("cr", "").strip()
            rows.append({
                "Team #": i+1,
                "Player": name.replace(f" ({role_credit})", ""),
                "Role": role.strip(),
                "Credit": credit,
                "Captain": "✅" if team["captain"] in name else "",
                "Vice-Captain": "✅" if team["vice_captain"] in name else ""
            })

    df = pd.DataFrame(rows)
    df.to_csv(filename, index=False)
    print(f"\n✅ All teams exported to: {filename}") 