from src.data_utils import IMG_FOLDER


def get_image_name(image_config):
    return image_config["fname"]


def get_image_url(image_config):
    webhost = image_config["webhost"]
    fname = get_image_name(image_config)
    image_url = f"{webhost}{fname}"
    return image_url


def get_image_local_fname(image_config):
    fname = get_image_name(image_config)
    filetype = image_config["filetype"]
    if not fname.endswith(filetype):
        fname += filetype
    return fname


def get_image_path(image_config):
    return IMG_FOLDER + get_image_local_fname(image_config)


def get_template_scale(image_config):
    try:
        template_scale = image_config["template_scale"]
    except KeyError:
        template_scale = None
    return template_scale
