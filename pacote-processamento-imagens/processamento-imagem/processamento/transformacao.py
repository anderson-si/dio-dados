

from skimage.transform import resize

def redimensionar_image(image, proporcao):
    assert 0 <= proporcao <= 1, "Especificar uma proporção válida entre 0 e 1"
    heigth = round(image.shape[0] * proporcao)
    width = round(image.shape[1] * proporcao)
    image_resize = resize(image, (heigth, width), anti_aliasing=True)
    return image_resize