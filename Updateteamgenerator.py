from scoring import predict_score
import random

def generate_fantasy_team(team_data):
    all_players = team_data["team1"] + team_data["team2"]

    # Add predicted score and simulated credit
    for p in all_players:
        p["score"] = predict_score(p["name"], p["role"])
        p["credit"] = 8 + (len(p["name"]) % 4)  # Simulated credits (8–11)

    # Sort by highest score
    sorted_players = sorted(all_players, key=lambda x: x["score"], reverse=True)

    team = []
    roles = {"bat": 0, "bowl": 0, "wk": 0, "all": 0}
    limits = {"bat": 3, "bowl": 3, "wk": 1, "all": 4}

    total_credit = 0
    team_counts = {"team1": 0, "team2": 0}

    for p in sorted_players:
        if len(team) == 11:
            break

        role = p["role"] if p["role"] in roles else "all"
        team_key = "team1" if p in team_data["team1"] else "team2"

        if (
            roles[role] < limits[role] and
            team_counts[team_key] < 7 and
            total_credit + p["credit"] <= 100
        ):
            team.append(p)
            roles[role] += 1
            total_credit += p["credit"]
            team_counts[team_key] += 1

    captain = team[0]["name"]
    vice_captain = team[1]["name"]

    return {
        "team": [f"{p['name']} ({p['role']}, {p['credit']}cr)" for p in team],
        "captain": captain,
        "vice_captain": vice_captain,
        "total_credit": total_credit,
        "split": team_counts
    }