import numpy as np
from task08 import simulate_end_steps, calculate_odds

def test_simulate_end_steps_length():
    end_steps = simulate_end_steps(times=500, throws=100, rng=np.random.default_rng(123))
    assert len(end_steps) == 500

    count_above_60 = np.sum(end_steps >= 60)
    assert count_above_60 == 276

def test_end_steps_values_non_negative():
    end_steps = simulate_end_steps(times=500, throws=100, rng=np.random.default_rng(123))
    assert np.all(end_steps >= 0)

def test_calculate_odds_range():
    end_steps = np.array([10, 60, 70, 50, 100])
    odds = calculate_odds(end_steps, threshold=60)
    assert odds == 3/5
