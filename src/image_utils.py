from pathlib import Path

import mediapy as media
import skimage.io
import skimage.transform

NUM_RGB_CHANNELS = 3


def remove_transparency_channel(image):
    return image[..., :NUM_RGB_CHANNELS]


def reshape_image(image, scale=1.0):
    return skimage.transform.rescale(image, (scale, scale, 1))


def load_image(path_or_url, allow_transparency=False):
    if Path(path_or_url).exists():
        image = skimage.io.imread(path_or_url)
    else:
        image = media.read_image(path_or_url)
    if not allow_transparency:
        image = remove_transparency_channel(image)
    return image
