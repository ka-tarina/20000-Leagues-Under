from write_parts import divide_file, write_parts, delete_parts
from divide_chapters_into_folders import read_parts, divide_chapters, create_folders, create_chapter_files
from analytics import get_word_freq
import os


def main():
    cwd = os.getcwd()

    file_path = os.path.join(cwd, "20000leagues-under-Jules-Verne.txt")

    part1, part2 = divide_file(file_path)

    write_parts(part1, part2)

    part_1_txt_path = os.path.join(cwd, "part1.txt")
    part_2_txt_path = os.path.join(cwd, "part2.txt")

    part_1, part_2 = read_parts(part_1_txt_path, part_2_txt_path)

    parts = [part_1, part_2]

    chapters = divide_chapters(parts)
    create_folders(chapters)

    folder_part_1 = os.path.join(cwd, "20000 leagues under/part 1")
    folder_part_2 = os.path.join(cwd, "20000 leagues under/part 2")

    create_chapter_files(part_1_txt_path, folder_part_1)
    create_chapter_files(part_2_txt_path, folder_part_2)

    get_word_freq(folder_part_1)
    get_word_freq(folder_part_2)

    delete_parts()


if __name__ == "__main__":
    main()
