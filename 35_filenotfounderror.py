def read_file_safe(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: '{filename}' not found!"

print(read_file_safe("basha1.txt"))
print(read_file_safe("missing.txt"))
