import time


class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, args):
        date = time.strftime("%H:%M:%S", time.localtime())
        print(f'<{date}>: function {self.func.__name__} called with arguments {args}')
        start = time.time()
        self.func(args)
        end = time.time()
        diff = f"{end-start:01f}"
        print(f"Class-Decorator elapsed time = {diff} sec")
        f = open(f"{self.func.__name__}.html", 'w')
        f.write(f"<html><body>Время: {diff} секунд</body></html>")
