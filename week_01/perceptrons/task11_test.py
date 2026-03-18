from task11 import SquareMLP


def create_dataset():
  return [(x, x**2) for x in range(0, 5)]


def get_trained_model():
  model = SquareMLP()
  dataset = create_dataset()
  model.train(dataset, epochs=50000)
  return model


def test_square_predictions():
  model = get_trained_model()

  test_cases = [0, 1, 2, 3, -1]

  for x in test_cases:
    y_pred = model.forward(x)
    y_true = x**2

    assert abs(y_pred - y_true) < 2


def test_loss_decreases():
  model = SquareMLP()
  dataset = create_dataset()

  initial_loss = model.calculate_loss(dataset)
  model.train(dataset, epochs=5000)
  final_loss = model.calculate_loss(dataset)

  assert final_loss < initial_loss
