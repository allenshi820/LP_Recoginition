#go through each file in JPEGImages, copy name and set bounding box == 0,0,0,0
import pandas as pd
import numpy as np
import glob
import os

filenames = glob.glob('JPEGImages/*.jpg')

save_path = '/home/kechiao/Desktop/FRCN/data/basketball/ImageSets/'
f = open(save_path + "val.txt", "w+")
for i in range(len(filenames)):
    filen = filenames[i][11:-4]
    f.write(filen + '\n')

f.close()


save_path2 = '/home/kechiao/Desktop/FRCN/data/basketball/Annotations/'
for i in range(len(filenames)):
    name = filenames[i][11:-4]
    bbox = [150,150,180,180]
    contents = '<annotation>\
                  <folder>{}</folder>\
                  <filename>{}</filename>\
                  <source>\
                    <database>ImageNet database</database>\
                  </source>\
                  <size>\
                    <width>896</width>\
                    <height>592</height>\
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
                </annotation>'.format('n02802426',name,'n02802426',bbox[0],bbox[1],bbox[2],bbox[3])
    with open(save_path2 + name +'.xml', 'w+') as f:
        f.write(contents)
