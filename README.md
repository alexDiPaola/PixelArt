# PixelatorBW – Grayscale Lightness Reduction

This script processes an input image (`example.png`) by converting it to grayscale using the **lightness component** of the HLS color space. The grayscale values are then **reduced** to a limited number of brightness levels (default is 18), creating a stylized, pixel-art-like effect.
Sctipt is zipped. Hit me up for a password.
ig: @alex.dipaola.art
tiktok:@alexdipaolapaint
email: dipaola.alex@gmail.com

## Features

- Uses perceptual lightness (`HLS`) instead of simple averages or single color channels
- Adjustable brightness reduction level with the `c` variable
- Outputs a new image (`pixel_example.png`) with reduced grayscale levels
- Exports grayscale brightness values as a CSV file (`pixel_example_values.csv`) for further analysis or manipulation

## Requirements

- Python 3
- [NumPy](https://numpy.org/)
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)

Install dependencies if needed:

```bash
pip install numpy pillow7:34 PM 5/30/2025
```

## License

This project is licensed under a custom non-commercial license.  
You may use, modify, and share the code **for non-commercial purposes only**, with **attribution**.  
**Commercial use is not allowed** without written permission.

See [LICENSE](./LICENSE) for full terms.



