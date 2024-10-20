

import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def encontrar_diferenca(image1, image2):
    assert image1.shape == image2.shape, "Specifica 2 imagens com a mesma forma"
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)
    print("Semelhaça nas imagens", score)
    normalized_difference_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image))
    return normalized_difference_image


def transformacao_histogram(image1, image2):
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image 