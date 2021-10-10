#%matplotlib inline

#from skimage import feature, filters
#import numpy as np
#import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage.util import random_noise
from skimage import feature
from PIL import Image

fname = 'Images/Example A.png'
image = Image.open(fname).convert("L")
arr = np.asarray(image)
plt.imshow(arr, cmap='gray', vmin=0, vmax=255)
#plt.show()


# Generate noisy image of a square
#image = np.zeros((128, 128), dtype=float)
#image[32:-32, 32:-32] = 1

#image = plt.imread('Images/Basic.png')

image = ndi.gaussian_filter(image, 3)
image = random_noise(image, mode='speckle', mean=0.1)

# Compute the Canny filter for two values of sigma
edges1 = feature.canny(image)
edges2 = feature.canny(image, sigma=2)
edges3 = feature.canny(image, sigma=3)

# display results
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(8, 3))

ax[0].imshow(edges1, cmap='gray')
ax[0].set_title(r'Canny filter, $\sigma=1$', fontsize=20)

ax[1].imshow(edges2, cmap='gray')
ax[1].set_title(r'Canny filter, $\sigma=2$', fontsize=20)

ax[2].imshow(edges3, cmap='gray')
ax[2].set_title(r'Canny filter, $\sigma=3$', fontsize=20)

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()

"""
import numpy as np
import matplotlib.pyplot as plt

#define the vertical filter
vertical_filter = [[-1,-2,-1], [0,0,0], [1,2,1]]

#define the horizontal filter
horizontal_filter = [[-1,0,1], [-2,0,2], [-1,0,1]]

#read in the pinwheel image
img = plt.imread('Images/Basic.png')

#get the dimensions of the image
n,m,d = img.shape

#initialize the edges image
edges_img = img.copy()
"""
#plt.show()
plt.savefig("Images/Basic Image Edges.png")

print("fini")