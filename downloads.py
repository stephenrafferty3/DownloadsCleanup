import os, time
from pathlib import Path

current_time = time.time()

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
files = os.scandir(path_to_download_folder)

old_files = []

for file in files:
    print(file.name)
    e = os.stat(file)
    if e.st_mtime < current_time - (10 * 86400):
        print("old enough")
        old_files.append(file.name)
    else:
        print("not old enough.")

print(len(old_files))
print("**********Files to be deleted***************")
for i in old_files:
    print(i)
    try:
        os.remove(os.path.join(path_to_download_folder, i))
    except:
        print("Failed to delete: ", i)
