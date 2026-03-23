import numpy as np

# Model form:
# y = w * x
# Number of parameters: 1 (weight w)


def create_dataset(n):
  return [(x, x * 2) for x in range(n)]


def initialize_weights(x, y, rng=None):
  if rng is None:
    rng = np.random.default_rng()

  return rng.uniform(x, y)


def calculate_loss(w, dataset):
  errors = []

  for x, y in dataset:
    y_observed = w * x
    errors.append((y_observed - y)**2)

  return np.mean(errors)


def train_model(dataset,
                epochs=10,
                learning_rate=0.001,
                epsilon=0.001,
                rng=None):
  if rng is None:
    rng = np.random.default_rng()

  w = initialize_weights(0, 10, rng)

  print("-------------")
  print("Initial w:", w)
  print("Loss before training:", calculate_loss(w, dataset))

  for epoch in range(epochs):
    loss = calculate_loss(w, dataset)

    loss_eps = calculate_loss(w + epsilon, dataset)
    derivative = (loss_eps - loss) / epsilon

    w = w - learning_rate * derivative

    # print(f"Epoch {epoch + 1} loss:", calculate_loss(w, dataset))

  print("Final w:", w)
  print("Loss after training:", calculate_loss(w, dataset))
  print("-------------")

  return w


def main():
  dataset = create_dataset(6)
  print("Training for 500 epochs with seed")

  rng = np.random.default_rng(42)
  train_model(dataset, epochs=500, learning_rate=0.001, epsilon=0.001, rng=rng)

  print("Training for 500 epochs without seed")
  train_model(dataset,
              epochs=500,
              learning_rate=0.001,
              epsilon=0.001,
              rng=None)


if __name__ == "__main__":
  main()


def task01_test():
  print(create_dataset(4))
  print(initialize_weights(0, 100))
  print(initialize_weights(0, 10))


def task02_test():
  dataset = create_dataset(6)
  w = initialize_weights(0, 10, rng=np.random.default_rng(42))

  loss = calculate_loss(w, dataset)
  print(f"Initial weight: {w}")
  print(f"MSE: {loss}")

  print(calculate_loss(w + 0.001 * 2, dataset))
  print(calculate_loss(w + 0.001, dataset))
  print(calculate_loss(w - 0.001, dataset))
  print(calculate_loss(w - 0.001 * 2, dataset))
  # When w moves closer to the optimal value (w = 2), the loss decreases.
  # When w moves farther from 2, the loss increases.


def task03_test():
  dataset = create_dataset(6)
  train_model(dataset,
              epochs=10,
              learning_rate=0.001,
              epsilon=0.001,
              rng=np.random.default_rng(42))
  # train_model(dataset, epochs=10, learning_rate=0.005, epsilon=0.001, rng=rng)
