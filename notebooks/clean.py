import os

for i in os.listdir('.'):
    if i.endswith('.html'):
        os.rename(i,i[9:])
