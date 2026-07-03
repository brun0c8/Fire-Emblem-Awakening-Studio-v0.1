from pathlib import Path

class GameFile:
    def __init__(self, filename):
        self.path = Path(filename)
        self.data = self.path.read_bytes()

    @property
    def size(self):
        return len(self.data)

    @property
    def extension(self):
        return self.path.suffix.lower()

    def magic(self, size=16):
        return self.data[:size]

    def is_lz11(self):
        return self.data and self.data[0] == 0x11
