from numpy import *
import scipy.io
import pywt
import matplotlib.pyplot as plt
from PIL import Image


def get_image_array(image):
    #return scipy.misc.imread(image, flatten='true', mode='RGB')
    return scipy.misc.imread(image, mode='RGB')
#print(get_image_array('temp.jpg'))


def get_image_array_with_noise(image, noiseVariance):
    image_with_noise = get_image_array(image) + random.normal(0, noiseVariance, size=get_image_array(image).shape)
    return image_with_noise


def get_denoise_image_array(image_file, wavelet, level_transform, threhold, mode_threholding):
    wavelet_transformation = pywt.Wavelet(wavelet)
    WaveletCoeffs = pywt.wavedec2(get_image_array_with_noise(image_file, 10), wavelet_transformation, level=level_transform)

    cA = pywt.threshold(WaveletCoeffs[0], threhold, mode=mode_threholding)
    cH = WaveletCoeffs[1][0]
    cV = WaveletCoeffs[1][1]
    cD = WaveletCoeffs[1][2]
    thresholded_wavelet = [cA, [cH, cV, cD]]
    denoise_image_array = pywt.waverec2(thresholded_wavelet, wavelet_transformation, mode=mode_threholding)

    return denoise_image_array, thresholded_wavelet, cH


def show_image(image_array):
    plt.axis('off')
    plt.imshow(image_array)
    plt.gray()
    plt.show()





#denoise_array = get_denoise_image_array('temp.jpg', 'db2', 2, 15, 10, 10, 10, 'soft')[0]
#show_image()
#show_image(denoise_array)

# plt.plot(get_denoise_image_array('temp.jpg', 'db1', 1, 10, 200, 200, 200, 'soft')[2])
# plt.show()
#print(get_denoise_image_array('temp.jpg', 'db1', 1, 5, 10, 10, 10, 'soft')[1][1])

#print(get_image_array('temp.jpg'))