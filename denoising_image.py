import image_extract_array
import wavelet_thresholding
import main
from compare_estimation import compare_psnr
from scipy.misc import imread
from skimage import img_as_float


def denoising_image(image, wavelet, mode_thresholding):
    """
    :param image: path to image;
    :param wavelet: 'haar', 'db', 'sym', 'coif', 'bior', 'rbio', 'dmey', 'gaus'
    :param level_of_transformation:
    :param threshold: thresholding value;
    :param mode_thresholding: {'soft', 'hard', 'greater', 'less'}
    :return: denoised image array;
    """
    image_for_threshold = image_extract_array.get_image_array(image)
    image_array = img_as_float(imread(image, mode='L'))
    WaveletCoefficients = wavelet_thresholding.wavelet_decomposition(image_array, wavelet)
    thresholded_wavelet = wavelet_thresholding.wavelet_thresholding(WaveletCoefficients, image_array,
                                                                    mode_thresholding)
    denoised_array = wavelet_thresholding.wavelet_reconstruction(thresholded_wavelet, wavelet)

    return denoised_array, image_array



#result = denoising_image('images/test.jpg', 'db2', 'soft')
#main.show_image(result[0])
#print(compare_psnr(result[1], result[0], data_range=255))

#print(denoising_image('a713.jpg', 'db1', 2, [5, 5, 5, 5], 'soft'))
#main.image_show_PIL(denoising_image('temp.jpg', 'db1', 2, [5, 5, 5, 5], 'soft'))

