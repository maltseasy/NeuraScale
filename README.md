# NeuraScale
[Video](https://youtu.be/MGCR36iL_JM) for Powered by TF2.0 challenge.
[Website](https://aryanmisra.com/neurascale/)
## What it does
_NeuraScale_, the fancy name we gave our project, is basically a Super Resolution Generative Adversarial Network (SRGAN) with the purpose of upscaling image resolutions by a factor of two using deep learning. This way, a picture which initially appears pixellated and/or blurry can be modified so that the features are quite more distinguishable. The model is trained on the COCO unlabeled2017 dataset. Download [here](http://cocodataset.org/#download).

## Requirements
- Tensorflow 2.0
- Scipy, Numpy
- PIL
- Matplotlib
- MS COCO unlabeled2017 Dataset (for training)

## Directory Tree Structure
```
/datasets
  /unlabeled2017
/Neurascale
  /images
    /unlabeled2017
  /main
    /temp
    /tests
    data_loader.py
    preprocessing.py
    srgan.py
  /saves
```
## Usage
To train model (which we highly reccomend doing some more):
```
python srgan.py
```
To run the model on an image:
```
python srgan.py -p image.jpg
```
Thats it!

## Images
**Original:**      

![original1](https://github.com/aryanmisra/NeuraScale/raw/master/main/tests/test1.jpg)

**SuperResolution:**

![superres1](https://github.com/aryanmisra/NeuraScale/raw/master/main/tests/highres_output1.jpg)

**Original:**

![original2](https://github.com/aryanmisra/NeuraScale/raw/master/main/tests/test2.jpg)

**SuperResolution:**

![superres2](https://github.com/aryanmisra/NeuraScale/raw/master/main/tests/highres_output2.jpg)


## How we built it
We used **TensorFlow 2.0** as the API for creating and training our SRGAN. The model was built with Keras and trained on the MS COCO Dataset. Numpy, Matplotlib, and several other libraries were used as well to allow for proper image preprocessing, as different image sizes need to be modified in order to be properly evaluated by the network.

## Challenges we ran into
Since most neural networks require a fixed input/output size, figuring out the image preprocessing was a difficult part of our project, as we ran into many bugs and sighed in frustration multiple times. We found a way to split an image into several regular pieces to be fed into the network and then stitch the output together to end up with a proper, upscaled image.

## What's next for NeuraScale
Our next steps for NeuraScale include smoothing out some of the rough edges in our code, converting the model to use it in a web app with TF.js or as a native app with TF Lite, and possibly retraining the model to output with colour enhancements. 

We also plan to heavily improve our model performance, as hardware limitation have resulted in poor convergence.

## Meta

[Aryan Misra](http://aryanmisra.com)
[Alex Yu](https://alexyu.ca)

Distributed under the GNU General Public License v3.0. See ```license``` for more information.
