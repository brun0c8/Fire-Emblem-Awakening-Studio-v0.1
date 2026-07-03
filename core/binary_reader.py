import struct


class BinaryReader:

    def __init__(self, data: bytes):
        self.data = data
        self.pos = 0

    def seek(self, offset):
        self.pos = offset

    def tell(self):
        return self.pos

    def read(self, size):
        value = self.data[self.pos:self.pos + size]
        self.pos += size
        return value

    def u8(self):
        return struct.unpack("<B", self.read(1))[0]

    def u16(self):
        return struct.unpack("<H", self.read(2))[0]

    def u32(self):
        return struct.unpack("<I", self.read(4))[0]

    def string(self, size):
        return self.read(size).decode("ascii", "ignore").rstrip("\0")
