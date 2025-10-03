class FileManager:
    """Context manager to handle file open and close automatically"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"An error occurred: {exc_val}")
        return True  # prevents program from crashing


with FileManager("basha1.txt", "w") as f:
    f.write("Hello, this is written using a custom context manager!\n")

with FileManager("basha1.txt", "r") as f:
    print(f.read())
