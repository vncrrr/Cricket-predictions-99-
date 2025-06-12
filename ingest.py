 # ingest.py

def get_mock_player_pool():
    """Simulates a pool of 22 players with sample stats"""
    return [
        {'name': 'Player 1', 'stats': {'runs': 45, 'wickets': 1, 'catches': 0}},
        {'name': 'Player 2', 'stats': {'runs': 10, 'wickets': 2, 'catches': 1}},
        {'name': 'Player 3', 'stats': {'runs': 70, 'wickets': 0, 'catches': 2}},
        {'name': 'Player 4', 'stats': {'runs': 25, 'wickets': 1}},
        {'name': 'Player 5', 'stats': {'runs': 5, 'wickets': 3}},
        {'name': 'Player 6', 'stats': {'runs': 38, 'wickets': 0, 'catches': 1}},
        {'name': 'Player 7', 'stats': {'runs': 0, 'wickets': 4, 'duck': 1}},
        {'name': 'Player 8', 'stats': {'runs': 60, 'wickets': 0}},
        {'name': 'Player 9', 'stats': {'runs': 12, 'wickets': 1}},
        {'name': 'Player 10', 'stats': {'runs': 80, 'wickets': 0}},
        {'name': 'Player 11', 'stats': {'runs': 15, 'wickets': 2}},
        {'name': 'Player 12', 'stats': {'runs': 28, 'wickets': 1}},
        {'name': 'Player 13', 'stats': {'runs': 33, 'wickets': 1}},
        {'name': 'Player 14', 'stats': {'runs': 50, 'wickets': 0}},
        {'name': 'Player 15', 'stats': {'runs': 0, 'wickets': 3}},
        {'name': 'Player 16', 'stats': {'runs': 25, 'wickets': 1}},
        {'name': 'Player 17', 'stats': {'runs': 60, 'wickets': 0}},
        {'name': 'Player 18', 'stats': {'runs': 5, 'wickets': 2}},
        {'name': 'Player 19', 'stats': {'runs': 10, 'wickets': 1}},
        {'name': 'Player 20', 'stats': {'runs': 40, 'wickets': 0}},
        {'name': 'Player 21', 'stats': {'runs': 18, 'wickets': 2}},
        {'name': 'Player 22', 'stats': {'runs': 22, 'wickets': 1}}
    ]