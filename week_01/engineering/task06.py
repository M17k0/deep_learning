import matplotlib.pyplot as plt
import numpy as np

from task05 import simulate_walks

def plot_all_walks(walks):
  walks_array = np.array(walks)
  
  print(walks_array)

  plt.plot(walks_array.T)
  plt.xlabel("Throw")
  plt.ylabel("Step")
  plt.title("Random walks")
  plt.show()

def main():
  walks = simulate_walks()
  plot_all_walks(walks)

if __name__ == "__main__":
  main()