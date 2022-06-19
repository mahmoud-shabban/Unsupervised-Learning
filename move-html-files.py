import os
import shutil
for i in os.listdir('.'):
    if i.endswith('.html'):
        new_path = 'notebooks/' + i
        os.rename(i, new_path)