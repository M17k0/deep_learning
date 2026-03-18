import numpy as np
import matplotlib.pyplot as plt
from task07 import random_walk, simulate_walks_with_clumsiness, draw_walks


def test_random_walk_length_and_values():
  rng = np.random.default_rng(123)
  walk = random_walk(throws=100, rng=rng)

  assert len(walk) == 101

  assert all(isinstance(step, int) for step in walk)
  assert all(step >= 0 for step in walk)


def test_simulate_walks_with_clumsiness_length():
  walks = simulate_walks_with_clumsiness(times=20, throws=100)

  assert len(walks) == 20
  assert all(len(walk) == 101 for walk in walks)


def test_draw_walks_calls(monkeypatch):
  calls = {
      "plot": False,
      "xlabel": False,
      "ylabel": False,
      "title": False,
      "show": False
  }

  def fake_plot(walk):
    calls["plot"] = True
    assert all(isinstance(step, int) for step in walk)

  def fake_xlabel(label):
    calls["xlabel"] = True
    assert label == "Throw"

  def fake_ylabel(label):
    calls["ylabel"] = True
    assert label == "Step"

  def fake_title(title):
    calls["title"] = True
    assert title == "Random walks"

  def fake_show():
    calls["show"] = True

  monkeypatch.setattr(plt, "plot", fake_plot)
  monkeypatch.setattr(plt, "xlabel", fake_xlabel)
  monkeypatch.setattr(plt, "ylabel", fake_ylabel)
  monkeypatch.setattr(plt, "title", fake_title)
  monkeypatch.setattr(plt, "show", fake_show)

  example_walks = [[0, 1, 2, 3], [0, 0, 1, 2], [0, 2, 1, 3]]

  draw_walks(example_walks)

  assert all(calls.values())
