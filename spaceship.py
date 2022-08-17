# Represents a spaceship.

class Spaceship:
    def __init__(self, p, w, h):
        self.p = p
        self.w = w
        self.h = h

class Failure:
    def __init__(self, dep):
        self.d = dep

def evaluate(s):
    if isinstance(s, Spaceship):
        return 2 ** (s.p * s.w) * s.h
    elif isinstance(s, Failure):
        return 2 ** (300 - s.d)
