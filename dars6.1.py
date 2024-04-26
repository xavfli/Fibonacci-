class Fibonacci:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

# 10 ta Fibonacci sonini chiqarish:
fib = Fibonacci()
for _ in range(10):
    print(next(fib))
