import os
from shutil import move

src = "C:\\ALL IN ONE\\Movies"
dst = "C:\\ALL IN ONE\\Temp Folder"
exc = "C:\\ALL IN ONE\\Excess Folders"
num_files = 0
# The src is the absolute path while the root is the relevant path, which is what we need


def sort(movie_file, root_file):                             # Moves all the files into the temporary folder
    if movie_file.lower().strip().endswith(("mp4", "mkv", "mpeg")):
        global num_files
        num_files += 1
        path = os.path.join(root_file, movie_file)
        move(path, dst)
        return print(f"Moving file:  {movie_file[:10]}...\tto\t\t\t\t\t{src}")


def re_sort(mv_file):                                        # Moves the files back to the src
    path = os.path.join(dst, mv_file)
    move(path, src)


def sort_sub_folders():
    for rootA, dirsA, filesA in os.walk(src):                   # Moves all the empty sub folders into a specific folder
        for folder in dirsA:
            path = os.path.join(rootA, folder)
            move(path, exc)
    move(dst, exc)                                           # Moves the empty Temporary Folder to the Excess Folder
    return print(f"\nMoved a total of {num_files} files \n//////////////////////////////////////")


if __name__ == "__main__":
    if not os.path.exists(dst):
        os.makedirs(dst)
    if not os.path.exists(exc):
        os.makedirs(exc)

    for root, dirs, files in os.walk(src):
        for file in files:
            sort(file, root)

    for mov_file in os.listdir(dst):
        re_sort(mov_file)

    sort_sub_folders()
