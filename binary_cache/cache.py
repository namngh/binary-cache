import msgpack
import bz2
from binary_cache import serde, compression


class BinaryCache:
    def __init__(self, **kwargs):
        self.serde_format = kwargs.get("serde_format", "json")
        self.serde_callback = kwargs.get("serde_callback")
        self.compression_format = kwargs.get("compression_format", "bz2")
        self.compression_callback = kwargs.get("compression_callback")

    def save_file(self, file_path, data):
        serialized_data = serde.serialize(
            data, format=self.serde_format, callback=self.serde_callback)
        compressed_data = compression.compress(
            serialized_data, format=self.compression_format, callback=self.compression_callback)

        with open(file_path, "wb") as f:
            f.write(compressed_data)

    def load_file(self, file_path):
        with open(file_path, "rb") as f:
            data = f.read()

            decompress_data = compression.decompress(
                data, format=self.compression_format, callback=self.compression_callback)
            deserialized_data = serde.deserialize(
                decompress_data, format=self.serde_format, callback=self.serde_callback)

            return deserialized_data
