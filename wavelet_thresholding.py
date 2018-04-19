import pywt


def wavelet_decomposition(input_array, wavelet_family, level_transformation):
    """
    :param input_array: array of image file
    :param wavelet_family: 'haar', 'db', 'sym', 'coif', 'bior', 'rbio', 'dmey', 'gaus'
    :param level_transformation:
    :return: wavelet coefficients: Approximation, horizontal detail, vertical detail and diagonal detail coefficients respectively
    """

    wavelet_transformation = pywt.Wavelet(wavelet_family)
    WaveletCoeffs = pywt.wavedec2(input_array, wavelet_transformation, level=level_transformation)
    return WaveletCoeffs


def wavelet_thresholding(array_of_wavelet_coeff, threshold, mode_thresholding):
    """
    :param array_of_wavelet_coeff:  wavelet coefficients: Approximation, horizontal detail, vertical detail
            and diagonal detail coefficients respectively
    :param threshold: threshold for Approximation component;
    :param mode_thresholding: {'soft', 'hard', 'greater', 'less'}
    :return: thresholded wavelet coefficients.
    """
    array_of_wavelet_coeff[0] = pywt.threshold(array_of_wavelet_coeff[0], threshold, mode=mode_thresholding)
    return array_of_wavelet_coeff


def wavelet_reconstruction(thresholded_wavelet_coefficents, wavelet_family):
    """
    :param thresholded_wavelet_coefficents:
    :param wavelet_family:
    :return:
    """

    wavelet_transformation = pywt.Wavelet(wavelet_family)
    denoise_image_array = pywt.waverec2(thresholded_wavelet_coefficents, wavelet_transformation)

    return denoise_image_array

