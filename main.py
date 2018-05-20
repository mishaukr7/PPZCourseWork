from numpy import *
import pywt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



def get_image_array(image):
    return mpimg.imread(image)


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

# def show_image(image_array):
#     img = Image.fromarray(image_array)
#     img.show()