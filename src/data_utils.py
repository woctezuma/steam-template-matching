from src.json_utils import load_json

IMG_FOLDER = "img/"
DATA_FOLDER = "data/"
TEMPLATE_CONFIG = "template.json"
TEST_IMAGES_CONFIG = "test_images.json"


def load_config_for_template_image():
    return load_json(f"{DATA_FOLDER}{TEMPLATE_CONFIG}")


def load_config_for_test_images():
    return load_json(f"{DATA_FOLDER}{TEST_IMAGES_CONFIG}")
