# License Plate Recognition
This project constructs a pipeline to detect license plates and read license plate numbers with high accuracy and fast performance. It makes use of [Faster R-CNN](https://github.com/rbgirshick/py-faster-rcnn) and [Attention based OCR](https://github.com/da03/Attention-OCR).

This project was run on Ubuntu 16.04, with Python 2.7. It may work in other environments, but if you want to recreate our results, this environment is your best bet.

# Requirements

Before running anything, first install Faster R-CNN and Attention OCR from their respective github pages (linked above). This will require installing Caffe. This can be a confusing installation. This [guide](https://huangying-zhan.github.io/2016/09/22/detection-faster-rcnn.html) will take you through Faster R-CNN, including the Caffe installation. It will also install any necessary python dependencies/modules.

# Running the LP detector

Make sure you are in the home directory (one level above the master directory for faster r-cnn and attention OCR). You can use your own dataset, or if you want to use our dataset, simply send us a message and we can provide you our dataset.

[Overleaf report](https://www.overleaf.com/9891238nktzqsjtgqcs#/36248536/)
