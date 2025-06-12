 # model_core.py

def evaluate_player(player_stats):
    """Basic scoring logic (you can expand this)"""
    score = 0
    score += player_stats.get("recent_runs", 0) * 0.5
    score += player_stats.get("wickets", 0) * 25
    score += player_stats.get("catches", 0) * 10
    score -= player_stats.get("ducks", 0) * 5
    return score