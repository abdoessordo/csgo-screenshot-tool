import numpy as np
from PIL import Image


def verify_loaded() -> bool:
    # FIXME: Improve this function to be faster and work better with 4K
    img_dir = './tmp/is_loaded.png'
    im = Image.open(img_dir)
    im = im.convert('RGB')
    data = np.array(im)
    first_pixel = data[0][0].tolist()
    acceptable_values = [
        [87, 95, 98],
        [88, 95, 98],
        [87, 95, 97],
        [85, 92, 95],
    ]

    return first_pixel in acceptable_values
