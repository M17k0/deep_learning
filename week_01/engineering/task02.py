import numpy as np


def random_walk(throws=100, seed=123):
  rng = np.random.default_rng(seed)
  step = 0
  steps = [step]

  for _ in range(throws):
    dice = rng.integers(1, 7)

    if dice in [1, 2]:
      step -= 1
    elif dice in [3, 4, 5]:
      step += 1
    else:
      step += rng.integers(1, 7)

    steps.append(int(step))

  return steps


def main():
  steps = random_walk(100)
  print(f"Steps: {steps}")


# Do you notice anything unexpected in the output?
# The step number goes down to -1.

if __name__ == "__main__":
  main()
