import numpy as np

DEFAULT_RNG = np.random.default_rng(123)

def random_walk(throws=100, rng=None):
  if rng is None:
    rng = np.random.default_rng()

  step = 0
  steps = [step]

  for _ in range(throws):
    dice = rng.integers(1, 7)

    if dice in [1, 2]:
      step = max(0, step - 1)
    elif dice in [3, 4, 5]:
      step += 1
    else:
      step += rng.integers(1, 7)

    steps.append(int(step))

  return steps


def main():
  steps = random_walk(100, DEFAULT_RNG)
  print(f"Steps: {steps}")


if __name__ == "__main__":
  main()
