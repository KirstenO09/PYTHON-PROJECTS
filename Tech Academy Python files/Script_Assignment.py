import os

def listTextFiles():
    directory = r'D:\Python\Tech Academy Python files\Script_Assignment'

    folder = os.listdir(directory)

    for file in folder:
        if file.endswith('.txt'):
            full_path = os.path.join(directory, file)
            time = os.path.getmtime(full_path)
            print(file, '-', time)


if __name__ == "__main__":
    listTextFiles()
