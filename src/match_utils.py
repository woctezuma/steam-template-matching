import matplotlib.pyplot as plt
import numpy as np
from skimage.feature import match_template

from src.parse_utils import get_image_name, get_template_scale
from src.pipeline_utils import load_image_from_disk


def compute_correlation_image(image, template):
    return np.squeeze(match_template(image, template))


def compute_score(result, verbose=False):
    score = np.max(result)

    if verbose:
        print(f"Correlation score: {score:.2}")

    return score


def show_template_matching_result(result, image, template, score):
    # Reference: https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_template.html

    ij = np.unravel_index(np.argmax(result), result.shape)
    x, y = ij[::-1]

    if image.shape[0] > image.shape[1]:
        num_rows = 1
        num_columns = 3
    else:
        num_rows = 3
        num_columns = 1

    fig = plt.figure(figsize=(8, 3))
    ax1 = plt.subplot(num_rows, num_columns, 1)
    ax2 = plt.subplot(num_rows, num_columns, 2)
    ax3 = plt.subplot(num_rows, num_columns, 3, sharex=ax2, sharey=ax2)

    ax1.imshow(template, cmap=plt.cm.gray)
    ax1.set_axis_off()
    ax1.set_title("template")

    ax2.imshow(image, cmap=plt.cm.gray)
    ax2.set_axis_off()
    ax2.set_title("image")
    # highlight matched region
    hcoin, wcoin, num_channels = template.shape
    rect = plt.Rectangle((x, y), wcoin, hcoin, edgecolor="r", facecolor="none")
    ax2.add_patch(rect)

    ax3.imshow(np.squeeze(result))
    ax3.set_axis_off()
    ax3.set_title(f"correlation map (max={score:.2})")
    # highlight matched region
    ax3.autoscale(False)
    ax3.plot(x, y, "o", markeredgecolor="r", markerfacecolor="none", markersize=10)

    fig.tight_layout()

    plt.show()

    return


def run_template_matching_using_configs(
    test_config,
    template_config,
    show_images=True,
    verbose=True,
):
    test_image = load_image_from_disk(test_config)
    image_fname = get_image_name(test_config)
    template_scale = get_template_scale(test_config)

    if verbose:
        print(f"\nTest image name: {image_fname}")
        print(f"Template scale: {template_scale}")

    template = load_image_from_disk(template_config, scale=template_scale)

    result = compute_correlation_image(test_image, template)
    score = compute_score(result, verbose=verbose)

    if show_images:
        show_template_matching_result(result, test_image, template, score)

    return
