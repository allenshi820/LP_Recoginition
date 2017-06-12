import pandas as pd
from PIL import Image

folder = ['boundingbox1/','boundingbox2/']



name = folder[0]
df = pd.read_csv(name + 'test_set.txt',sep='\n',names=['filename','bbox'])
df2 = pd.read_csv(name+'training_set.txt',sep='\n',names=['filename','bbox'])
test_df = pd.DataFrame({'filename':df['filename'].iloc[::2].values, 'bbox':df['filename'].iloc[1::2].values})
training_df = pd.DataFrame({'filename':df2['filename'].iloc[::2].values, 'bbox':df2['filename'].iloc[1::2].values})

for i in range(len(test_df)):
    filen = test_df['filename'][i]
    bboxstring  = test_df['bbox'][i]
    bbox = [int(x) for x in bboxstring.split(',')]
    img = Image.open(name+'/' + filen)
    img2 = img.crop(bbox)
    start = filen.find('images/') + len('images/')
    save_file = name + 'cropped_images/' + filen[start:-4] + '_lp.jpg'
    img2.save(save_file)
for i in range(len(training_df)):
    filen = training_df['filename'][i]
    bboxstring  = training_df['bbox'][i]
    bbox = [int(x) for x in bboxstring.split(',')]
    img = Image.open(name+'/' + filen)
    img2 = img.crop(bbox)
    start = filen.find('images/') + len('images/')
    save_file = name + 'cropped_images/' + filen[start:-4] + '_lp.jpg'
    img2.save(save_file)

name = folder[1]
df = pd.read_csv(name + 'labels.info',sep='\n',names=['filename'])
new_df = pd.DataFrame({'filename':df['filename'].iloc[::3].values, 'bbox':df['filename'].iloc[1::3].values})

for i in range(len(new_df)):
    filen = new_df['filename'][i]
    bboxstring  = new_df['bbox'][i]
    bbox = [int(x) for x in bboxstring.split(',')]
    img = Image.open(name+'/' + filen)
    img2 = img.crop(bbox)
    start = filen.find('cropped/') + len('cropped/')
    save_file = name + 'cropped_images/' + filen[start:-4] + '_lp.jpg'
    img2.save(save_file)
