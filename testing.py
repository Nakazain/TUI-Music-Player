import os

os.chdir("/run/media/nakazain/ES CAMPUR")

for dirpath, dirnames, filenames in os.walk("/run/media/nakazain/ES CAMPUR"):
    print('curent_path: ', dirpath)
    print('directories: ', dirnames)
    for filenames in os.listdir(dirpath):
        if filenames.endswith('.flac'):
            print('Musik: ',filenames)