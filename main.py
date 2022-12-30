from src.data_utils import load_config_for_template_image, load_config_for_test_images
from src.match_utils import run_template_matching_using_configs


def main():
    for test_config in load_config_for_test_images():
        run_template_matching_using_configs(
            test_config=test_config,
            template_config=load_config_for_template_image(),
            show_images=True,
            verbose=True,
        )

    return


if __name__ == "__main__":
    main()
