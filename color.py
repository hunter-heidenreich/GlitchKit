import numpy as np

seed = 0
np.random.seed(seed=seed)


def color_flip(data):
    """
    A function for flipping the color channels of an image randomly.

    :param data: The image pixel data, a 3D numpy array
    :return: The data, but manipulated, a 3D numpy array
    """
    # Get the color channels to swap
    source_color_channel = np.random.randint(3)
    target_color_channel = np.random.randint(3)

    # 1, 2, swap-a-roo
    data[:, :, source_color_channel], data[:, :, target_color_channel] = \
        data[:, :, target_color_channel], data[:, :, source_color_channel]

    return data
