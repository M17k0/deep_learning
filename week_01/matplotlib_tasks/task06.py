import matplotlib.pyplot as plt

from task05 import create_colorful_plot


def main():
  create_colorful_plot()

  plt.text(1550, 69, 'India')
  plt.text(3260, 78, 'China')
  plt.grid(True)

  plt.show()

  # A.) The countries in blue, corresponding to Africa, have both low life expectancy and a low GDP per capita.


if __name__ == "__main__":
  main()
