import os
import pandas as pd
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

encoding='utf-8'
errors = 'ignore'
path = ".\\enron\\"
file_list = os.listdir(path)

base_df = pd.read_excel('.\\spam_ham_dataset.xlsx') #base_dataset
seq = base_df.shape[0] #row size of base_dataset

spam_label = 'spam'
spam_label_num = 1

ham_label = 'ham'
ham_label_num = 0

#load from enron data
#enron data has illegal character e.g. 0xbd(Hex)
#ILLEGAL_CHARACTERS_RE.sub(r'', text) remove of illegal chracter
seq_list = []
label_list = []
text_list = []
label_num_list = []
for p in file_list:
    ham_path = path + p + '\\ham\\'
    spam_path = path + p +'\\spam\\'
    
    ham_list = os.listdir(ham_path)
    spam_list = os.listdir(spam_path)

    for file in ham_list:
        text = ''
        str_list=[]
        with open(ham_path+file, 'rt', encoding=encoding, errors=errors) as f:
            for line in f:
                str_list.append(line)
        text = text.join(str_list)
        text = ILLEGAL_CHARACTERS_RE.sub(r'', text)

        seq_list.append(seq)
        label_list.append(ham_label)
        text_list.append(text)
        label_num_list.append(ham_label_num)

        seq += 1

    for file in spam_list:
        text = ''
        str_list=[]
        with open(spam_path+file, 'rt', encoding=encoding, errors=errors) as f:
            for line in f:
                str_list.append(line)
        text = text.join(str_list)
        text = ILLEGAL_CHARACTERS_RE.sub(r'', text)

        seq_list.append(seq)
        label_list.append(spam_label)
        text_list.append(text)
        label_num_list.append(spam_label_num)

        seq += 1

new_df = pd.DataFrame({
    'seq': seq_list,
    'label': label_list,
    'text': text_list,
    'label_num': label_num_list
})

#Concate base_df and new_df
res_df = pd.concat([base_df, new_df])

#Seperate spam and ham
spam_df = res_df[res_df['label_num'] == 1]
ham_df = res_df[res_df['label_num'] == 0]

#Test set size is 20% of dataset.
spam_cut = spam_df.shape[0]*8//10 
ham_cut = ham_df.shape[0]*8//10

training_spam_df = spam_df.iloc[0:spam_cut]
test_spam_df = spam_df.iloc[spam_cut:]

training_ham_df = ham_df.iloc[0:ham_cut]
test_ham_df = ham_df.iloc[ham_cut:]

training_df = pd.concat([training_spam_df, training_ham_df])
test_df = pd.concat([test_spam_df, test_ham_df])

training_df.to_excel('.\\input\\training.xlsx')
test_df.to_excel('.\\input\\test.xlsx')