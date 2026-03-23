from week_01.engineering.task02 import random_walk

EXPECTED_WALK = [
    0, -1, 0, 1, 0, 2, 1, 0, 1, 0, 1, 2, 3, 6, 5, 6, 7, 13, 12, 13, 12, 11, 10,
    11, 12, 11, 12, 13, 12, 13, 14, 19, 18, 23, 22, 23, 24, 23, 22, 21, 20, 21,
    20, 21, 22, 21, 22, 21, 20, 21, 20, 21, 20, 22, 23, 24, 28, 31, 30, 29, 31,
    32, 33, 32, 33, 34, 35, 41, 40, 41, 42, 43, 42, 43, 44, 46, 47, 48, 50, 51,
    50, 51, 50, 51, 50, 51, 52, 53, 54, 55, 54, 53, 54, 53, 54, 55, 56, 57, 56,
    57, 58
]


class TestRandomWalk:

  def test_when_called_with_100_throws_then_length_is_101(self):
    walk = random_walk(100)
    assert len(walk) == 101

  def test_when_seed_is_123_then_returns_expected_walk(self):
    walk = random_walk(100, seed=123)
    assert walk == EXPECTED_WALK
