import numpy as np

from week_01.engineering import task01


class TestGenerateRandomValues:

  def test_when_rng_is_seeded_then_returns_expected_values(self, monkeypatch):
    monkeypatch.setattr(task01, "rng", np.random.default_rng(123))

    rand_float, rand_int1, rand_int2 = task01.generate_random_values()

    assert rand_float == 0.6823518632481435
    assert rand_int1 == 4
    assert rand_int2 == 1


class TestSimulateStep:

  def test_when_rng_is_seeded_then_returns_expected_dice_and_step(
      self, monkeypatch):
    monkeypatch.setattr(task01, "rng", np.random.default_rng(123))

    dice, step = task01.simulate_step()

    assert dice == 1
    assert step == 49
