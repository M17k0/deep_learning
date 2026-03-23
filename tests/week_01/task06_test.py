import matplotlib.pyplot as plt
import numpy as np

from week_01.engineering.task06 import plot_all_walks


class TestPlotAllWalks:

  def test_when_walks_are_provided_then_plot_receives_transposed_array(
      self, monkeypatch):

    def fake_plot(data):
      expected_array = np.array([[0, 1, 2, 3, 4], [0, 0, 1, 2, 3],
                                 [0, 2, 1, 3, 4]]).T
      np.testing.assert_array_equal(data, expected_array)

    monkeypatch.setattr(plt, "plot", fake_plot)
    monkeypatch.setattr(plt, "show", lambda: None)

    walks = [[0, 1, 2, 3, 4], [0, 0, 1, 2, 3], [0, 2, 1, 3, 4]]
    plot_all_walks(walks)

  def test_when_walks_are_plotted_then_labels_title_and_show_are_called(
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

    walks = [[0, 1, 2, 3, 4], [0, 0, 1, 2, 3], [0, 2, 1, 3, 4]]
    plot_all_walks(walks)

    assert all(calls.values())
