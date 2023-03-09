import yaml
import json
import msgpack


def serialize(data, format="json", callback=None):
    if format == "msgpack":
        return msgpack.packb(data, use_bin_type=True)
    elif format == "json":
        return json.dumps(data)
    elif format == "yaml":
        return yaml.dump(data)
    elif callable(callback):
        return callback(data)
    else:
        raise Exception(
            "Serialized format {} is not supported (supported format: msgpack, json, yaml)".format(format))


def deserialize(data, format="json", callback=None):
    if format == "msgpack":
        return msgpack.unpackb(data, raw=False)
    elif format == "json":
        return json.loads(data)
    elif format == "yaml":
        return yaml.load(data, Loader=yaml.FullLoader)
    elif callable(callback):
        return callback(data)
    else:
        raise Exception(
            "Deserialized format {} is not supported (supported format: msgpack, json, yaml)".format(format))
