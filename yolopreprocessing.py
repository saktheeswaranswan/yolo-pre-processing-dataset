import os

def count_files_in_folder(folder_path, file_extensions):
    file_count = {ext: 0 for ext in file_extensions}

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            _, file_ext = os.path.splitext(filename)
            file_ext = file_ext.lower()

            if file_ext in file_extensions:
                file_count[file_ext] += 1

    return file_count

if __name__ == "__main__":
    folder_path = "/path/to/your/folder"
    file_extensions = ['.jpg', '.txt']

    file_count = count_files_in_folder(folder_path, file_extensions)

    for ext, count in file_count.items():
        print(f"Number of {ext} files: {count}")
