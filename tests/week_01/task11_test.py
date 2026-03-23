import numpy as np

from week_01.perceptrons.task11 import SquareMLP

DATASET = [(x, x**2) for x in range(0, 5)]
TEST_CASES = [0, 1, 2, 3, -1]


def get_trained_model(seed=123, epochs=50000):
  np.random.seed(seed)
  model = SquareMLP()
  model.train(DATASET, epochs=epochs)
  return model


class TestSquareMLP:

  def test_when_trained_then_predictions_are_close_to_square(self):
    model = get_trained_model()

    for x in TEST_CASES:
      y_pred = model.forward(x)
      y_true = x**2

      assert abs(y_pred - y_true) < 2

  def test_when_training_then_loss_decreases(self):
    np.random.seed(123)
    model = SquareMLP()

    initial_loss = model.calculate_loss(DATASET)
    model.train(DATASET, epochs=5000)
    final_loss = model.calculate_loss(DATASET)

    assert final_loss < initial_loss
