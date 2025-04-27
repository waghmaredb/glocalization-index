# local_capacity.py
def calculate_L(metrics: dict) -> float:
    """
    Calculate Local Adaptation Capacity (0-100)
    Implements weighting from philosophical frameworks
    """
    components = {
        'digital': (metrics['fiber_optic']/95 + metrics['cloud_adoption']/89)/2,
        'workforce': (metrics['stem_graduates']/47 + metrics['ai_literacy']/68)/2,
        'institutional': ((180-metrics['approval_days'])/180 + metrics['sandbox_utilization']/75)/2,
        'innovation': (metrics['co_patenting']/18 + metrics['rnd_investment']/4.3)/2,
        'cultural': (metrics['tech_optimism']/82 + metrics['legacy_replacement']/70)/2
    }
    
    weights = [0.15, 0.20, 0.25, 0.20, 0.20]
    return sum(comp*weight for comp, weight in zip(components.values(), weights)) * 100
