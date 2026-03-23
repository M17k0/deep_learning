import numpy as np

rng = np.random.default_rng(123)


def generate_dice_roll():
  return rng.integers(1, 7)


def generate_random_values():
  rand_float = rng.random()
  rand_int1 = generate_dice_roll()
  rand_int2 = generate_dice_roll()

  return rand_float, rand_int1, rand_int2


def simulate_step():
  step = 50
  print(f"Before throw step = {step}")

  dice = generate_dice_roll()

  if dice in [1, 2]:
    step -= 1
  elif dice in [3, 4, 5]:
    step += 1
  else:
    step += generate_dice_roll()

  print(f"After throw dice = {dice}")
  print(f"After throw step = {step}")

  return dice, step


def main():
  rand_float, rand_int1, rand_int2 = generate_random_values()

  print(f"Random float: {rand_float}")
  print(f"Random integer 1: {rand_int1}")
  print(f"Random integer 2: {rand_int2}")

  simulate_step()


if __name__ == "__main__":
  main()
