import random

class AI:
    def __init__(self, memory: int, pattern: int):
        self.history = []

        self.memory = memory
        self.pattern = pattern

    def append(self, s: int):
        self.history.append(s)

        if len(self.history) > len(self.pattern):
            self.history.pop(0)

    def win(self, s: int) -> int:
        return (s+1)%3
    
    def res(self, a: int, b: int) -> int:
        if a == self.win(b): return 0
        if a == b:           return 1
        return 2
    
    def predict(self) -> int:
        check_len = min(len(self.history), self.pattern)
        check_pattern = self.history[-check_len:]

        # ah yes, O(n^3) complexity
        while check_len > 0:
            for i in range(len(self.history) - check_len + 1):
                match = True
                for j in range(check_len):
                    if self.history[i+j] != check_pattern[j]:
                        match = False
                        break
                if match and i+check_len < len(self.history):
                    return self.win(self.history[i+check_len])

            check_len -= 1
            check_pattern.pop(0)

        return random.randint(0, 2)