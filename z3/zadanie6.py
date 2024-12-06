class ToUpper(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result.upper()

@ToUpper
def print_text():
    return "Jestem Maciej"

print(print_text())