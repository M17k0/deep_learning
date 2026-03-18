import matplotlib.pyplot as plt
import numpy as np
from task06 import plot_all_walks


def test_plot_all_walks(monkeypatch):
  calls = {
      "plot": False,
      "xlabel": False,
      "ylabel": False,
      "title": False,
      "show": False
  }

  def fake_plot(data):
    calls["plot"] = True
    expected_array = np.array([[0, 1, 2, 3, 4], [0, 0, 1, 2, 3],
                               [0, 2, 1, 3, 4]]).T
    np.testing.assert_array_equal(data, expected_array)

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

  walks = [[0, 1, 2, 3, 4], [0, 0, 1, 2, 3], [0, 2, 1, 3, 4]]

  plot_all_walks(walks)

  assert all(calls.values())
