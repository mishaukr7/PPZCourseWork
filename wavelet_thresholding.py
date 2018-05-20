import pywt
import math
import numpy as np
from skimage.restoration import estimate_sigma


def wavelet_decomposition(input_array, wavelet_family):
    """
    :param input_array: array of image file
    :param wavelet_family: 'haar', 'db', 'sym', 'coif', 'bior', 'rbio', 'dmey', 'gaus'
    :param level_transformation:
    :return: wavelet coefficients: Approximation, horizontal detail, vertical detail and diagonal detail
                coefficients respectively
    """
    wavelet_transformation = pywt.Wavelet(wavelet_family)
    level_transformation = pywt.dwt_max_level(len(input_array), wavelet_transformation)
    WaveletCoeffs = pywt.wavedec2(input_array, wavelet_transformation, level=level_transformation)
    return WaveletCoeffs


def threshold_value(input_array, n, image):
    abs_list = [np.absolute(x-np.median(input_array)) for x in input_array]
    gamma = estimate_sigma(image, multichannel=True)
    #print(gamma)
    return gamma[0] * math.sqrt(2*math.log(n))/2


def wavelet_thresholding(array_of_wavelet_coeff, image, mode_thresholding):
    """
    :param array_of_wavelet_coeff:  wavelet coefficients: Approximation, horizontal detail, vertical detail
            and diagonal detail coefficients respectively
    :param threshold: threshold for Approximation component;
    :param mode_thresholding: {'soft', 'hard', 'greater', 'less'}
    :return: thresholded wavelet coefficients.
    """

    cA = array_of_wavelet_coeff[0]
    denoise_array = [cA]
    for i in range(len(array_of_wavelet_coeff)-1):
        cH = pywt.threshold(array_of_wavelet_coeff[i+1][0],
                            threshold_value(array_of_wavelet_coeff[i+1][2], len(array_of_wavelet_coeff[i+1][0]), image),
                            mode=mode_thresholding)
        cV = pywt.threshold(array_of_wavelet_coeff[i+1][1],
                            threshold_value(array_of_wavelet_coeff[i+1][2], len(array_of_wavelet_coeff[i+1][1]), image),
                            mode=mode_thresholding)
        cD = pywt.threshold(array_of_wavelet_coeff[i+1][2],
                            threshold_value(array_of_wavelet_coeff[i+1][2], len(array_of_wavelet_coeff[i+1][2]), image),
                            mode=mode_thresholding)
        denoise_array.append((cH, cV, cD))
    return denoise_array


def wavelet_reconstruction(thresholded_wavelet_coefficents, wavelet_family):
    """
    :param thresholded_wavelet_coefficents:
    :param wavelet_family:
    :return:
    """

    wavelet_transformation = pywt.Wavelet(wavelet_family)
    denoise_image_array = pywt.waverec2(thresholded_wavelet_coefficents, wavelet_transformation)

    return denoise_image_array


