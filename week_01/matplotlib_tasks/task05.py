import matplotlib.pyplot as plt

from task04 import create_plot

colors = [
    'red', 'green', 'blue', 'blue', 'yellow', 'black', 'green', 'red', 'red',
    'green', 'blue', 'yellow', 'green', 'blue', 'yellow', 'green', 'blue',
    'blue', 'red', 'blue', 'yellow', 'blue', 'blue', 'yellow', 'red', 'yellow',
    'blue', 'blue', 'blue', 'yellow', 'blue', 'green', 'yellow', 'green',
    'green', 'blue', 'yellow', 'yellow', 'blue', 'yellow', 'blue', 'blue',
    'blue', 'green', 'green', 'blue', 'blue', 'green', 'blue', 'green',
    'yellow', 'blue', 'blue', 'yellow', 'yellow', 'red', 'green', 'green',
    'red', 'red', 'red', 'red', 'green', 'red', 'green', 'yellow', 'red',
    'red', 'blue', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue',
    'blue', 'red', 'blue', 'blue', 'blue', 'yellow', 'red', 'green', 'blue',
    'blue', 'red', 'blue', 'red', 'green', 'black', 'yellow', 'blue', 'blue',
    'green', 'red', 'red', 'yellow', 'yellow', 'yellow', 'red', 'green',
    'green', 'yellow', 'blue', 'green', 'blue', 'blue', 'red', 'blue', 'green',
    'blue', 'red', 'green', 'green', 'blue', 'blue', 'green', 'red', 'blue',
    'blue', 'green', 'green', 'red', 'red', 'blue', 'red', 'blue', 'yellow',
    'blue', 'green', 'blue', 'green', 'yellow', 'yellow', 'yellow', 'red',
    'red', 'red', 'blue', 'blue'
]


def create_colorful_plot(**kwargs):
  create_plot(c=colors, **kwargs)


def main():
  create_colorful_plot()

  plt.show()


if __name__ == "__main__":
  main()
