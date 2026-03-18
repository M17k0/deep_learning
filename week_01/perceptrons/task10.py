import numpy as np

# Model form:
# h1 = sigmoid(w1*x1 + w2*x2 + b1)
# h2 = sigmoid(w3*x1 + w4*x2 + b2)
# y  = sigmoid(v1*h1 + v2*h2 + b3)
# Total parameters: 9


class Xor:
  DATASET = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]

  def __init__(self, learning_rate=0.1, epsilon=0.001):
    self.learning_rate = learning_rate
    self.epsilon = epsilon

    self.w = np.random.uniform(-1, 1, 4)
    self.b = np.random.uniform(-1, 1, 2)

    self.v = np.random.uniform(-1, 1, 2)
    self.b_out = np.random.uniform(-1, 1)

  def sigmoid(self, x):
    return 1 / (1 + np.exp(-x))

  def forward(self, x1, x2):
    h1 = self.sigmoid(self.w[0] * x1 + self.w[1] * x2 + self.b[0])
    h2 = self.sigmoid(self.w[2] * x1 + self.w[3] * x2 + self.b[1])

    y = self.sigmoid(self.v[0] * h1 + self.v[1] * h2 + self.b_out)

    return y

  def calculate_loss(self, dataset):
    errors = []
    for x1, x2, y in dataset:
      y_pred = self.forward(x1, x2)
      errors.append((y_pred - y)**2)
    return np.mean(errors)

  def train(self, dataset, epochs=100000):
    for _ in range(epochs):
      loss = self.calculate_loss(dataset)

      params = np.concatenate([self.w, self.b, self.v, [self.b_out]])
      grads = np.zeros_like(params)

      for i in range(len(params)):
        original = params[i]

        params[i] += self.epsilon
        self._set_params(params)
        loss_eps = self.calculate_loss(dataset)

        grads[i] = (loss_eps - loss) / self.epsilon

        params[i] = original

      params -= self.learning_rate * grads
      self._set_params(params)

  def _set_params(self, params):
    self.w = params[0:4]
    self.b = params[4:6]
    self.v = params[6:8]
    self.b_out = params[8]

  def predict(self, dataset):
    for x1, x2, _ in dataset:
      y_pred = self.forward(x1, x2)
      print(f"Input ({x1},{x2}) -> {y_pred:.4f}")


def main():
  model = Xor()
  model.train(Xor.DATASET)

  print("\nXOR predictions:")
  print(f"Input (0,0) -> {model.forward(0, 0):.4f}")
  print(f"Input (0,1) -> {model.forward(0, 1):.4f}")
  print(f"Input (1,0) -> {model.forward(1, 0):.4f}")
  print(f"Input (1,1) -> {model.forward(1, 1):.4f}")


if __name__ == "__main__":
  main()
