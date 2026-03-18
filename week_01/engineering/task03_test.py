import numpy as np

from task03 import random_walk


def test_random_walk_length():
  walk = random_walk(100)
  assert len(walk) == 101


def test_random_walk_output():
  walk = random_walk(100, np.random.default_rng(123))

  assert walk == [
      0, 0, 1, 2, 1, 3, 2, 1, 2, 1, 2, 3, 4, 7, 6, 7, 8, 14, 13, 14, 13, 12,
      11, 12, 13, 12, 13, 14, 13, 14, 15, 20, 19, 24, 23, 24, 25, 24, 23, 22,
      21, 22, 21, 22, 23, 22, 23, 22, 21, 22, 21, 22, 21, 23, 24, 25, 29, 32,
      31, 30, 32, 33, 34, 33, 34, 35, 36, 42, 41, 42, 43, 44, 43, 44, 45, 47,
      48, 49, 51, 52, 51, 52, 51, 52, 51, 52, 53, 54, 55, 56, 55, 54, 55, 54,
      55, 56, 57, 58, 57, 58, 59
  ]
