import cv2
import numpy as np 
import matplotlib.pyplot as plt 

path = r"C:\Users\USER\Pictures\Screenshots\Screenshot 2025-03-15 161038.png"
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
bilateral_image = cv2.bilateralFilter(src = image, d = 5, sigmaColor = 75, sigmaSpace = 75)

plt.subplot(121), plt.imshow(image), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(bilateral_image), plt.title('Bilateral Filtering Image'),
plt.xticks([]), plt.yticks([])
plt.show()
