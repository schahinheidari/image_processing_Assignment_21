import matplotlib.pyplot as plt
import numpy as np

n = 5

# create an nxn numpy array
a = np.reshape(np.linspace(0,1,n**2), (n,n))
b = -a

plt.figure(figsize=(12,4.5))

#use imshow to plot the array
plt.subplot(131)
plt.imshow(b,                         #numpy array generating the image
           cmap = 'gray',             #color map used to specify colors
           interpolation='bicubic'    #algorithm used to blend square colors; with 'bicubic' colors will not be blended
          )
plt.xticks(range(n))
plt.yticks(range(n))
plt.title('Gray color map, bicubic blending', y=1.01, fontsize=12)


plt.show()