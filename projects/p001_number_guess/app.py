import random


class Game:
    def __init__(self, low: int = 1, high: int = 100, tries: int = 7) -> None:
        if low >= high:
            raise ValueError("low must be < high")
        if tries <= 0:
            raise ValueError("tries must be > 0")
        self.low = low
        self.high = high
        self.tries = tries
        self.secret = random.randint(low, high)

    def guess(self, value: int) -> str:
        if value < self.secret:
            return "higher"
        if value > self.secret:
            return "lower"
        return "correct"