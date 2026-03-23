import numpy as np
import matplotlib.pyplot as plt

from week_01.engineering.task07 import random_walk

DEFAULT_RNG = np.random.default_rng(123)

def simulate_end_steps(times=500, throws=100, rng=None):
    if rng is None:
        rng = np.random.default_rng()

    end_steps = []

    for _ in range(times):
        walk = random_walk(throws=throws, rng=rng)
        end_steps.append(walk[-1])

    return np.array(end_steps)


def plot_end_steps_histogram(end_steps):
    plt.hist(end_steps, bins=10)
    plt.xlabel("End step")
    plt.ylabel("Count")
    plt.title("Random Walk End Steps Distribution")
    plt.show()


def calculate_odds(end_steps, threshold=60):
    success = np.sum(end_steps >= threshold)
    odds = success / len(end_steps)
    return odds


def main():
    end_steps = simulate_end_steps(times=500, throws=100, rng=DEFAULT_RNG)
    plot_end_steps_histogram(end_steps)

    odds = calculate_odds(end_steps, threshold=60)
    print(f"Odds of reaching 60 steps: {odds:.4f}")
    # Odds of reaching ≥ 60 steps: approximately 55%
    

if __name__ == "__main__":
    main()