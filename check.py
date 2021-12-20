import os
import chardet

path = '.\\enron\\'
file_list = os.listdir(path)
to_remove = []

for p in file_list:
    ham_path = path + p + '\\ham\\'
    spam_path = path + p +'\\spam\\'

    ham_list = os.listdir(ham_path)
    spam_list = os.listdir(spam_path)

    for file in ham_list:
        with open(ham_path + file, 'rb') as f:
            result = chardet.detect(f.readline())  # or read() if the file is small.
            
            if(result['encoding'] != 'ascii'):
                to_remove.append(ham_path + file)

    for file in spam_list:
        with open(spam_path + file, 'rb') as f:
            result = chardet.detect(f.readline())  # or read() if the file is small.
            if(result['encoding'] != 'ascii'):
                to_remove.append(spam_path + file)

for p in to_remove:
    os.remove(p)


