import numpy as np
import librosa
import os
import time
from multiprocessing import Process, current_process
NULL_PATH = "id00012"

def check_folder(new_path, our_folder):
    procs = []
    print(current_process().name)
    for filename in os.listdir(new_path):
        os.chdir(new_path)
        if os.path.isdir(os.path.abspath(filename)):
            new_folder = our_folder + '\\'
            new_folder = new_folder + filename
            os.makedirs(new_folder)
            full_path = os.path.abspath(filename)
            proc = Process(target=check_folder,name = filename, args=(full_path, new_folder,))
            procs.append(proc)
            proc.start()
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
    print(procs)
    for proc in procs:
        proc.join()
start_time = time.time()
os.chdir('C:\\Users\\osbel\\Desktop')
answer = os.getcwd() + '\\test'
os.mkdir(answer)
check_folder(os.path.abspath(NULL_PATH), answer)
print("Time: {}".format(time.time() - start_time))
