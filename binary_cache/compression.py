import bz2
import zlib


def compress(data, format="bz2", callback=None):
    if format == "bz2":
        return bz2.compress(data, 9)
    elif format == "zlib":
        return zlib.compress(data, 9)
    elif callable(callback):
        return callback(data)
    else:
        raise Exception(
            "Compress format {} is not supported (supported format: bz2, zlib)".format(format))


def decompress(data, format="bz2", callback=None):
    if format == "bz2":
        return bz2.decompress(data)
    elif format == "zlib":
        return zlib.decompress(data, 9)
    elif callable(callback):
        return callback(data)
    else:
        raise Exception(
            "Decompress format {} is not supported (supported format: bz2, zlib)".format(format))
