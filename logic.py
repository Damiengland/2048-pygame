import numpy as np
import random

# Rows and Cols
RC = 4

# Build Grid
# box_index = np.where(grid == 0)
# pos = list(zip(box_index[0], box_index[1]))
# print(pos)


class Logic:

    def __init__(self):
        # Generate 4x4 Array of Zeros
        self.grid = np.zeros((RC, RC))

    def generate_num(self, k=1):
        box_index = np.where(self.grid == 0)
        pos = list(zip(box_index[0], box_index[1]))

        for p in random.sample(pos, k=k):
            if random.random() < 0.15:
                self.grid[p] = 4
            else:
                self.grid[p] = 2

    def make_move(self, move):

        for i in range(RC):

            flipped = False

            if move in "lr":
                boxes = self.grid[i, :]
            else:
                boxes = self.grid[:, i]

            if move in "rd":
                flipped = True
                boxes = boxes[::-1]

            filled_boxes = boxes[boxes != 0]
            merged_boxes = []
            skip = False

            for j in range(len(filled_boxes)):

                if skip:

                    skip = False
                    continue

                if j != len(filled_boxes) - 1 and filled_boxes[j] == filled_boxes[j + 1]:

                    n_sum = filled_boxes[j] * 2
                    merged_boxes.append(n_sum)
                    skip = True

                else:

                    merged_boxes.append(int(filled_boxes[j]))

            new_grid = np.zeros_like(boxes)
            new_grid[:len(merged_boxes)] = np.array(merged_boxes)

            if flipped:
                new_grid = new_grid[::-1]

            if move in "lr":
                self.grid[i, :] = new_grid
            else:
                self.grid[:, i] = new_grid

    def play(self, cmd):

        old_grid = self.grid.copy()
        self.make_move(move=cmd)

        if all((self.grid == old_grid).flatten()):
            return

        self.generate_num(k=1)

    def play_console(self):

        self.generate_num(k=2)

        while True:

            print(self.grid)

            cmd = input("Choose a Direction: ")

            if cmd == "q":
                break

            old_grid = self.grid.copy()
            self.make_move(move=cmd)

            if all((self.grid == old_grid).flatten()):
                continue

            self.generate_num(k=1)


if __name__ == "__main__":
    game = Logic()
    game.play_console()
