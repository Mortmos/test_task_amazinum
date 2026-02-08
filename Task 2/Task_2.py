import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

MATRIX_SIZE = 26
STEPS = 20
COLORS = ['#CCCCCC', '#2D7D2D']
CMAP = ListedColormap(COLORS)


class MATRIX:
    def __init__(self, size=MATRIX_SIZE):
        self.size = size
        self.matrix = np.random.randint(0, 2, (size, size))

    def count_live_neighbors(self, x, y):
        neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        count = 0
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                count += self.matrix[nx, ny]
        return count

    def next_gen(self):
        new_matrix = np.zeros((self.size, self.size), dtype=int)

        for i in range(self.size):
            for j in range(self.size):
                live_neighbors = self.count_live_neighbors(i, j)

                if self.matrix[i, j] == 1:
                    if live_neighbors in [2, 3]:
                        new_matrix[i, j] = 1
                    else:
                        new_matrix[i, j] = 0
                else:
                    if live_neighbors == 3:
                        new_matrix[i, j] = 1

        self.matrix = new_matrix

    def out_matrix(self, title):
        plt.figure(figsize=(7, 7))
        plt.title(title)
        plt.imshow(self.matrix, cmap=CMAP, interpolation='nearest')
        plt.axis('off')
        plt.show()

    def out_print(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))


def main():
    task = MATRIX(MATRIX_SIZE)

    print("Initial Matrix:")
    task.out_print()
    task.out_matrix("Initial Matrix")

    for i in range(1, STEPS + 1):
        task.next_gen()

        title = f"Step {i}" if i < STEPS else "Final Matrix"
        task.out_matrix(title)

    print("\nFinal Matrix after 20 steps:")
    task.out_print()


if __name__ == '__main__':
    main()