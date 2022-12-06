class Queue():
    def __init__(self, length) -> None:
        self.queue = []
        self.length = length

    def push(self, item):
        if len(self.queue) >= self.length:
            self.queue.pop(0)

        self.queue.append(item)

    def check_if_all_different(self):
        for item in self.queue:
            if self.queue.count(item) > 1:
                return False
        return True

    def get_length(self):
        return len(self.queue)


signal_queue = Queue(14)

with open("Day 6/input_signal.txt", "r") as Signal_File:
    signal = Signal_File.read()
    for count, letter in enumerate(signal):
        if signal_queue.get_length() >= signal_queue.length:
            if signal_queue.check_if_all_different():
                print(signal_queue.queue)
                break
        signal_queue.push(letter)

print(count)
