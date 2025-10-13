def convert_dict_types(d):
    def convert(val):
        for t in (int, float):
            try:
                return t(val)
            except ValueError:
                continue
        if val.lower() in ["true", "false"]:
            return val.lower() == "true"
        return val
    return {k: convert(v) for k, v in d.items()}

# Example
print(convert_dict_types({"a": "123", "b": "3.14", "c": "True"}))
