import numpy as np

# Model form:
# h1 = sigmoid(w1 * x + b1)
# h2 = sigmoid(w2 * x + b2)
# ...
# hN = sigmoid(wN * x + bN)
#
# y = v1*h1 + v2*h2 + ... + vN*hN + b_out
# Total parameters:
# - Hidden layer: N weights (w) + N biases (b)
# - Output layer: N weights (v) + 1 bias (b_out)
# => Total = 3N + 1 parameters


class SquareMLP:

  def __init__(self, hidden_size=2, learning_rate=0.01, epsilon=0.001):
    self.hidden_size = hidden_size
    self.learning_rate = learning_rate
    self.epsilon = epsilon

    self.w = np.random.uniform(-1, 1, hidden_size)
    self.b = np.random.uniform(-1, 1, hidden_size)

    self.v = np.random.uniform(-1, 1, hidden_size)
    self.b_out = np.random.uniform(-1, 1)

  def sigmoid(self, x):
    return 1 / (1 + np.exp(-x))

  def forward(self, x):
    h = self.sigmoid(self.w * x + self.b)
    y = np.dot(self.v, h) + self.b_out
    return y

  def calculate_loss(self, dataset):
    errors = []
    for x, y in dataset:
      y_pred = self.forward(x)
      errors.append((y_pred - y)**2)
    return np.mean(errors)

  def _get_params(self):
    return np.concatenate([self.w, self.b, self.v, [self.b_out]])

  def _set_params(self, params):
    n = self.hidden_size
    self.w = params[0:n]
    self.b = params[n:2 * n]
    self.v = params[2 * n:3 * n]
    self.b_out = params[-1]

  def train(self, dataset, epochs=20000):
    for _ in range(epochs):
      loss = self.calculate_loss(dataset)
      params = self._get_params()
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
