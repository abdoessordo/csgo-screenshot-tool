import numpy as np
from PIL import Image


def verify_loaded() -> bool:
    img_dir = "./is_loaded.png"
    im = Image.open(img_dir)
    im = im.convert('RGB')
    data = np.array(im)
    first_pixel = data[0][0].tolist()
    acceptable_values = [
        [87, 95, 98],
        [88, 95, 98],
        [87, 95, 97],
    ]

    return first_pixel in acceptable_values
