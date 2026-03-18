from task01 import generate_random_values, simulate_step


def test_random_values():
  rand_float, rand_int1, rand_int2 = generate_random_values()

  assert rand_float == 0.6823518632481435
  assert rand_int1 == 4
  assert rand_int2 == 1


def test_simulation():
  dice, step = simulate_step()

  assert dice == 6
  assert step == 52
