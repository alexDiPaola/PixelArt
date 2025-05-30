# Pixel Veil – Grayscale Lightness Reduction

This script processes an input image (`veil0.png`) by converting it to grayscale using the **lightness component** of the HLS color space. The grayscale values are then **reduced** to a limited number of brightness levels (default is 18), creating a stylized, pixel-art-like effect.

## Features

- Uses perceptual lightness (`HLS`) instead of simple averages or single color channels
- Adjustable brightness reduction level with the `c` variable
- Outputs a new image (`pixel_veil.png`) with reduced grayscale levels
- Exports grayscale brightness values as a CSV file (`pixel_veil_values.csv`) for further analysis or manipulation

## Requirements

- Python 3
- [NumPy](https://numpy.org/)
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)

Install dependencies if needed:

```bash
pip install numpy pillow