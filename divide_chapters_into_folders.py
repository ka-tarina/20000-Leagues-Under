import os


def read_parts(part_1_path, part_2_path):
    try:
        with open(part_1_path, "r") as f1:
            part_one = f1.readlines()
        with open(part_2_path, "r") as f2:
            part_two = f2.readlines()
    except FileNotFoundError:
        print(f"Error: One or both of the files {part_1_path} and {part_2_path} were not found.")
        part_one, part_two = None, None
    return part_one, part_two


def divide_chapters(parts):
    chapters_1 = []
    chapters_2 = []
    if parts[0] is None or parts[1] is None:
        return chapters_1, chapters_2
    for part in parts:
        counter_ch = 0
        if part == parts[0]:
            for line in part:
                if line != "\n" and line.split()[0] == "CHAPTER":
                    counter_ch += 1
                    chapters_1.append("CHAPTER_" + str(counter_ch))
                else:
                    continue
        if part == parts[1]:
            for line in part:
                if line != "\n" and line.split()[0] == "CHAPTER":
                    counter_ch += 1
                    chapters_2.append("CHAPTER_" + str(counter_ch))
                else:
                    continue
    return chapters_1, chapters_2


def create_folders(chapters):
    if chapters[0] is None or chapters[1] is None:
        return
    try:
        os.mkdir("20000 leagues under")
        os.chdir("20000 leagues under")
        os.mkdir("part 1")
        os.mkdir("part 2")
        [os.mkdir(os.path.join("part 1", i))for i in chapters[0]]
        [os.mkdir(os.path.join("part 2", i)) for i in chapters[1]]
    except FileExistsError:
        print("Error: One or more of the specified directories already exist.")


def create_chapter_files(input_file, output_path):
    if not input_file or not output_path:
        return
    try:
        current_chapter = ""
        folder_name = ""
        with open(input_file) as infile:
            counter = 0
            for line in infile:
                if line.startswith("CHAPTER"):
                    current_chapter = ""
                    counter += 1
                    folder_name = "CHAPTER_" + str(counter)
                    chapter_name = next(infile).strip()
                    current_chapter += chapter_name
                    if current_chapter:
                        with open(os.path.join(output_path,
                                               folder_name, chapter_name + ".txt"), "w") as outfile:
                            pass
                else:
                    if current_chapter != "":
                        with open(os.path.join(output_path,
                                               folder_name, chapter_name + ".txt"), "a") as outfile:
                            outfile.write(line)
    except PermissionError:
        print("Error: You do not have permission to write to the specified files.")
