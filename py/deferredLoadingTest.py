class MyClass:

    def __init__(self, filename='test.txt'):
        self._MyText:
            string = None
        self.filename:
            string = filename

    @property
    def MyText(self):
        if not self._MyText:
            with open(self.filename, 'r') as f:
                self._MyText = f.read()
        return self._MyText

    @MyText.setter
    def MyText(self, value):
        self._MyText = value


def add(a: int, b: int) -> int:
    return a + b
