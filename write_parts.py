import os


def divide_file(path):
    try:
        with open(path, "r") as f:
            part1, part2 = f.read().split("PART TWO")
    except FileNotFoundError:
        print(f"Error: The file {path} was not found.")
        part1, part2 = None, None
    return part1, part2


def write_parts(part1, part2):
    try:
        with open("part1.txt", "w") as f1:
            f1.write(part1)
        with open("part2.txt", "w") as f2:
            f2.write(part2)
    except PermissionError:
        print("Error: You have no permission to write to the specified files.")


def delete_parts():
    if os.path.exists("part1.txt"):
        os.remove("part1.txt")
    if os.path.exists("part2.txt"):
        os.remove("part2.txt")
