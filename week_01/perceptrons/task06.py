import numpy as np

# Model form:
# y = w1*x1 + w2*x2 + b
# Number of parameters: 3 (w1, w2, b)

or_dataset = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)]

and_dataset = [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)]


def calculate_loss(w1, w2, b, dataset):
  errors = []

  for x1, x2, y in dataset:
    y_observed = w1 * x1 + w2 * x2 + b
    errors.append((y_observed - y)**2)

  return np.mean(errors)


def train_model(dataset, epochs=100000, lr=0.001, epsilon=0.001):
  w1 = np.random.uniform(0, 1)
  w2 = np.random.uniform(0, 1)
  b = np.random.uniform(0, 1)

  for _ in range(epochs):
    loss = calculate_loss(w1, w2, b, dataset)

    d_w1 = (calculate_loss(w1 + epsilon, w2, b, dataset) - loss) / epsilon
    d_w2 = (calculate_loss(w1, w2 + epsilon, b, dataset) - loss) / epsilon
    d_b = (calculate_loss(w1, w2, b + epsilon, dataset) - loss) / epsilon

    w1 -= lr * d_w1
    w2 -= lr * d_w2
    b -= lr * d_b

  return w1, w2, b


def predict(w1, w2, b, dataset):
  for x1, x2, _ in dataset:
    y_pred = w1 * x1 + w2 * x2 + b
    print(f"Input ({x1},{x2}) -> {y_pred:.4f}")


def main():
  or_w1, or_w2, or_b = train_model(or_dataset)
  and_w1, and_w2, and_b = train_model(and_dataset)

  print("OR predictions:")
  predict(or_w1, or_w2, or_b, or_dataset)
  print("w1:", or_w1, "w2:", or_w2, "b:", or_b)

  print("\nAND predictions:")
  predict(and_w1, and_w2, and_b, and_dataset)
  print("w1:", and_w1, "w2:", and_w2, "b:", and_b)

# With adding a bias parameter the model can learn to fit the data better
# and makes the predictions with higher confidence.

if __name__ == "__main__":
  main()
