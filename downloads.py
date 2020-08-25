import os
import time
from pathlib import Path

current_time = time.time()

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
files = os.scandir(path_to_download_folder)

old_files = []


def delete():
    days = input("Files older than how many days will be deleted?: ")
    for file in files:
        print(file.name)
        e = os.stat(file)
        if e.st_mtime < current_time - (int(days) * 86400):
            try:
                os.remove(os.path.join(path_to_download_folder, i))
            except:
                print("Failed to delete: ", file)


if __name__ == "__main__":
    delete()
