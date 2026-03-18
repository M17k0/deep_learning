from pdb import main

import numpy as np

# Model form:
# y = w1*x1 + w2*x2
# Number of parameters: 2 (w1, w2)

or_dataset = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)]

and_dataset = [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)]


def calculate_loss(w1, w2, dataset):
  errors = []

  for x1, x2, y in dataset:
    y_observed = w1 * x1 + w2 * x2
    errors.append((y_observed - y)**2)

  return np.mean(errors)


def train_model(dataset, epochs=100000, learning_rate=0.001, epsilon=0.001):
  w1 = np.random.uniform(0, 1)
  w2 = np.random.uniform(0, 1)

  for _ in range(epochs):
    loss = calculate_loss(w1, w2, dataset)

    d_w1 = (calculate_loss(w1 + epsilon, w2, dataset) - loss) / epsilon
    d_w2 = (calculate_loss(w1, w2 + epsilon, dataset) - loss) / epsilon

    w1 = w1 - learning_rate * d_w1
    w2 = w2 - learning_rate * d_w2

  return w1, w2


def predict(w1, w2, dataset):
  for x1, x2, _ in dataset:
    y_pred = w1 * x1 + w2 * x2
    print(f"Input ({x1},{x2}) -> {y_pred}")


def main():
  print("Training OR model")
  or_w1, or_w2 = train_model(or_dataset)

  print("Training AND model")
  and_w1, and_w2 = train_model(and_dataset)

  print("\nOR predictions:")
  predict(or_w1, or_w2, or_dataset)
  print("w1:", or_w1, "w2:", or_w2)

  print("\nAND predictions:")
  predict(and_w1, and_w2, and_dataset)
  print("w1:", and_w1, "w2:", and_w2)

# Values closer to 0 or 1 indicate higher confidence in the prediction.
# When both input parameters are 0 the predicted output is always 0.

if __name__ == "__main__":
  main()
