class LZ11:

    @staticmethod
    def is_compressed(data: bytes):
        return len(data) > 4 and data[0] == 0x11
