def parse_input(line):
    line = line.strip()
    if line.lower() in ["true", "false"]:
        return line.lower() == "true"
    try:
        return int(line)
    except ValueError:
        pass
    try:
        return float(line)
    except ValueError:
        pass
    return line

print(parse_input("3.14"))
print(parse_input("True"))
print(parse_input("hello"))
