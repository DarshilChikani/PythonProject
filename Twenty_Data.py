import os
import shutil

src_files = os.listdir(r'C:\NewDrive\0PG College\Python 2\Project data\color_train/')
arrFolder = [0]*len(src_files);


parent_dir = r"C:\NewDrive\0PG College\Python 2\Project data\color_val/"
for i in range(0, len(src_files)):
    # Path
    path = os.path.join(parent_dir, src_files[i])
    os.makedirs(path)



for i in range(0, len(src_files)):
    src_files1 = os.listdir(r'C:\NewDrive\0PG College\Python 2\Project data\color_train/'+src_files[i])
    #print(src_files1)
    templen = round(0.2 * len(src_files1)) #20% data
    print(templen)
    for j in range(0, templen):
        shutil.move(r"C:\NewDrive\0PG College\Python 2\Project data\color_train/"+src_files[i]+"/"+src_files1[j], r"C:\NewDrive\0PG College\Python 2\Project data\color_val/"+src_files[i])

