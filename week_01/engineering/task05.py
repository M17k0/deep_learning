from week_01.engineering.task03 import random_walk

SIMULATION_TIMES = 5

def simulate_walks(times=SIMULATION_TIMES, throws=100, rng=None):
  all_walks = []
  for _ in range(times):
    walk = random_walk(throws=throws, rng=rng)
    all_walks.append(walk)
  return all_walks

def main():
  walks = simulate_walks()
  print(walks)

if __name__ == "__main__":
  main()
