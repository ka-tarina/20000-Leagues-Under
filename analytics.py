import os


def get_word_freq(directory):
    if not directory:
        return
    all = {}
    try:
        for folder in os.listdir(directory):
            folder_path = os.path.join(directory, folder)
            for txt_file in os.listdir(folder_path):
                txt_path = os.path.join(folder_path, txt_file)
                with open(txt_path, "r") as f:
                    lines = f.readlines()
                    word_freq = {}
                    for line in lines:
                        words = line.split()
                        for word in words:
                            word = word.strip('.,!?"\'')
                            word = word.lower()
                            if word in word_freq:
                                word_freq[word] += 1
                            else:
                                word_freq[word] = 1
                    total_words = len(lines)
                    chapter = os.path.basename(folder_path)
                    all[chapter] = total_words
                    new_txt_file = os.path.join(folder_path, f'Analytics_{chapter}.txt')
                    with open(new_txt_file, "w") as f2:
                        for word in word_freq:
                            f2.write(f"{word}: {word_freq[word]/total_words}\n")
    except FileNotFoundError:
        print(f"Error: The directory {directory} was not found.")
    temp = ((value, key) for (key, value) in all.items())
    sorted_all = sorted(temp, reverse=True)
    final = [{k: v for v, k in sorted_all}]
    try:
        os.makedirs(os.path.join(directory, "all_analytics"))
        with open(os.path.join(directory, "all_analytics", "all_analytics.txt"), "w") as f3:
            for key, value in final[0].items():
                f3.write(f"{key}: {value}\n")
    except FileExistsError:
        print("Error: One or more of the specified directories already exist.")
