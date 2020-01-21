from PIL import Image
import numpy as np
from skimage.color import rgb2hsv
from skimage import data
import matplotlib.pyplot as plt

class image_data:
    def __init__(self, file_name=None):
        #self.rgb_img = np.ndarray(Image.open(f'../sample_images/{file_name}'))
        self.rgb_img = data.coffee()
        self.hsv_img = rgb2hsv(self.rgb_img)
        self.hue_img = self.hsv_img[:, :, 0]
        self.value_img = self.hsv_img[:, :, 2]

    def process(self, hue_threshold=0.04):
        fig, (ax0, ax1, ax2) = plt.subplots(ncols=3, figsize=(8, 2))
        ax0.imshow(self.rgb_img)
        ax0.set_title('RGB image')
        ax0.axis('off')
        ax1.imshow(self.hue_img, cmap='hsv')
        ax1.set_title("Hue channel")
        ax1.axis('off')
        ax2.imshow(self.value_img)
        ax2.set_title('Value Channel')
        ax2.axis('off')

        fig.tight_layout()

        binary_img = self.hue_img > hue_threshold
        fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 3))

        ax0.hist(self.hue_img.ravel(), 512)
        ax0.set_title("Histogram of the Hue channel with threshold")
        ax0.axvline(x=hue_threshold, color='r', linestyle='dashed', linewidth=2)
        ax0.set_xbound(0, 0.12)
        ax1.imshow(binary_img)
        ax1.set_title("Hue-thresholded image")
        ax1.axis('off')

        fig.tight_layout()

        fig, ax0 = plt.subplots(figsize=(4, 3))

        value_threshold = 0.10
        binary_img = (self.hue_img > hue_threshold) | (self.value_img < value_threshold)

        ax0.imshow(binary_img)
        ax0.set_title("Hue and value thresholded image")
        ax0.axis('off')

        fig.tight_layout()
        plt.show()
