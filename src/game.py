class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total = 0
        i = 0
        for _ in range(10):
            first = self.rolls[i]
            if first == 10:
                total += 10 + self.rolls[i + 1] + self.rolls[i + 2]
                i += 1
                continue
            second = self.rolls[i + 1]
            if first + second == 10:
                total += 10 + self.rolls[i + 2]
            else:
                total += first + second
            i += 2
        return total
