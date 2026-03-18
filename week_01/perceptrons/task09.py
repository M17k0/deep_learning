import numpy as np

from task08 import train_model, predict

nand_dataset = [(0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 0)]


def main():
  nand_w1, nand_w2, nand_b = train_model(nand_dataset)

  print("\nNAND predictions:")
  predict(nand_w1, nand_w2, nand_b, nand_dataset)
  print("w1:", nand_w1, "w2:", nand_w2, "b:", nand_b)


if __name__ == "__main__":
  main()
