import numpy as np
import scipy.misc
import math
import matplotlib.pyplot as plt
from data_loader import DataLoader
from prepreprocessing import ImageSlicer
path = '../../datasets/unlabeled2017/000000002272.jpg'
class ImageProcessor():
    def __init__(self):
        super(ImageProcessor, self).__init__()
        self.channels = 3
        self.lr_height = 200              # Low resolution height
        self.lr_width = 200                  # Low resolution width
        self.lr_shape = (self.lr_height, self.lr_width, self.channels)
        self.hr_height = self.lr_height*2   # High resolution height
        self.hr_width = self.lr_width*2     # High resolution width
        self.hr_shape = (self.hr_height, self.hr_width, self.channels)
        self.dataset_name = 'unlabeled2017'
        self.data_loader = DataLoader(dataset_name=self.dataset_name,
                                      img_res=(self.hr_height, self.hr_width))
        imgs_hr, imgs_lr = self.data_loader.load_pred(path)
        imgs_hr = np.squeeze(imgs_hr)
        print(imgs_hr.shape)
        M, N = 100, 100
        tiles = [imgs_hr[x:x+M,y:y+N] for x in range(0,imgs_hr.shape[0],M) for y in range(0,imgs_hr.shape[1],N)]
        tiles = np.array(tiles, dtype=np.float32)
        print(tiles.shape)

        tiles = (0.5 * tiles) +0.5
        print(np.max(tiles))
        print(np.min(tiles))
        r, c = int(math.ceil(len(tiles[1])/100)), int(math.ceil(len(tiles[2])/100))
        print(r,c)
        # Save generated images and the high resolution originals
        fig=plt.figure(figsize=(r,c))
        for i in range(1, r*c +1):
            img = tiles[i-1,0:100,0:100,0:3]
            fig.add_subplot(r, c, i)
            plt.imshow(img)
        fig.savefig("../images/%s.png" % ("gridded"))
        plt.close()
