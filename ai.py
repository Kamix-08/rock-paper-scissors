import random

class ai:
    def __init__(self, memory: int, pattern: int, p: float = 2.0):
        self.history = []

        self.memory = memory
        self.pattern = pattern

        self.P = p

    def append(self, s: int):
        self.history.append(s)

        if len(self.history) > len(self.pattern):
            self.history.pop(0)

    def win(s: int) -> int:
        return (s+2)%3
    
    def predict(self) -> int:
        check_len = min(len(self.history) - 1, self.pattern)
        check_pattern = self.history[-check_len:]
        votes = [0, 0, 0]

        # ah yes, O(n^3) complexity
        while check_len > 0:
            for i in range(len(self.history) - check_len + 1):
                match = True
                for j in range(check_len):
                    if self.history[i+j] != check_pattern[j]:
                        match = False
                        break
                if match:
                    votes[self.win(self.history[i+check_len])] += check_len ** self.P

            check_len -= 1

        max_votes = max(votes)
        candidates = [index for index, vote in enumerate(votes) if vote == max_votes]
        return random.choice(candidates)