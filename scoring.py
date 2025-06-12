 # scoring.py

def calculate_fantasy_points(stats):
    """
    Simulate fantasy points (like Dream11 rules).
    You can edit this to match platform-specific rules.
    """
    points = 0
    points += stats.get('runs', 0) * 1      # 1 point per run
    points += stats.get('fifties', 0) * 8   # bonus for 50s
    points += stats.get('centuries', 0) * 16
    points += stats.get('wickets', 0) * 25
    points += stats.get('maidens', 0) * 12
    points += stats.get('catches', 0) * 8
    points += stats.get('stumpings', 0) * 12
    points -= stats.get('duck', 0) * 2
    return points