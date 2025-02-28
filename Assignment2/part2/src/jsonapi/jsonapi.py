import json

"""
Code studyied and used from https://mathspp.com/blog/custom-json-encoder-and-decoder
"""


class ExtendedEncoder(json.JSONEncoder):
    def default(self, obj):
        name = type(obj).__name__
        try:
            encoder = getattr(self, f"encode_{name}")
        except AttributeError:
            super().default(obj)
        else:
            encoded = encoder(obj)
            encoded["__extended_json_type__"] = name
            return encoded

class ExtendedDecoder(json.JSONDecoder):
    def __init__(self, **kwargs):
        kwargs["object_hook"] = self.object_hook
        super().__init__(**kwargs)
    
    def object_hook(self, obj):
        try:
            name = obj["__extended_json_type__"]
            decoder = getattr(self, f"decode_{name}")
        except (KeyError, AttributeError):
            return obj
        else:
            return decoder(obj)

def dumps(*args, **kwargs):
    result = json.dumps(*args, **kwargs)
    return result

def loads(*args, **kwargs):
    result = json.loads(*args, **kwargs)
    return result
