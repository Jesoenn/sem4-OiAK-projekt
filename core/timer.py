import time

class Timer:
    def __init__(self):
        self.time = 0.00
        self.start_time = 0

    def start(self):
        """Start measuring time and reset timer"""
        self.start_time = time.perf_counter()
        self.time = 0.00

    def stop(self):
        """Stop timer, [ms], 2 precision"""
        if self.start_time != 0:
            self.time = (time.perf_counter() - self.start_time) * 1000  # konwersja na ms
            self.time = round(self.time, 3)
            self.start_time = 0
