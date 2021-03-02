#errordiffusion #dithering

This algorithm is based on the concept of error diffusion. Quantization error is diffused to the neighboring pixels according to the following formula, where P is the current pixel and the fraction of the quantization error passed on to the neighboring cells is shown. 


| *   | *   | *  |
|:---:|:---:|--- |
| *   |P    |7/16|
|3/16 |5/16 |1/16|

A simple python implementation will look like this

```python
def dither(img):
    """
    @img: Input image in the form of numpy array
    """
    r, c = img.shape
    for row_idx in np.arange(r):
        for col_idx in np.arange(c):
            old_pixel = img[row_idx][col_idx]
            new_pixel = 255 if old_pixel > 127 else 0
            err = old_pixel - new_pixel
            img[row_idx][col_idx] = new_pixel
            if col_idx + 1 < c:
                img[row_idx][col_idx + 1] += err * 7 // 16
                if row_idx + 1 < r:
                    img[row_idx + 1][col_idx] += err * 5 // 16
                    img[row_idx + 1][col_idx + 1] += err * 1 // 16
                    if col_idx - 1 >= 0:
                        img[row_idx + 1][col_idx - 1] += err * 3 // 16

    return img
```
