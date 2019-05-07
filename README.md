# NeuraScale

## What it does
_NeuraScale_, the fancy name we gave our project, is basically a Super Resolution Generative Adversarial Network (SRGAN) with the purpose of upscaling image resolutions by a factor of two using deep learning. This way, a picture which initially appears pixellated and/or blurry can be modified so that the features are quite more distinguishable. 

## Requirements
- Tensorflow 2.0
- Scipy, Numpy
- PIL
- Matplotlib

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



## How we built it
We used **TensorFlow 2.0** as the API for creating and training our SRGAN. The model was built with Keras and trained on the MS COCO Dataset. Numpy, Matplotlib, and several other libraries were used as well to allow for proper image preprocessing, as different image sizes need to be modified in order to be properly evaluated by the network.

## Challenges we ran into
Since most neural networks require a fixed input/output size, figuring out the image preprocessing was a difficult part of our project, as we ran into many bugs and sighed in frustration multiple times. We found a way to split an image into several regular pieces to be fed into the network and then stitch the output together to end up with a proper, upscaled image.

## What's next for NeuraScale
Our next steps for NeuraScale include smoothing out some of the rough edges in our code, converting the model to use it in a web app with TF.js or as a native app with TF Lite, and possibly retraining the model to output with colour enhancements.
