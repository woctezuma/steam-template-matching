from src.image_utils import load_image, reshape_image
from src.parse_utils import get_image_path, get_image_url


def download_image(config, scale=1.0, allow_transparency=False):
    image = load_image(path_or_url=get_image_url(config), allow_transparency=allow_transparency)
    return reshape_image(image, scale=scale)


def load_image_from_disk(config, scale=1.0, allow_transparency=False):
    image = load_image(path_or_url=get_image_path(config), allow_transparency=allow_transparency)
    return reshape_image(image, scale=scale)
