# -*- coding: utf-8 -*-
"""
Author: AlexDiPaola

This script loads an image, converts it to grayscale using the HLS lightness channel,
reduces the lightness to a limited number of levels, saves the result,
and exports the grayscale values to a CSV file.
"""

import numpy as np
from PIL import Image
import colorsys

c = 11  # Number of brightness levels to reduce to (e.g., 18 shades of gray)

fileName = 'example.png'  # Input image filename
img = Image.open(fileName)
rgb = np.asarray(img)  # Convert image to NumPy array for pixel-wise processing

# Initialize arrays to store the reduced grayscale image
newRGB = np.zeros((rgb.shape[0], rgb.shape[1], 3))  # RGB image array for output (grayscale in all channels)
newRGBarray = np.zeros((rgb.shape[0], rgb.shape[1]))  # 2D array to hold reduced brightness values for analysis or export

# Loop through each pixel to process
for i in range(rgb.shape[0]):
    for j in range(rgb.shape[1]):
        r, g, b = rgb[i][j][:3]  # Extract red, green, blue components
        
        # Convert RGB to HLS and extract the lightness component (perceptual brightness)
        lightness = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)[1]
        
        # Reduce lightness by rounding to nearest level based on 'c'
        reduced = round(lightness * c) / c
        
        # Assign reduced grayscale value to all RGB channels for the output image
        newRGB[i][j] = reduced
        
        # Store reduced value in the 2D array for exporting or analysis
        newRGBarray[i][j] = reduced

newRGBarray *= c  # Optional: scale values back up to integer range for easier interpretation

# Convert the processed RGB array back to an image (scale from [0,1] to [0,255]) and save as PNG
im = Image.fromarray((newRGB * 255).astype(np.uint8))
im.save("pixel_" + fileName + ".png")

# Export the reduced grayscale values to a CSV file, with values formatted to two decimals
np.savetxt("pixel_" + fileName + "_values.csv", newRGBarray, delimiter=",", fmt="%.2f")