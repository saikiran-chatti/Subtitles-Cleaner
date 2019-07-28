import os
import shutil

source = os.getcwd()
des = source+'\subs'

try:
    if not os.path.exists(des):
        os.makedirs(des)
    else:
        print('There')
except OSError:
    print('OS Error')

files = os.listdir(source)

for i in files:
    if '.srt' in i:
        shutil.move(i,des)
