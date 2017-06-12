import pandas as pd
import os.path


df = pd.read_csv('test_set.txt',sep='\n',names=['filename','bbox'])
df2 = pd.read_csv('training_set.txt',sep='\n',names=['filename','bbox'])
test_df = pd.DataFrame({'filename':df['filename'].iloc[::2].values, 'bbox':df['filename'].iloc[1::2].values})
training_df = pd.DataFrame({'filename':df2['filename'].iloc[::2].values, 'bbox':df2['filename'].iloc[1::2].values})

save_path = '/home/kechiao/Desktop/LPR/Attention-OCR/'
#create val.txt
f = open(save_path + "val.txt", "w+")
for i in range(len(test_df)):
    filen = test_df['filename'][i]
    start = filen.find('images/') + len('images/')
    name = filen[start:]
    f.write('JPEGImages/n02802426_' + name + '\n')

f.close()
print('done val')
#create train.txt
f = open(save_path + 'train.txt', 'w+')
for i in range(len(training_df)):
    filen = training_df['filename'][i]
    start = filen.find('images/') + len('images/')
    name = filen[start:]
    f.write('JPEGImages/n02802426_' + name + '\n')
f.close()
print('done train')
