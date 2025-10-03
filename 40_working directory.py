#context manager that temporarily changesthe working directory   


import os

class ChangeDirectory:
    """Context manager to temporarily change the working directory"""
    def __init__(self, new_path):
        self.new_path = new_path
        self.saved_path = None

    def __enter__(self):
        self.saved_path = os.getcwd()   # save current directory
        os.chdir(self.new_path)         # change to new directory
        return self.new_path

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.saved_path)       # go back to original directory
        if exc_type:
            print(f"An error occurred: {exc_val}")
        return True  # prevents crash

# Example usage
print("Before:", os.getcwd())

with ChangeDirectory("C:\\"):   # 👉 change this path based on your system
    print("Inside context:", os.getcwd())

print("After:", os.getcwd())
