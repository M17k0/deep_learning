import numpy as np
import matplotlib.pyplot as plt

DEFAULT_RNG = np.random.default_rng(123)

def roll_dice(rng):
  return rng.integers(1, 7)

def random_walk(throws=100, rng=None):
  if rng is None:
    rng = np.random.default_rng()

  step = 0
  steps = [step]

  for _ in range(throws):
    dice = roll_dice(rng)

    if dice in [1, 2]:
      step = max(0, step - 1)
    elif dice in [3, 4, 5]:
      step += 1
    else:
      step += roll_dice(rng)

    if rng.random() <= 0.005:
      step = 0

    steps.append(int(step))

  return steps


def simulate_walks_with_clumsiness(times=20, throws=100):
  all_walks = []
  for _ in range(times):
    walk = random_walk(throws=throws, rng=DEFAULT_RNG)
    all_walks.append(walk)
  return all_walks

def draw_walks(walks):
  for walk in walks:
    plt.plot(walk)

  plt.title("Random walks")
  plt.xlabel("Throw")
  plt.ylabel("Step")
  plt.show()

def main():
  walks = simulate_walks_with_clumsiness()
  draw_walks(walks)


if __name__ == "__main__":
  main()
