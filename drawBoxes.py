import _init_paths
from fast_rcnn.config import cfg
from fast_rcnn.test import im_detect
from fast_rcnn.nms_wrapper import nms
from utils.timer import Timer
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import caffe, os, sys, cv2
import argparse
import pickle

lis = []
thresh = 0.1
dets = pickle.load(open('detections.pkl', 'rb'))
det = dets[1]
img_path = '/home/kechiao/Desktop/FRCN/data/basketball/JPEGImages/'
with open('/home/kechiao/Desktop/FRCN/data/basketball/ImageSets/val.txt', 'r') as f:
    content = f.readlines()
lis = [x.strip() for x in content]

"""Draw detected bounding boxes."""

for i in range(10):
    im_file = os.path.join(img_path +lis[i] + '.jpg')
    im = cv2.imread(im_file)
    im = im[:, :, (2, 1, 0)]
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.imshow(im, aspect='equal')
    bbox = det[i][0][:4]
    score = det[i][0][-1]

    ax.add_patch(
            plt.Rectangle((bbox[0], bbox[1]),
                          bbox[2] - bbox[0],
                          bbox[3] - bbox[1], fill=False,
                          edgecolor='red', linewidth=3.5)
            )
    ax.text(bbox[0], bbox[1] - 2,
                '{:s} {:.3f}'.format('license plate', score),
                bbox=dict(facecolor='blue', alpha=0.5),
                fontsize=14, color='white')

    ax.set_title(('{} detections with '
                  'p({} | box) >= {:.1f}').format('license plate', 'license plate',
                                                  thresh),
                  fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.draw()
plt.show()
