 # predict.py

from model_core import evaluate_player

def generate_teams(player_pool, num_teams=20):
    """
    Create fantasy teams based on player scores.
    Each team is a list of player names with high predicted scores.
    """
    scored_players = []
    for player in player_pool:
        score = evaluate_player(player['stats'])
        scored_players.append((player['name'], score))

    # Sort players by score descending
    scored_players.sort(key=lambda x: x[1], reverse=True)

    teams = []
    for i in range(num_teams):
        # Rotate through sorted players for diversity
        team = [scored_players[(j + i) % len(scored_players)][0] for j in range(11)]
        teams.append(team)

    return teams