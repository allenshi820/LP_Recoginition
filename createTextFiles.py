import pandas as pd
import os.path


df = pd.read_csv('test_set.txt',sep='\n',names=['filename','bbox'])
df2 = pd.read_csv('training_set.txt',sep='\n',names=['filename','bbox'])
test_df = pd.DataFrame({'filename':df['filename'].iloc[::2].values, 'bbox':df['filename'].iloc[1::2].values})
training_df = pd.DataFrame({'filename':df2['filename'].iloc[::2].values, 'bbox':df2['filename'].iloc[1::2].values})

save_path = '/home/kechiao/Desktop/FRCN/data/basketball/ImageSets/'
#create val.txt
f = open(save_path + "val.txt", "w+")
for i in range(len(test_df)):
    filen = test_df['filename'][i]
    start = filen.find('images/') + len('images/')
    name = filen[start:-4]
    f.write('n02802426_' + name + '\n')

f.close()

#create train.txt
f = open(save_path + 'train.txt', 'w+')
for i in range(len(training_df)):
    filen = training_df['filename'][i]
    start = filen.find('images/') + len('images/')
    name = filen[start:-4]
    f.write('n02802426_' + name + '\n')
f.close()

df = pd.concat([test_df,  training_df])
df.index = range(246)
save_path2 = '/home/kechiao/Desktop/FRCN/data/basketball/Annotations/'
for i in range(len(df)):
    filen = df['filename'][i]
    start = filen.find('images/') + len('images/')
    name = filen[start:-4]
    bboxs = df['bbox'][i]
    bbox = [int(e) for e in bboxs.split(',')]
    contents = '<annotation>\
                  <folder>{}</folder>\
                  <filename>{}</filename>\
                  <source>\
                    <database>ImageNet database</database>\
                  </source>\
                  <size>\
                    <width>640</width>\
                    <height>480</height>\
                    <depth>3</depth>\
                  </size>\
                  <segmented>0</segmented>\
                  <object>\
                    <name>{}</name>\
                    <pose>Unspecified</pose>\
                    <truncated>0</truncated>\
                    <difficult>0</difficult>\
                    <bndbox>\
                      <xmin>{}</xmin>\
                      <ymin>{}</ymin>\
                      <xmax>{}</xmax>\
                      <ymax>{}</ymax>\
                    </bndbox>\
                  </object>\
                </annotation>'.format('n02802426','n02802426_'+name,'n02802426',bbox[0],bbox[1],bbox[2],bbox[3])
    with open(save_path2 + 'n02802426_' + name +'.xml', 'w+') as f:
        f.write(contents)

