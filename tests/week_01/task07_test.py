import numpy as np
import matplotlib.pyplot as plt

from week_01.engineering.task07 import random_walk, simulate_walks_with_clumsiness, draw_walks


class TestRandomWalk:

  def test_when_called_with_100_throws_then_length_is_101(self):
    rng = np.random.default_rng(123)
    walk = random_walk(throws=100, rng=rng)
    assert len(walk) == 101

  def test_when_walk_is_generated_then_steps_are_non_negative_integers(self):
    rng = np.random.default_rng(123)
    walk = random_walk(throws=100, rng=rng)
    assert all(isinstance(step, int) for step in walk)
    assert all(step >= 0 for step in walk)


class TestSimulateWalksWithClumsiness:

  def test_when_times_is_twenty_then_returns_twenty_walks(self):
    walks = simulate_walks_with_clumsiness(times=20, throws=100)
    assert len(walks) == 20

  def test_when_walks_are_simulated_then_each_walk_has_101_steps(self):
    walks = simulate_walks_with_clumsiness(times=20, throws=100)
    assert all(len(walk) == 101 for walk in walks)


class TestDrawWalks:

  def test_when_walks_are_provided_then_plot_is_called_for_each_walk(
      self, monkeypatch):
    calls = {"plot": 0}

    def fake_plot(walk):
      calls["plot"] += 1
      assert all(isinstance(step, int) for step in walk)

    monkeypatch.setattr(plt, "plot", fake_plot)
    monkeypatch.setattr(plt, "show", lambda: None)

    example_walks = [[0, 1, 2, 3], [0, 0, 1, 2], [0, 2, 1, 3]]
    draw_walks(example_walks)

    assert calls["plot"] == len(example_walks)

  def test_when_walks_are_drawn_then_labels_title_and_show_are_called(
      self, monkeypatch):
    calls = {"xlabel": False, "ylabel": False, "title": False, "show": False}

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

    monkeypatch.setattr(plt, "plot", lambda _: None)
    monkeypatch.setattr(plt, "xlabel", fake_xlabel)
    monkeypatch.setattr(plt, "ylabel", fake_ylabel)
    monkeypatch.setattr(plt, "title", fake_title)
    monkeypatch.setattr(plt, "show", fake_show)

    example_walks = [[0, 1, 2, 3], [0, 0, 1, 2], [0, 2, 1, 3]]
    draw_walks(example_walks)

    assert all(calls.values())
