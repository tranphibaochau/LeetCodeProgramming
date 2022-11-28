import random


class Puzzle():
    def __init__(self):
        self.cells = {}
        self.prisoner_list = [i for i in range(1, 101)]

    def assign_nums(self):
        # shuffle the prisoners first before putting them in the boxes
        random.shuffle(self.prisoner_list)
        for i in range(1, 101):
            self.cells[i] = self.prisoner_list[i - 1]

    def solve(self):
        for p in self.prisoner_list:
            chosen = p  # choose the cell with your own number first
            # each prisoner has 50 tries
            for trial in range(50):
                # pick the number inside the box until it matches the prisoner number
                if self.cells[chosen] != p:
                    chosen = self.cells[chosen]
                else:
                    break
            # if after the loop, the prisoner cannot find his own number, then everyone fails
            # otherwise, move on to the next person
            if self.cells[chosen] != p:
                return False
        return True


trials = []
for i in range(1000000):
    puzzle = Puzzle()
    puzzle.assign_nums()
    trials.append(puzzle.solve())
print("Success rate:", sum(trials) / len(trials))
