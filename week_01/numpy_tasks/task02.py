import numpy as np

from week_01.numpy_tasks.datasets import baseball_dataset, baseball_dataset_corrected

COLUMNS = ['Height', 'Weight', 'Age']


def mean_for_column(data, column_index):
  column_values = data[:, column_index]
  mean_value = np.mean(column_values)
  return mean_value


def median_for_column(data, column_index):
  column_values = data[:, column_index]
  median_value = np.median(column_values)
  return median_value


def std_for_column(data, column_index):
  column_values = data[:, column_index]
  std_value = np.std(column_values)
  return std_value


def print_statistics(data, column_index):
  mean_value = mean_for_column(data, column_index)
  median_value = median_for_column(data, column_index)
  std_value = std_for_column(data, column_index)

  print(f'Summary statistics for column {COLUMNS[column_index]}:')
  print(f'Mean: {mean_value}')
  print(f'Median: {median_value}')
  print(f'Standard Deviation: {std_value}')


def main():
  np_baseball = np.array(baseball_dataset)
  print(f'Number of rows and columns: {np_baseball.shape}')
  print_statistics(np_baseball, 0)
  print_statistics(np_baseball, 1)
  print_statistics(np_baseball, 2)

  print('-------------------------------------------')
  # Q: Is there anything abnormal about the data MLB sent you?
  # A: 21 values for the height column are incorrect. There are players with height more than 70000 inches
  print('Number of players more than 70000 inches tall:',
        np.sum(np_baseball[:, 0] > 70000))
  print('-------------------------------------------')

  print('After data correction:')
  np_baseball_corrected = np.array(baseball_dataset_corrected)
  print(f'Number of rows and columns: {np_baseball_corrected.shape}')
  print_statistics(np_baseball_corrected, 0)
  print_statistics(np_baseball_corrected, 1)
  print_statistics(np_baseball_corrected, 2)

  print('-------------------------------------------')
  # Q: Do big players tend to be heavier?
  # A: Yes, there is a positive correlation between height and weight. The correlation coefficient is 0.53.
  height = np_baseball_corrected[:, 0]
  weight = np_baseball_corrected[:, 1]
  correlation = np.corrcoef(height, weight)
  if correlation[0, 1] > 0.5:
    print('There is a positive correlation between height and weight.')
  elif correlation[0, 1] < -0.5:
    print('There is a negative correlation between height and weight.')


if __name__ == '__main__':
  main()
