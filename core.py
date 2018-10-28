from PIL import Image
import numpy as np


def _read_image(filename):
    """
    Reads a file into a Pillow Image

    :param filename: The name of the file to read in, str
    :return: The image, PIL.Image
    """
    return Image.open(filename)


def read_image(filename, color_mode='RGB'):
    """
    Reads a file into a Pillow Image, specifying what color mode is desired.

    :param filename: The name of the file to read in, str
    :param color_mode: The color mode, str
    :return: The image in the specified color mode, PIL.Image
    """
    try:
        return _read_image(filename).convert(mode=color_mode)
    except ValueError:
        print('Not a supported conversion')
        return _read_image(filename)


def list_modes():
    """
    Returns the list of possible color modes to set images to.

    :return: A list of color modes, list[str]
    """
    return ['1', 'L', 'P', 'RGB', 'RGBA', 'CMYK', 'YCbCr', 'LAB',
            'HSV', 'I', 'F']


if __name__ == '__main__':
    test = 'test.jpeg'

    modes = list_modes()

    for m in modes:
        im = read_image(test, m)
        pixels = np.array(im)

        print(im.mode)
        print(im.size)
        print(pixels.shape)
