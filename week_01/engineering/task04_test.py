import matplotlib.pyplot as plt

from task04 import draw_plot_from_walk


def test_draw_plot_from_walk(monkeypatch):
  calls = {
      "plot": False,
      "xlabel": False,
      "ylabel": False,
      "title": False,
      "show": False
  }

  def fake_plot(data):
    calls["plot"] = True
    assert data == [0, 1, 2, 3]

  def fake_xlabel(label):
    calls["xlabel"] = True
    assert label == "Throw"

  def fake_ylabel(label):
    calls["ylabel"] = True
    assert label == "Step"

  def fake_title(title):
    calls["title"] = True
    assert title == "Random walk"

  def fake_show():
    calls["show"] = True

  monkeypatch.setattr(plt, "plot", fake_plot)
  monkeypatch.setattr(plt, "xlabel", fake_xlabel)
  monkeypatch.setattr(plt, "ylabel", fake_ylabel)
  monkeypatch.setattr(plt, "title", fake_title)
  monkeypatch.setattr(plt, "show", fake_show)

  walk = [0, 1, 2, 3]
  draw_plot_from_walk(walk)

  assert all(calls.values())
