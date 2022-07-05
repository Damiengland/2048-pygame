import numpy as np
import random

N = 4


class Logic:

    def __init__(self):
        self.grid = np.zeros((N, N))

    def new_number(self, k=1):
        grid_pos = list(zip(* np.where(self.grid == 0)))

        # Selects two random positions in the grid an assigns the value to 2
        for pos in random.sample(grid_pos, k=k):
            if random.random() < 0.1:
                self.grid[pos] = 4
            else:
                self.grid[pos] = 2

    @staticmethod
    def _get_nums(boxes):
        box_n = boxes[boxes != 0]
        box_num_sum = []
        #  Skip a single loop
        skip = False
        for j in range(len(box_n)):
            if skip:
                skip = False
                continue
            if j != len(box_n) - 1 and box_n[j] == box_n[j + 1]:
                new_n = box_n[j] * 2
                skip = True
            else:
                new_n = box_n[j]

            box_num_sum.append(new_n)

        return np.array(box_num_sum)

    def make_move(self, move):

        for i in range(N):

            flipped = False

            if move in "lr":
                box = self.grid[i, :]
            else:
                box = self.grid[:, i]

            if move in "rd":
                flipped = True
                box = box[::-1]

            box_num = self._get_nums(box)

            new_grid = np.zeros_like(box)
            new_grid[:len(box_num)] = box_num

            if flipped:
                new_grid = new_grid[::-1]

            if move in 'lr':
                self.grid[i, :] = new_grid
            else:
                self.grid[:, i] = new_grid

    def play(self):
        self.new_number(k=2)
        while True:

            print(self.grid)

            cmd = input("what's your move?")

            if cmd == "q":
                break
            old_grid = self.grid.copy()

            self.make_move(cmd)
            if all((self.grid == old_grid).flatten()):
                continue
            self.new_number(k=1)


if __name__ == "__main__":
    game = Logic()
    game.play()
