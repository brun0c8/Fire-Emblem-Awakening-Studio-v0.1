import re

from core.logger import info


class Inspector:

    def __init__(self, data):
        self.data = data

    def strings(self):

        print("ASCII")

        for s in re.findall(rb"[ -~]{4,}", self.data):

            try:
                print(s.decode())
            except:
                pass

        print("\nUTF16")

        for s in re.findall(rb"(?:[\x20-\x7E]\x00){4,}", self.data):

            try:
                print(s.decode("utf-16le"))
            except:
                pass

    def mids(self):

        ids = re.findall(rb"MID_[A-Za-z0-9_]+", self.data)

        for i in ids:
            print(i.decode())
