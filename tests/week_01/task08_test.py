import numpy as np

from week_01.engineering.task08 import simulate_end_steps, calculate_odds


class TestSimulateEndSteps:

  def test_when_times_is_500_then_returns_500_end_steps(self):
    end_steps = simulate_end_steps(times=500,
                                   throws=100,
                                   rng=np.random.default_rng(123))
    assert len(end_steps) == 500

  def test_when_rng_is_seeded_then_count_above_60_is_expected(self):
    end_steps = simulate_end_steps(times=500,
                                   throws=100,
                                   rng=np.random.default_rng(123))
    count_above_60 = np.sum(end_steps >= 60)
    assert count_above_60 == 276

  def test_when_end_steps_are_simulated_then_all_values_are_non_negative(self):
    end_steps = simulate_end_steps(times=500,
                                   throws=100,
                                   rng=np.random.default_rng(123))
    assert np.all(end_steps >= 0)


class TestCalculateOdds:

  def test_when_values_meet_threshold_then_returns_fraction_of_successes(self):
    end_steps = np.array([10, 60, 70, 50, 100])
    odds = calculate_odds(end_steps, threshold=60)
    assert odds == 3 / 5
