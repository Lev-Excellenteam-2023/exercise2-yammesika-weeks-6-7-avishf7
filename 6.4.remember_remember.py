from PIL import Image


def encode(path):
    """
       Extract ASCII characters from black pixels in a black and white image.
       :param path: The path to the image file to process.

       :return: A string containing the extracted ASCII characters.
       """
    result = ""
    image = Image.open(path)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if image.getpixel((x, y)) == 1:
                result += chr(y)

    return result

