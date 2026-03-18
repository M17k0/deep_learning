import matplotlib.pyplot as plt

from task03 import random_walk


def draw_plot_from_walk(walk):
  plt.plot(walk)
  plt.xlabel("Throw")
  plt.ylabel("Step")
  plt.title("Random walk")
  plt.show()
  

def main():
  walk = random_walk()
  draw_plot_from_walk(walk)


if __name__ == "__main__":
  main()
