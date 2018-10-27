from PIL import Image


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
    return _read_image(filename).convert(mode=color_mode)
