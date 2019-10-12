import numpy as np
import librosa
import os
import time
from threading import Thread
NULL_PATH = "id00012"
def check_folder(new_path, our_folder):
    for filename in os.listdir(new_path):
        os.chdir(new_path)
        if os.path.isdir(os.path.abspath(filename)):
            new_folder = our_folder + '\\'
            new_folder = new_folder + filename
            os.makedirs(new_folder)
            full_path = os.path.abspath(filename)
            t1 = Thread(target=check_folder, args = (full_path, new_folder,))
            t1.start()
            t1.join()
            continue
        ext = filename[filename.rfind(".") + 1:]
        if ext == 'm4a':
            os.rename(filename, filename[0:filename.rfind(".") + 1:] + 'ogg')
            filename = filename[0:filename.rfind(".") + 1:] + 'ogg'
            ext = 'ogg'
        if ext == 'ogg':
            x , sr = librosa.load(os.path.abspath(filename))
            mfcc = librosa.feature.mfcc(x, sr)
            new_folder = our_folder + '\\'
            new_folder = new_folder + filename
            np.save(new_folder, mfcc)
start_time = time.time()
os.chdir('C:\\Users\\osbel\\Desktop')
answer = os.getcwd() + '\\test'
os.mkdir(answer)
check_folder(os.path.abspath(NULL_PATH), answer)
print("Time: {}".format(time.time() - start_time))
