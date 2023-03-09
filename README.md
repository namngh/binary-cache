# Binary Cache

Cache data in binary file.

## Installation

Not supported yet.

## Usage

```python
from binary_cache import cache

data = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append(i * j)

    data.append(row)

binary_cache = cache.BinaryCache(
    serde_format="msgpack", compression_format="bz2")
binary_cache.save_file("cache.bin", data)

deserialized_data = binary_cache.load_file("cache.bin")
print(len(deserialized_data))
```

## Contributing

Pull requests are welcome. For major changes,
please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)